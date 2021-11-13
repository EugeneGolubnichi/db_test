from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey
from config import user, password, host, db_name
import psycopg2
from sqlalchemy.orm import sessionmaker

metadata = MetaData()
penis_form = Table('penis_form', metadata,

        Column('form_id', Integer, primary_key=True),
        Column('form', String(255))
                    )

#Session = sessionmaker(bind=engine)
#penis_form = Table('penis_form', meta,
#                   Column('form_id', Integer, primary_key=True ),
#                   Column('form', String(250), nullable =  False)
#)
#engine = create_engine(f"postgresql://{user}:{password}@{host}/{db_name}")
#engine.connect()

#Session.configure(bind=engine)

#conn = engine.connect()
#s = penis_form.select()
#result = conn.execute(s).fetchall()
#for i in result:
  #  print(i)


def opentable():
    try:
        engine = create_engine(f"postgresql://{user}:{password}@{host}/{db_name}")
        engine.connect()

        with engine.connect() as conn:
            s = penis_form.select()
            result = conn.execute(s).fetchall()
            for i in result:
                print(i)
    except Exception as ex:
        print (f'Something gone wrong: ({Exception})')
    finally:
        conn.close()


def insert_smth():
    try:
        engine = create_engine(f"postgresql://{user}:{password}@{host}/{db_name}")
        engine.connect()

        with engine.connect() as conn:
            ins = input('Какой формы?')
            query = penis_form.insert().values(form = ins)
            result = conn.execute(query)
            print(result)

    except Exception as ex:
        print (f'Something gone wrong: ({Exception})')
    finally:
        conn.close()
insert_smth()
opentable()
