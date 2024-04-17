import telebot
import openai
import json
import requests
from telebot import types
from bs4 import BeautifulSoup

# Инициализация бота
bot = telebot.TeleBot("6730835793:AAEoy7akpdDJrY4jJX30QlVYSiHEunP47JA")
openai.api_key = "YOUR_OPENAI_API_KEY"

# Функция для парсинга страницы с вариантом
def parse_variant(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Находим блок с заданиями
        tasks_block = soup.find('div', class_='tasks')

        if tasks_block:
            tasks = []
            # Извлекаем текст каждого задания
            for task in tasks_block.find_all('div', class_='task'):
                task_text = task.text.strip()
                tasks.append(task_text)
            
            return tasks
        else:
            return None
    else:
        return None

# Определение разделов и их содержания
sections = {
    "test1": {
        "https://egefizmat.ru/oge-gia-9-klass/oge-gia-fizika/": "ФИЗИКА",
        "https://egefizmat.ru/oge-gia-9-klass/oge-gia-matematika/": "МАТЕМАТИКА",
        "https://ege-centr.ru/courses/9/soc/program": "ОБЩЕСТВОЗНАНИЕ",
        "https://ege-study.ru/ru/oge/materialy/himiya/programma-podgotovki/": "ХИМИЯ",
        "https://ege-centr.ru/courses/9/his/program": "ИСТОРИЯ",
        "https://umschool.net/journal/oge/teoriya-dlya-oge-po-russkomu-yazyku-chto-nuzhno-znat-chtoby-sdat-ekzamen-na-pyaterku/": "РУССКИЙ ЯЗЫК",
        "https://ege-centr.ru/courses/9/bio/program": "БИОЛОГИЯ",
        "https://englishinn.ru/temyi-po-angliyskomu-yazyiku-v-9-klasse.html": "АНГЛИЙСКИЙ"
    },
    "test2": {
        "https://fipi.ru/": "СБОРНИК ЗАДАНИЙ ФИПИ"
    },
    "ChatGPT": {
        "ChatGPT": "ChatGPT"
    },
    "Parse": {
        "https://math-oge.sdamgia.ru/test?id=59754024": "Решить математический вариант ОГЭ"
    }
}

# Преобразование ключей в строковый формат
sections = {str(key): value for key, value in sections.items()}

# Функция для удаления сообщений
def delete_message(chat_id, message_id):
    try:
        bot.delete_message(chat_id, message_id)
    except Exception as e:
        print("Error deleting message:", e)

# Функция для обработки команды /start
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    for section, links in sections.items():
        section_btn = types.InlineKeyboardButton(text=section, callback_data=json.dumps({"section": section}))
        markup.add(section_btn)
    
    # Delete the previous message if it exists
    if message.chat.type == "private":
        try:
            delete_message(message.chat.id, message.message_id)
        except Exception as e:
            print("Error deleting message:", e)
    
    bot.send_message(message.chat.id, "Выберите раздел для изучения или действия:", reply_markup=markup)


# Функция для отправки кнопки "Вернуться в меню"
def return_to_menu():
    markup = types.InlineKeyboardMarkup()
    return_btn = types.InlineKeyboardButton(text="Вернуться в меню", callback_data=json.dumps({"return_to_menu": True}))
    markup.add(return_btn)
    return markup

# Функция для обработки нажатий на разделы и ссылки
@bot.callback_query_handler(func=lambda call: True)
def button_click(call):
    try:
        data = json.loads(call.data)
        if "section" in data:
            section = data["section"]
            if section == "ChatGPT":
                bot.send_message(call.message.chat.id, "в работе...")
            elif section == "Parse":
                for link, name in sections[section].items():
                    tasks = parse_variant(link)
                    if tasks:
                        bot.send_message(call.message.chat.id, f"Вариант ОГЭ: {name}")
                        for task in tasks:
                            bot.send_message(call.message.chat.id, task)
                    else:
                        bot.send_message(call.message.chat.id, f"Не удалось загрузить вариант ОГЭ: {name}")
            else:
                links = sections.get(section, {})
                markup = types.InlineKeyboardMarkup()
                for link, name in links.items():
                    link_btn = types.InlineKeyboardButton(text=name, url=link)
                    markup.add(link_btn)
                markup.add(types.InlineKeyboardButton(text="Вернуться в меню", callback_data=json.dumps({"return_to_menu": True})))
                if links:
                    bot.send_message(call.message.chat.id, f"Ссылки на интересующий вас материал, в разделе \"{section}\":", reply_markup=markup)
                else:
                    bot.send_message(call.message.chat.id, "Нет доступных ссылок, скоро они появятся", reply_markup=return_to_menu())
        elif "return_to_menu" in data:
            start(call.message)
    except Exception as e:
        print("Error:", e)
        bot.send_message(call.message.chat.id, "Что-то пошло не так...")
        # Посылаем сообщение снова с начальным меню
        start(call.message)

# Функция для обработки сообщений для ChatGPT
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    if message.text.strip() != '/start':
        try:
            if message.text.lower() == "вернуться обратно в меню":
                start(message)
            else:
                response = openai.Completion.create(
                    engine="text-davinci-003", 
                    prompt=message.text,
                    max_tokens=150
                )
                bot.send_message(message.chat.id, f"Ответ от ChatGPT: {response.choices[0].text.strip()}")
        except Exception as e:
            print("Error:", e)
            bot.send_message(message.chat.id, "Что-то пошло не так...")

# Функция для обработки первого сообщения пользователя
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_first_message(message):
    if message.text.strip().lower() == '/start':  # Changed 'начать' to '/start'
        start(message)

# Запуск бота
bot.polling()
