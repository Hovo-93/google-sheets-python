Для запуска

1. pip install -r requirements.txt


2. Создаем БД и прописываем данные в .env файл


    SPREADSHEET_ID='10lbps1OABCyOWO3cVJvT_CQ5-6s9QUC9iqe-rkz5-G8'
    HOST='127.0.0.1'
    DATABASE='postgres'
    USER='postgres'
    PASSWORD='password'

3. Добавить настройки Google Developer Console


    Использовать, полученный в Google Developer Console example.json 
    либо попросить у меня

    Закинуть в корневую директорию проекта файл настроек Google Developer Console по названию credentials.json

    https://console.cloud.google.com/cloud-resource-manager

    
    

4. Запускаем python run.py

Ссылка на google_sheets_table

https://docs.google.com/spreadsheets/d/10lbps1OABCyOWO3cVJvT_CQ5-6s9QUC9iqe-rkz5-G8/edit#gid=0