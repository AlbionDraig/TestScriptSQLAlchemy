from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base
import datetime

class Bot(Base):
    __tablename__ = 'CFG_Bot'
    id = Column(Integer, primary_key=True, autoincrement=True)
    schema = Column(String)
    name = Column(String)
    mainPath = Column(String)
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))))
    updatedAt = Column(DateTime(timezone=True), default=None, onupdate=lambda: datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))))
    steps = relationship('Step', cascade='all, delete, delete-orphan')