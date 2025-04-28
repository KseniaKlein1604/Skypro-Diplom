# Aviasales Autotests Project

## Описание проекта
Проект тестирует базовые сценарии поиска и покупки авиабилетов через сайт Aviasales.

Покрытие:
- UI тесты: поиск билетов, покупка билетов, фильтрация параметров
- API тесты: позитивные и негативные сценарии работы с профилем пользователя

## Структура проекта
- `/test/test_ui.py` — UI автотесты
- `/test/test_api.py` — API автотесты
- `/config/settings.py` — настройки проекта
- `/data/` — тестовые данные
- `/postman/` — Postman коллекции и тест-раны
- `/reports/` — Allure-отчеты
- `/data/manual_test_results/` — результаты ручного тестирования

## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Переменные окружения
Создайте файл `.env` и добавьте туда токен:
```bash
API_TOKEN=your_token_here
```

## Как запускать тесты
Запуск всех тестов:
```bash
pytest --alluredir=reports/
```

Запуск только UI тестов:
```bash
pytest -m ui --alluredir=reports/
```

Запуск только API тестов:
```bash
pytest -m api --alluredir=reports/
```

## Генерация отчета Allure
```bash
allure serve reports/
```

## Ссылки на исходные материалы
- Чек-листы ручного тестирования: `/data/manual_test_results/`
- Постман коллекция: `/postman/`
