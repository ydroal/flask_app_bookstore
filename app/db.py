import pymysql
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker
from os import getenv

pymysql.install_as_MySQLdb()
# 環境変数の取得
USER = getenv('USER')
PWD = getenv('DB_PASSWORD')
HOST = getenv('HOST')
DB = getenv('DB')

if not USER or not PWD or not HOST or not DB:
    raise ValueError("Environment variables are not set. Please set USER, DB_PASSWORD, HOST, and DB.")

engine = create_engine(f'mysql://{USER}:{PWD}@{HOST}/{DB}')

# テーブル定義を記述
Base = declarative_base()

class Books(Base):
    __tablename__ = "books"  # テーブル名を指定
    book_id = Column(Integer, primary_key=True)
    title = Column(String(255))
    price = Column(Integer)
    arrival_day = Column(DateTime)


# テーブルが存在しない場合にのみ新しいテーブルをデータベースに作成   
Base.metadata.create_all(engine)
SessionClass = sessionmaker(engine)
session = SessionClass()
