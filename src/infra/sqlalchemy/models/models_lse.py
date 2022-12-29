from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df

from src.infra.sqlalchemy.models.models_questions import *
from src.infra.sqlalchemy.models.models_client import *


class Lse(Base):
    __tablename__ = df.__prefixo__+"lse"
    id = Column(Integer, primary_key=True, index=True)
    quiz = Column(String)
    create_at = Column(TIMESTAMP)
    is_available = Column(Boolean)
    
    questions = relationship('Question', back_populates='lse')
    clients = relationship('Client', back_populates='lses')

# OK
