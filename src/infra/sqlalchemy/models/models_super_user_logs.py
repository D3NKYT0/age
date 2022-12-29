from sqlalchemy import Column, Integer, String, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_super_user import *


class SuperLog(Base):
    __tablename__ = df.__prefixo__+"super_log"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)

    super_user = relationship('SuperUser', back_populates='logs')

# OK
