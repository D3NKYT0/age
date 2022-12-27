from sqlalchemy import Column, Integer, String
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class StatusClient(Base):
    __tablename__ = df.__prefixo__ + "status_client"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)

# OK
