import psycopg2

from config import user, password, host, db_name
def opentable():
    try:
        conn = psycopg2.connect(
            user = user,
            password = password,
            host = host,
            database = db_name
        )

        with conn.cursor() as cursor:
            cursor.execute(
                'SELECT * FROM penis_form;'
            )
            for i in cursor.fetchall():
                print(i)

    except Exception as ex:
        print(ex)
    finally:
        if conn:
            conn.close()
            print('Close')

def add_form():
    forma = input('Какой формы у тебя член, роднуля: ')

    try:
        conn = psycopg2.connect(
            user = user,
            password = password,
            host = host,
            database = db_name
        )

        with conn.cursor() as cursor:
            cursor.execute(
                f'''INSERT INTO penis_form(form)
                VALUES('{forma}')'''
                )
            conn.commit()


            


    except Exception as ex:
        print(ex)

    finally:
        if conn:
            conn.close()
            print('Closee')


opentable()