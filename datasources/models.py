from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select, insert
from config import *

# DB connection
if mysql == True:
    engine = create_engine('mysql+pymysql://'+db_user+':' +
                           db_pass+'@'+db_host+'/'+database+'?charset=utf8mb4')
else:
    engine = create_engine(
        'sqlite:///datasources/database/database.db', echo=False)

meta = MetaData()

# Table testing
logs_testing = Table(
    'logs_testing', meta,
    Column('id', Integer, primary_key=True),
    Column('timestamp', String(255), nullable=False),
    Column('username', String(255), nullable=False),
    Column('os_username', String(255), nullable=False),
    Column('action_name', String(255), nullable=False),
    Column('owner', String(255), nullable=False),
    Column('obj_name', String(255), nullable=False),
    Column('current_user', String(255), nullable=False),
    Column('return_code', Integer, nullable=False),
)

meta.create_all(engine)

conn_mysql = engine.connect()
