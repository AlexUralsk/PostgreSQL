import psycopg2
from config import host, port, user, password, db_name
try :
    # создаем подключение к базе данных
    connection = psycopg2.connect(
        host = host,
        user = user,
        password = password,
        database = db_name,
        port = port
    )
    # создаем курсор
    #cursor = connection.cursor()
    with connection.cursor() as cursor:
         cursor.execute(
              'SELECT version();'
         )
         print(f'версия сервира: {cursor.fetchone()}')
except Exception as ex:
       print("[INFO] Error while working with PostgreSQL", ex)
finally:
    pass 