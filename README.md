Тестовое задание "Блог Kodland"
=====================
Проект представляет собой сайт с блогом новостей с возможностью 
добавления новости в блог

-----------------------------------
Для запуска проекта необходимо
-----------------------------------
Установить зависимости:

```bash
pip install -r requirements.txt
```

Указать в конфигурационном файле settings.py в переменной "DATABASES" 
данные для подключения БД Postgresql :

Выполнить следующие команды:

* провести миграции
```bash
python manage.py migrate
```

* запустить отладочный веб-сервер проекта:
```bash
python manage.py runserver
```
