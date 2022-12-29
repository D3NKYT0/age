from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_questions import *


class Alternative(Base):
    __tablename__ = df.__prefixo__+"alternative"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    weight = Column(Float)
    is_available = Column(Boolean)
    create_at = Column(TIMESTAMP)
    
    question_id = Column(Integer, ForeignKey(df.__prefixo__+'question.id', name="fk_questions"))

    question = relationship('Question', back_populates='alternatives')

# OK
