Backend Test
===============
Текст задания - [Backend Test](https://github.com/thakryptex/backend_test/blob/master/Backend_Test.pdf)

Ответ по заданиям - [Backend Answers](https://github.com/thakryptex/backend_test/blob/master/Backend_Answers.pdf)

### Проверено на версиях Python:
* python 3.5.1
* python 2.7.11

### Как запустить проект:

0. Установить Python (автор рекомендует Python >= 3.5)

1. Скачать проект целиком и распаковать в желаемую папку

2. Через терминал зайти в папку проекта и создать виртуальное окружение: `python -m venv virt`

3. Запустить виртуальное окружение: `virt\Scripts\activate` (для Linux или OS X: `source virt/bin/activate`)

4. Из виртуального окружения вызвать команду: `pip install -r requirements.txt`

5. В терминале ввести команду: `python manage.py migrate` (либо использовать db-test.sqlite3 как тестовую базу: там введено 5 URL для проведения теста, superuser: admin, password: admin1234)

6. Запустить: `python manage.py runserver`

7. Перейти на `localhost:8000`, нажать кнопку 'Parse'


### Доп. инфо:
* Используются только базовые библиотеки помимо Django
* Код проверен на python 3.5.1 и python 2.7.11
* Парсинг запускается по нажатию кнопки
* Парсинг сайтов запускается согласно временному сдвигу (timeshift)
* Результат парсинга отображается сразу как информация получена с пропарсенного сайта
* Используется ajax, поскольку в django очень проблемно с websocket’ами
