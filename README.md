# Финансовый многопользовательский сервис (FastAPI)

![finance_service](img/finance_service.png)

Данный проект представляет собой бэкенд на основе `FastAPI` для управления финансовыми операциями.

Включает функционал для пользователей, счетов, категорий и транзакций. 

Проект предполагает работу, как `RESTful API`, так и многостраничного интерфейса с личным кабинетом и аналитикой.

## Основные функции

- **Личный кабинет**: Возможность просмотра и управления своими финансами.
- **Управление пользователями**: Регистрация и аутентификация.
- **Счета**: Создание и управление счетами, учет балансов.
- **Категории**: Добавление категорий для классификации операций.
- **Транзакции**: Ведение доходов и расходов, связанные с конкретными счетами и категориями.
- **Аналитика**: Построение графиков и таблиц для анализа финансов.

## Структура проекта

```
financial_operations_project/
├── app/                          # Основное приложение
│   ├── __init__.py               # Инициализация приложения FastAPI
│   ├── main.py                   # Точка входа в приложение
│   ├── models.py                 # SQLAlchemy-модели для базы данных
│   ├── routes/                   # Маршруты приложения
│   │   ├── __init__.py           # Инициализация маршрутов
│   │   ├── auth.py               # Маршруты для аутентификации и регистрации пользователей
│   │   ├── accounts.py           # Маршруты для работы со счетами пользователей
│   │   ├── categories.py         # Маршруты для работы с категориями расходов и доходов
│   │   ├── transactions.py       # Маршруты для работы с финансовыми транзакциями
│   │   └── analytics.py          # Маршруты для аналитики и отчетов
│   └── templates/                # Шаблоны HTML для интерфейса
│       ├── base.html             # Базовый шаблон
│       ├── dashboard.html        # Панель управления (личный кабинет)
│       ├── login.html            # Страница входа
│       ├── register.html         # Страница регистрации
│       ├── account_details.html  # Детализация счетов
│       ├── analytics.html        # Страница аналитики
│       └── transaction_list.html # Список транзакций
│
├── migrations/                   # Миграции базы данных (если используется Alembic)
├── financial_operations.db       # Файл базы данных SQLite
├── README.md                     # Описание проекта, инструкция по установке и запуску
├── requirements.txt              # Список зависимостей Python
├── .env                          # Конфигурация приложения (секреты и настройки окружения)
└── run.py                        # Файл для запуска приложения
```

## Эндпоинты API

### Пользователи

- **POST** `/users/`  
  Создание нового пользователя.

### Счета

- **POST** `/accounts/`  
  Создание нового счета.

### Категории

- **POST** `/categories/`  
  Добавление новой категории.

### Транзакции

- **POST** `/transactions/`  
  Запись новой транзакции (доход или расход).

## Инструкция по настройке

### Требования

- Python 3.8+
- pip

### Установка

1. Склонируйте репозиторий:
   ```bash
   git clone <repository_url>
   cd financial_operations_project
   ```

2. Создайте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate   # В Windows: venv\Scripts\activate
   ```

3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

4. Запустите приложение:
   ```bash
   uvicorn main:app --reload
   ```

5. Доступ к API-документации:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
   - ReDoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

6. Доступ к интерфейсу:
   - Главная страница: [http://127.0.0.1:8000](http://127.0.0.1:8000)

## База данных

### Таблицы

- **`users`**  
  - `id`: Первичный ключ  
  - `username`: Уникальное имя пользователя  
  - `email`: Уникальный адрес электронной почты  
  - `password_hash`: Захэшированный пароль  
  - `created_at`: Время создания

- **`accounts`**  
  - `id`: Первичный ключ  
  - `user_id`: Внешний ключ на `users`  
  - `name`: Название счета  
  - `balance`: Баланс счета  
  - `created_at`: Время создания

- **`categories`**  
  - `id`: Первичный ключ  
  - `user_id`: Внешний ключ на `users`  
  - `name`: Название категории  
  - `created_at`: Время создания

- **`transactions`**  
  - `id`: Первичный ключ  
  - `user_id`: Внешний ключ на `users`  
  - `account_id`: Внешний ключ на `accounts`  
  - `category_id`: Внешний ключ на `categories`  
  - `type`: Тип транзакции (`доход` или `расход`)  
  - `amount`: Сумма транзакции  
  - `description`: Описание (опционально)  
  - `transaction_date`: Дата транзакции

## Лицензия

Проект распространяется под лицензией MIT.



**Автор:** Дуплей Максим Игоревич

**TG:** @quadd4rv1n7

**Дата:** 17.12.2024
