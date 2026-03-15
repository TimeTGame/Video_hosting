# Шаблон сайта видеохостинга на Django

[![pipeline status](https://gitlab.crja72.ru/django/2025/autumn/course/students/167251-serhioalekhin-course-1474/badges/main/pipeline.svg?key_text=Lint+and+Format&key_width=130)](https://gitlab.crja72.ru/django/2025/autumn/course/students/167251-serhioalekhin-course-1474/-/commits/main)

## Требования к работе

[Git](https://git-scm.com/downloads)
[Python](https://www.python.org/downloads/): 3.10, 3.11, 3.12, 3.13

## Установка

Клонируйте репозиторий:

```
git clone https://github.com/TimeTGame/Video_hosting.git
cd Video_hosting
```

### Установка на Mac и Linux

На этом моменте возможно установка зависимостей для prod, test и dev режимов.
Пример для prod режима:

```
python3 -m venv .venv
source venv/bin/activate
python3 -m pip install -r ./requirements/prod.txt
```

Для запуска в других режимах используйте dev.txt и test.txt

### Установка на Windows

На этом моменте возможно установка зависимостей для prod, test и dev режимов.
Пример для prod режима:

```
python -m venv .venv

# Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Windows (cmd.exe)
.\venv\Scripts\activate.bat

python -m pip install -r ./requirements/prod.txt
```

Для запуска в других режимах используйте dev.txt и test.txt

## Запуск

Перейдите в директорию проекта:

```
cd video_hosting
```

Копировать файл template.env и переименовать в .env:

```
cp template.env .env
```

Запуск сервера:

```
# Windows
python manage.py migrate
python manage.py runserver

# Mac и linux
python3 manage.py migrate
python3 manage.py runserver
```

Тестовый сервер хостится по ссылке [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Настройка

Настройки производятся через файл video_hosting/.env
