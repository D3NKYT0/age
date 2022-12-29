from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_client import *


class Solicitation(Base):
    __tablename__ = df.__prefixo__+"solicitation"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)
    
    client_id = Column(Integer, ForeignKey(df.__prefixo__+'client.id', name="fk_client_solicitation"))

    client = relationship('Client', back_populates='solicitations')

# OK
