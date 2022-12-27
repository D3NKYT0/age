from sqlalchemy import Column, Integer, String, DATETIME
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class SuperUser(Base):
    __tablename__ = df.__prefixo__ + "super_user"
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DATETIME)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    classified_as = Column(Integer)
    solicitations = relationship('Solicitation', back_populates='solicitation')
    logs = relationship('SuperLog', back_populates='super_log')

# OK
