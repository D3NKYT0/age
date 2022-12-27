from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class Log(Base):
    __tablename__ = df.__prefixo__ + "log"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

# OK
