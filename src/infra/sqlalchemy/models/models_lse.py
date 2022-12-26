from sqlalchemy import Column, Integer, String, Boolean, DATETIME
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class Lse(Base):
    __tablename__ = df.__prefixo__ + "lse"
    id = Column(Integer, primary_key=True, index=True)
    quiz = Column(String)
    create_at = Column(DATETIME)
    is_available = Column(Boolean)
    questions = relationship('Question', back_populates='question')

# OK
