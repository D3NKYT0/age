from sqlalchemy import Column, Integer, String, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_client import *


class StatusClient(Base):
    __tablename__ = df.__prefixo__+"status_client"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)

    clients = relationship('Client', back_populates='status')

# OK
