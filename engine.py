from sqlalchemy import create_engine, text
from sqlalchemy.orm import create_session

engine = create_engine("postgresql+psycopg2://postgres:1337@localhost/shcool")
session = create_session(bind=engine)

def add_data(full_name, number_class, index_class):
    session.execute (text(f"INSERT INTO public.Klass(FIO, number, index) VALUES ('{full_name}', '{number_class}', '{index_class}') "))
    session.commit()
    session.close()