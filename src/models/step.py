from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .declarative_base import Base
import datetime

class Step(Base):
    __tablename__ = 'CFG_Step'
    id = Column(Integer, primary_key=True)
    logs = relationship('Log', cascade='all, delete, delete-orphan')
    bot = Column(Integer, ForeignKey('CFG_Bot.id'))
    stepName = Column(String)
    startOver = Column(Boolean, default=False)
    createdAt = Column(DateTime(timezone=True), default=lambda: datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))))
    updatedAt = Column(DateTime(timezone=True), default=None, onupdate=lambda: datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=-5))))