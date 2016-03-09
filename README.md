Backend Test
===============
Текст задания - Backend_Test.pdf

Ответ по заданиям - Backend_Answers.pdf

### Проверено на версиях Python:
* python 3.5.1
* python 2.7.11

### Как запустить проект:

1. Скачать проект целиком и распаковать в желаемую папку

2. Через терминал зайти в папку проекта и создать виртуальное окружение: `python -m venv virt`

3. Запустить виртуальное окружение: `virt\Scripts\activate`

4. Из виртуального окружения вызвать команду: `pip install -r requirements.txt`

5. В терминале ввести команду: `python manage.py migrate` (либо использовать db-test.sqlite3 как тестовую базу: там введено 5 URL для проведения теста, superuser: admin, password: admin1234)

6. Запустить: `python manage.py runserver`

7. Перейти на `localhost:8000`
