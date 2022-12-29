from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_questions import *
from src.infra.sqlalchemy.models.models_client import *


class Response(Base):
    __tablename__ = df.__prefixo__+"response"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)
    
    question_id = Column(Integer, ForeignKey(df.__prefixo__+'question.id', name="fk_questions"))
    client_id = Column(Integer, ForeignKey(df.__prefixo__+'client.id', name="fk_clients"))

    question = relationship('Question', back_populates='responses_question')
    client = relationship('Client', back_populates='responses_client')

# OK
