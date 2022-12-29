from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df

from src.infra.sqlalchemy.models.models_client import *
from src.infra.sqlalchemy.models.models_logs import *
from src.infra.sqlalchemy.models.models_classifier_user import *


class User(Base):
    __tablename__ = df.__prefixo__ + "user"
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(TIMESTAMP)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    
    classified_as = Column(Integer, ForeignKey(df.__prefixo__+'classifier_user.id', name="fk_classifier_user"))

    classifier = relationship('ClassifierUser', back_populates='user')
    
    clients = relationship('Client', back_populates='user')
    logs = relationship('Log', back_populates='user')

# OK
