import os
import gspread
import httplib2
from dotenv import load_dotenv
from googleapiclient import discovery
from oauth2client.service_account import ServiceAccountCredentials
from db_worker import database
from prepare_data import prepare_date

load_dotenv()
# Файл, полученный в Google Developer Console
CREDENTIALS_FILE = 'credentials.json'
# ID Google Sheets документа (можно взять из его URL)
spreadsheet_id = os.getenv('SPREADSHEET_ID')

# Авторизуемся и получаем service — экземпляр доступа к API
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive'])
httpAuth = credentials.authorize(httplib2.Http())
service = discovery.build('sheets', 'v4', http=httpAuth)

# Пример чтения файла
# spreadsheet — это Google-документ с таблицами.
values = service.spreadsheets().values().get(
    spreadsheetId=spreadsheet_id,
    range='Лист1',
    majorDimension='ROWS'
).execute()
# Обработка и запись данных в базу
database(prepare_date(values))
