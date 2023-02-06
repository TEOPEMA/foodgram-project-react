# Проект Foodgram
![example workflow](https://github.com/NIK-TIGER-BILL/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)  
  
[![Python](https://img.shields.io/badge/-Python-464646?style=flat-square&logo=Python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/-Django-464646?style=flat-square&logo=Django)](https://www.djangoproject.com/)
[![Django REST Framework](https://img.shields.io/badge/-Django%20REST%20Framework-464646?style=flat-square&logo=Django%20REST%20Framework)](https://www.django-rest-framework.org/)
[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?style=flat-square&logo=PostgreSQL)](https://www.postgresql.org/)
[![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/)
[![gunicorn](https://img.shields.io/badge/-gunicorn-464646?style=flat-square&logo=gunicorn)](https://gunicorn.org/)
[![docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/)
[![GitHub%20Actions](https://img.shields.io/badge/-GitHub%20Actions-464646?style=flat-square&logo=GitHub%20actions)](https://github.com/features/actions)
[![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/)



---
## Описание проекта «Продуктовый помощник»
Это сайт, на котором пользователи смогут публиковать рецепты, подписываться
на публикации других пользователей, добавлять понравившиеся рецепты в список «Избранное», 
а перед походом в магазин скачивать сводный список продуктов, необходимых для приготовления 
одного или нескольких выбранных блюд.

## Чтобы запустить проект:
### Склонировать репозиторий на свой компьютер:
```
git clone https://github.com/TEOPEMA/foodgram-project-react
```
## Для работы с удаленным сервером (на ubuntu):
* Перейти в каталог infra в командной строке:
```

cd foodgram-project-react/infra/
```

* Заполнить файл infra/.env. Для примера используется редактор nano:
```
sudo nano .env
```

* Из дериктории infra/ запустить docker-compose командой:
```
sudo docker-compose up -d --build
```

* Загрузить статические файлы:
```
sudo docker-compose exec backend python manage.py collectstatic
```
* Выполнить миграции:
```
sudo docker-compose exec backend python manage.py migrate
```

* Создать суперпользователя:
```
sudo docker-compose exec backend python manage.py createsuperuser
```
* Загрузить данные ингредиентов и теги
```
sudo docker-compose exec backend python manage.py loaddata --exclude auth.permission --exclude contenttypes ./data/db.json
```




* Пример заполнения .env файла:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    SECRET_KEY=<секретный ключ проекта django>
    ```
* Для работы с Workflow добавьте в Secrets GitHub переменные окружения для работы:
    ```
    DB_ENGINE=<django.db.backends.postgresql>
    DB_NAME=<имя базы данных postgres>
    DB_USER=<пользователь бд>
    DB_PASSWORD=<пароль>
    DB_HOST=<db>
    DB_PORT=<5432>
    
    DOCKER_PASSWORD=<пароль от DockerHub>
    DOCKER_USERNAME=<имя пользователя>
    
    SECRET_KEY=<секретный ключ проекта django>

    USER=<username для подключения к серверу>
    HOST=<IP сервера>
    PASSPHRASE=<пароль для сервера, если он установлен>
    SSH_KEY=<ваш SSH ключ (для получения команда: cat ~/.ssh/id_rsa)>

    TELEGRAM_TO=<ID чата, в который придет сообщение>
    TELEGRAM_TOKEN=<токен вашего бота>
    ```
    Workflow состоит из трёх шагов:
     - Проверка кода на соответствие PEP8
     - Сборка и публикация образа бекенда на DockerHub.
     - Автоматический деплой на удаленный сервер.
     - Отправка уведомления в телеграм-чат.  
  


## Проект в интернете
Проект запущен и доступен по [http://158.160.15.44/recipes](http://158.160.15.44/recipes)

## Админ-панель:
 [http://158.160.15.44/admin](http://158.160.15.44/admin)
```
teo (Логин)
2580 (Пароль)
```
