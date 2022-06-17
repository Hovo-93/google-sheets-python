import psycopg2
import os
from dotenv import load_dotenv
from psycopg2 import Error
from GetXmlData import get_xml


def database(values):
    usd_rate = float(get_xml().replace(',', '.'))
    connection = False
    try:
        connection = getDb_Connection()
        # Создание курсора для выполнения операций с базой данных
        cursor = connection.cursor()

        # Выполнение команды: это создает новую таблицу
        cursor.execute(getCreate_DbQuery())
        connection.commit()

        print("Таблица успешно создана в PostgreSQL")

        # Заполнение данных
        for item in values:
            cost_in_rur = str(int(item['coast']) * usd_rate)
            # Выполнение SQL-запроса для вставки данных в таблицу
            cursor.execute(
                '''
                   INSERT  INTO  data (NUMBER,ORDER_ID,COST,DELIVERY,COST_IN_RUR) VALUES(%s,%s,%s,%s,%s);
                ''', (item['number'], item['order_id'], item['coast'], item['delivery'],
                      cost_in_rur)
            )

        connection.commit()

    except (Exception, Error) as error:
        print("Ошибка при работе с PostgreSQL", error)

    finally:

        if connection:
            cursor.close()
            connection.close()
            print("Соединение с PostgreSQL закрыто")


# Подключение к базе
def getDb_Connection():
    load_dotenv()

    return psycopg2.connect(
        host=os.getenv('HOST'),
        database=os.getenv('DATABASE'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD')
    )


# SQL-запрос для создания новой таблицы
def getCreate_DbQuery():
    return '''
                DROP TABLE IF  EXISTS data;
                CREATE TABLE  data (
                      id SERIAL  PRIMARY KEY,
                      NUMBER   bigint,
                      ORDER_ID bigint,
                      COST  integer check(COST > 0),
                      COST_IN_RUR text,
                      DELIVERY  text
                );
        '''
