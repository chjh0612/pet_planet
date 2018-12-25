# encoding: utf-8
#@author: chenjunhua
#time: 2018/12/25 20:08

from sqlalchemy import Column,DateTime, func, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine("mysql+pymysql://root:123456@localhost:3306/spacebox_test", max_overflow=5, encoding='utf-8')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class Record_Time():
    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=func.now())
    updated_at = Column(DateTime, default=func.now(), onupdate=func.now())