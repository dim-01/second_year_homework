# Проект: Обработка данных

## Цель проекта
Этот проект предоставляет инструменты для обработки данных, представленных в виде списка словарей. Основные функции включают фильтрацию данных по состоянию (`state`) и сортировку по дате (`date`).

## Установка
1. Склонируйте репозиторий:
      ```bash
   git clone https://github.com/ваш-username/ваш-репозиторий.git
2. Перейдите в директорию проекта:
      ```bash
   cd ваш-репозиторий
3. Установите зависимости (если они есть):
      ```bash
         pip install -r requirements.txt
## Использование
1. Модуль processing 

filter_by_state(data, state="EXECUTED"): Фильтрует список словарей по значению ключа state.

sort_by_date(data, reverse=True): Сортирует список словарей по ключу date.

2. Модуль masks

get_mask_card_number(card_number): Маскирует номер карты.

get_mask_account(account_number): Маскирует номер счёта.

3. Модуль widget

mask_account_card(input_data): Маскирует номер карты или счёта в зависимости от входных данных.

get_date(input_date): Преобразует дату из формата ISO в формат DD.MM.YYYY.

## Запуск тестов
1. Установите pytest и pytest-cov:
   ```bash 
   pip install pytest pytest-cov

2. Запустите тесты:
   ```bash
   pytest tests/
3. Проверьте покрытие кода:
   ```bash
   pytest --cov=src tests/
   