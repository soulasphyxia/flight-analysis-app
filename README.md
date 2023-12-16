# Прогнозирование цен на авиабилеты
Приложение разработано для предсказывания данных о стоимости билетов на самолет, основываясь на собранных данных об уже прошедших полетах.

## Инструкция по запуску:
### 1. Склонировать репозиторий, перейти в папку с проектом:
`git clone git@github.com:soulasphyxia/flight-analysis-app.git`
### 2. Создать виртуальное окружение:
`python -m venv venv`
### 3. Активировать виртуальное окружение venv.
* `source /venv/bin/activate` для Linux\
* `.\venv\Scripts\activate` для Windows

### 4. Установить необходимые зависимости:
`pip install -r requirements.txt`
### 5. Открыть 2 окна терминала и запустить 2 локальных сервера:
`flask run` для запуска backend API\
`streamlit run ./mainpage.py` для запуска frontend сервера


## Описание:
1. Для получения основной модели для анализа использовался PyCaret, были обучены различные модели машинного обучения на предварительно подготовленном датасете. Среди выбранных моделей выделяется XGBoost из-за его высокой производительности и точности предсказаний.
2. Из-за нехватки данных в открытых источниках, для анализа был выбран датасет с информацией о ценах на авиабилеты в Индии на момент 2019 года. Не смотря на неактуальность данных, прогноз получился весьма точным ([пример](https://www.makemytrip.com/flight/search?itinerary=BLR-DEL-14/03/2024&tripType=O&paxType=A-1_C-0_I-0&intl=false&cabinClass=E&ccde=IN&lang=eng)). Результат работы приложения для аналогичного запроса Вы можете увидеть ниже.
3. Одним из требований к задаче было использование базы данных SQLite, но в ходе разработки было принято решение не использовать хранилище данных из-за ненадобности: на данный момент нам не удалось получить нужную нам информацию из открытых источников(все API, которые удалось найти, имели нужный функционал, представленный только в платной версии).
4. Приложение на наш взгляд имеет интуивно понятный интерфейс: пользователю всего-лишь нужно выбрать город отбытия, город прибытия, необходимую дату. На выходе пользователь получает информацию о прогнозируемой цене билетов от разных авиакомпаний(отсортированных от самых дешевых к самым дорогим)
5. На момент сдачи работы в ходе различных трудностей не был реализован деплой приложения(обертка в Docker-образ/хостинг)

## Скриншот интерфейса веб-приложения
![image](https://github.com/soulasphyxia/flight-analysis-app/assets/98162330/e10642fb-c72f-47fc-a2e9-4289e16b9c10)
