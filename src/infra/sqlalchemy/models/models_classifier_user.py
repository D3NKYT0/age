from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_authorization import *
from src.infra.sqlalchemy.models.models_user import *


class ClassifierUser(Base):
    __tablename__ = df.__prefixo__+"classifier_user"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)
    
    authorization_id = Column(Integer, ForeignKey(df.__prefixo__+'authorization.id', name="fk_authorization"))
    
    autorization = relationship('Authorization', back_populates='classifier')
    
    user = relationship('User', back_populates='classifier')

# OK
