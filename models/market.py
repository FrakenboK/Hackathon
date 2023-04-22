from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Market(Base):
   __tablename__ = 'users'
   
   name = Column(String, primary_key=True)
   code = Column(String)