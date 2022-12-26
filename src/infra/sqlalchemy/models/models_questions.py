from sqlalchemy import Column, Integer, String, Boolean, DATETIME, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class Question(Base):
    __tablename__ = df.__prefixo__ + "question"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(DATETIME)
    is_available = Column(Boolean)
    is_alternative = Column(Boolean)
    alternatives = relationship('Alternative', back_populates=df.__prefixo__+'alternative')
    lse_id = Column(Integer, ForeignKey('lse.id', name="fk_lse"))

# OK
