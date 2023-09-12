from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    capital = Column(String)  
    currency = Column(String)
    continent = Column(String)
    language = Column(String)
    population = Column(Integer)
    flag = Column(String)