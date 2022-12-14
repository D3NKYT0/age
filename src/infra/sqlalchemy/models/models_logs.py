from sqlalchemy import Column, Integer, String, TIMESTAMP, ForeignKey
from src.infra.sqlalchemy.config.database import Base
from sqlalchemy.orm import relationship
from src.data import default as df

from src.infra.sqlalchemy.models.models_user import *


class Log(Base):
    __tablename__ = df.__prefixo__+"log"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)

    user_id = Column(Integer, ForeignKey(df.__prefixo__+'user.id', name="fk_log_user"))

    user = relationship('User', back_populates='logs')

# OK
