from sqlalchemy import Column, Integer, String, Enum, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base
import datetime
import enum

class Type(enum.Enum):
    INFO = 1
    WARNING = 2
    ERROR = 3

class Log(Base):
    __tablename__ = 'CFG_Log'
    id = Column(Integer, primary_key=True)
    step = Column(Integer, ForeignKey('CFG_Step.id'))
    type = Column(Enum(Type))
    description = Column(String)
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))))
    updatedAt = Column(DateTime(timezone=True), default=None, onupdate=lambda: datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))))