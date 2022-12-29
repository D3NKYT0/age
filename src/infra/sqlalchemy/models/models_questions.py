from sqlalchemy import Column, Integer, String, Boolean, TIMESTAMP, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df

from src.infra.sqlalchemy.models.models_alternative import *
from src.infra.sqlalchemy.models.models_lse import *
from src.infra.sqlalchemy.models.models_response import *


class Question(Base):
    __tablename__ = df.__prefixo__+"question"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)
    is_available = Column(Boolean)
    is_alternative = Column(Boolean)

    lse_id = Column(Integer, ForeignKey(df.__prefixo__+'lse.id', name="fk_lse"))

    lse = relationship('Lse', back_populates='questions')
    
    alternatives = relationship('Alternative', back_populates='question')
    responses_question = relationship('Response', back_populates='question')

# OK
