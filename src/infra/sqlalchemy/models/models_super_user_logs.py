from sqlalchemy import Column, Integer, String, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class SuperLog(Base):
    __tablename__ = df.__prefixo__ + "super_log"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)

# OK
