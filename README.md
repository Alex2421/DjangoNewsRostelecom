  ## ⚙️ Проект: сайт хостинговой компании/блог компании:
  
  1. Aдаптирован и использован шаблон  с сайта https://bootstraptema.ru/stuff/templates_bootstrap/blog/hosting/5-1-0-1246
  2. 
  




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
