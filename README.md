# Платформа дял трейдинга

Данный проект не имеет серьёзного практического применения. Функционал платформы уступает реальным приложениям для трейдинга, но предоставляет пользователю возможность формировать свой портфель акций, облигаций и валют, просматривать историю  действий. Возможно, в будущем возможности платформы будут расширены. Главная цель её создания - ознакомление с принципами API и объектно-ориентированного программирования, а также работа по визуализации.

▎Классы

▎Asset

Класс Asset представляет собой финансовый актив с следующими атрибутами:

• name: Название актива.

• quantity: Количество актива в собственности.

• price_per_unit: Цена за единицу актива.

▎Методы

• price(): Рассчитывает общую стоимость актива на основе его количества и цены за единицу.

• __str__(): Возвращает строковое представление актива.

• __eq__(other): Сравнивает два актива на равенство по их атрибутам.

▎Stock

Класс Stock наследует от класса Asset и представляет собой актив в виде акции.

▎Методы

• Унаследованы все методы из класса Asset.

▎Obligation

Класс Obligation наследует от класса Asset и представляет собой облигацию. Он включает дополнительные атрибуты:

• interest_rate: Процентная ставка облигации.

• maturity_date: Дата погашения облигации.

▎Методы

• total_interest(): Рассчитывает общую сумму процентов, полученных по облигации.

▎Currency

Класс Currency наследует от класса Asset и представляет собой валютный актив.

▎Методы

• convert(target_currency: Currency): Конвертирует сумму этой валюты в целевую валюту на основе обменного курса.

▎StockPortfolio

Класс StockPortfolio представляет собой портфель акций.

▎Методы

• add_asset(asset: Stock): Добавляет акцию в портфель. Если актив с таким же названием уже существует, обновляет его количество.

• remove_asset(asset: Stock): Удаляет акцию из портфеля. Если недостаточно активов для продажи, выводится сообщение об ошибке.

• portfolio_price(): Рассчитывает общую стоимость всех активов в портфеле.

• __str__(): Возвращает строковое представление портфеля, включая все активы и общую стоимость.

# Тинькофф API

▎Функции

• GetFigi(ticker: str): Получает FIGI актива по его тикеру. Возвращает строку с FIGI.

• get_price_by_figi(figi_name: str): Получает текущую цену актива по его FIGI. Возвращает цену в виде числа с плавающей точкой.

# PyQt6 визулизация

С помощью PyQt6 реализована простая визуализация проекта

# Инструкция по использованию

1) Установить все необходимые библиотеки, указанные в requirements.txt

2) Получить на Т-Инвестициях токен для работы с API и вставить его в указанное место в assets.py

3) Запустить файл test.py с помощью команды
  ```bash
  python3 test.py
  ```
