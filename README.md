
<h1 align="center">Тестовое задание Justhost</h1>

<div align="center">

Выполнено в рамках [тестового задания](https://app.affine.pro/workspace/f6dfe706-59c0-41e5-898b-9d6a25d84efe/axys06NdTgU_NMAga6JC9?mode=page)

[![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Django DRF](https://img.shields.io/badge/Django-%23092E20?style=for-the-badge&logo=django&logoColor=white)](https://www.djangoproject.com/)
[![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
[![Docker](https://img.shields.io/badge/Docker-%230db7ed?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
</div>

## Установка и запуск:

1. Клонирование репозитория:

```
git clone https://github.com/pavlowave/backset.git
cd
```

2. Создание .env файла:
Создайте файл .env в корне проекта с таким содержанием:

```bash
SECRET_KEY=your-django-secret-key
DEBUG=True
DB_HOST=db
DB_NAME=your-db-name
DB_USER=your-db-user
DB_PASSWORD=your-db-password
```

3. Сборка и запуск контейнеров
```bash
docker-compose up --build
```

4. Миграции базы данных После запуска контейнера выполните миграции для настройки базы данных:
```
docker-compose exec web-app python manage.py migrate
```
5. Доступ к приложению Приложение будет доступно по адресу: http://127.0.0.1:8000/api/vps/

## 📋 Основные возможности

API предоставляет следующие функции:

1. **Создание нового виртуального сервера**:
   - Метод: `POST`
   - URL: `http://127.0.0.1:8000/api/vps/`
   - Описание: Создаёт новый VPS с заданными параметрами.
   
   Пример запроса тела:
   ```
    {
    "cpu": 4,
    "ram": 8,
    "hdd": 100,
    "status": "started"
    }
    ```
2. **Получение информации о конкретном сервере по его `uid`**:
   - Метод: `GET`
   - URL: `http://127.0.0.1:8000/api/vps/<uid>/`
   - Описание: Возвращает данные о сервере с указанным `uid`.

3. **Получение списка серверов с фильтрацией**:
   - Метод: `GET`
   - URL: `http://127.0.0.1:8000/api/vps/list/`
   - Описание: Возвращает список всех серверов. Поддерживается фильтрация по следующим параметрам:
     - `cpu`: Количество процессорных ядер.
     - `ram`: Объём оперативной памяти.
     - `status`: Статус сервера (`started`, `stopped`, `blocked`).

4. **Изменение статуса сервера**:
   - Метод: `PATCH`
   - URL: `http://127.0.0.1:8000/api/vps/<uid>/status/`
   - Описание: Позволяет обновить статус сервера.
