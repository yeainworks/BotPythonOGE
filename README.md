# Бот для обучения и помощи с подготовкой к ОГЭ

Этот бот представляет собой удобный инструмент для обучения и подготовки к ОГЭ (Основному государственному экзамену) с использованием различных онлайн-ресурсов и искусственного интеллекта.

# Библиотеки Python для проекта

Ниже приведен список всех библиотек Python, необходимых для работы проекта, а также их версии.

## Установка

Вы можете установить все необходимые библиотеки с помощью pip. Просто выполните следующую команду:

```bash
pip install -r requirements.txt
```

## Особенности

- **Выбор раздела:** Бот предлагает различные разделы для изучения, включая различные предметы и источники, такие как материалы ФИПИ, задания по конкретным предметам и другие полезные ссылки.

- **Поддержка ChatGPT:** Бот использует мощные модели искусственного интеллекта, такие как ChatGPT, чтобы помочь вам с ответами на вопросы и объяснениями.

- **Парсинг заданий ОГЭ:** Бот может извлекать и отправлять вам задания ОГЭ из указанных онлайн-ресурсов для дополнительной практики.

## Установка и настройка

1. **Установка зависимостей:** Убедитесь, что у вас установлены все необходимые зависимости, перечисленные в `requirements.txt`. Вы можете установить их, выполнив команду `pip install -r requirements.txt`.

2. **Настройка токенов:** Замените `"YOUR_TELEGRAM_BOT_TOKEN"` и `"YOUR_OPENAI_API_KEY"` в коде на свои реальные токены Telegram бота и ключ OpenAI API соответственно.

3. **Запуск бота:** После установки зависимостей и настройки токенов, запустите бота, выполнив скрипт `bot.py`.

## Использование

1. **Команда /start:** Начните разговор с ботом, отправив команду `/start`. Бот предложит вам выбрать раздел для изучения или действия.

2. **Выбор раздела:** Выберите раздел, который вас интересует, нажав на соответствующую кнопку. Бот предоставит вам доступ к материалам и функциям выбранного раздела.

3. **Интерактивный диалог:** Если вы выберете раздел "ChatGPT", бот предложит вам задать вопрос или написать предложение, и модель ChatGPT предоставит ответ или объяснение.

4. **Практика с заданиями ОГЭ:** Если вы выберете раздел с заданиями по ОГЭ, бот извлечет задания из соответствующего источника и отправит их вам для дополнительной практики.

## Вклад в проект

Вы можете вносить свой вклад в развитие этого проекта, предлагая улучшения, исправляя ошибки и добавляя новые функции через пулл-реквесты.

## Лицензия

Этот проект распространяется под лицензией [MIT License](LICENSE).
