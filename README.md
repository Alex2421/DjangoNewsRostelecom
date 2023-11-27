
  <h1>
    Проект находится в директории /host 
  </h1>
  <h3>
    ДЗ_№1 (тема сайт хостинговой компании) 
  </h3>
  <p>
     1.Шаблон сайта и главной страницы
  </p>
  <p>
     2.Шаблон для навигации верхняя и боковая панель.
  </p>
  <p>
    3.Шаблон для отдельной страницы о нас / планы хостинга.
  </p>
  <p>
     4.Страница регистрации пользователя.
  </p>
  



## ⚙️ Установка и настройка проекта:

  1. Скопируйте репозиторий на ваше машину:
```bash
git clone https://github.com/..............
```
  2. Требуется создать и активировать виртуальную среду:
```bash
$ python -m venv venv
или создать ее в IDE

# Активация виртуальной среды в Windows:
$ source venv/Scripts/activate

# Активация виртуальной среды в Linux/Mac:
$ source venv/bin/activate
```
  3. Установка и создание requirements.txt пакета в python:
```bash
$ pip install -r requirements.txt
# создание requirements.txt
 pip freeze > requirements.txt
``` 
  4. Создание superuser :
```bash
$ python manage.py createsuperuser
```
```
#  Не создаеться superuser:  
Поставь в сеттингах вместо ru-ru en-en, после активации можно поменять.
ошибка: django.db.utils.OperationalError: no such table: auth_user
Решение - требуется сделать миграцию в БД ./manage.py migrate. После этого все запускается.
```  
 5. Запуск Django сервера:
```bash
$ python manage.py runserver
``` 
