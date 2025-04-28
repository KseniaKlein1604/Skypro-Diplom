# Aviasales Autotests Project

## Описание проекта
Проект тестирует базовые сценарии поиска и покупки авиабилетов через сайт Aviasales.

Покрытие:
- UI тесты: поиск билетов, покупка билетов, фильтрация параметров
- API тесты: позитивные и негативные сценарии работы с профилем пользователя

## Структура проекта
- `/test/test_ui.py` — UI автотесты
- `/test/test_api.py` — API автотесты


## Установка зависимостей
```bash
pip install -r requirements.txt
```

## Переменные окружения
 Тесты настроены только с авторизациией по токену.
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
- Чек-листы ручного тестирования:
  1.Функциональное и регрессионное :`https://chlist.sitechco.ru/project/53386/checklist`
  2.Smoke и приемочное : `https://app.qase.io/project/FP?case=2&suite=1` `https://app.qase.io/project/FP?case=2&suite=1`
- Постман коллекция: `file:///C:/Users/alisa/Downloads/18%2018_25_1267631388940cf9.23525340%D0%A4%D0%98%D0%9D%D0%90%D0%9B%D0%AC%D0%9D%D0%AB%D0%99%D0%9F%D0%A0%D0%9E%D0%95%D0%9A%D0%A2.postman_test_run%20(1).json` `file:///C:/Users/alisa/Downloads/18%2018_25_1067631386e5e567.10214256%D0%A4%D0%98%D0%9D%D0%90%D0%9B%D0%AC%D0%9D%D0%AB%D0%99%D0%9F%D0%A0%D0%9E%D0%95%D0%9A%D0%A2.postman_collection%20(1).json`
