from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Message(Base):
    __tablename__ = 'message'
    id = Column(Integer, primary_key=True)
    id_sender = Column(Integer)
    id_reciever = Column(Integer)
    text = Column(String)
    attachment = Column(String)
    is_sent = Column(Integer)
    is_read = Column(Integer)