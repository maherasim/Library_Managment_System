from . import Base
from sqlalchemy import Column, Integer, String
class User( Base):
    __tablename__ = 'user'
    id = Column(Integer(), primary_key=True,  autoincrement=True)
    email = Column(String(100), unique=True)
    password = Column(String(100), nullable=True)
    name = Column(String(10))

class Books( Base):
    __tablename__ = 'Books'
    id = Column(Integer(), primary_key=True,  autoincrement=True)
    name = Column(String(100), unique=True)
    description = Column(String(100), nullable=True)
    pub_by = Column(String(10))
    copies = Column(String(10))
    checked_out = Column(String(10))
    checked_out_by1 = Column(String(10))