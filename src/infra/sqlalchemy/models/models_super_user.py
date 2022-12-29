from sqlalchemy import Column, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df

from src.infra.sqlalchemy.models.models_super_user_logs import *


class SuperUser(Base):
    __tablename__ = df.__prefixo__+"super_user"
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(TIMESTAMP)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    classified_as = Column(Integer)
    
    logs = relationship('SuperLog', back_populates='super_user')

# OK
