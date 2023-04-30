# Hello_Recryto
web-service
Test task from the company Rekruto

### Описание:

Проект представляет собой выполненное тестовое задание
в котором реализованы все основные требования и дополнительные особенности:

* Реализован url endpoint который принимает query параметры name и message и выводит их на главной странице  
* Реализована полноценная система авторизации

### Технологический стэк:
* Python
* Django
* HTML

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone ...
```

```
cd Hello_Recruto
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

```
source venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:
```
cd backend
```

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver  
```