from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey, DATETIME
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class Alternative(Base):
    __tablename__ = df.__prefixo__ + "alternative"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    weight = Column(Float)
    is_available = Column(Boolean)
    create_at = Column(DATETIME)
    question_id = Column(Integer, ForeignKey('question.id', name="fk_questions"))

# OK