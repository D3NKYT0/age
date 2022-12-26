from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class User(Base):
    __tablename__ = df.__prefixo__ + "user"
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(DATETIME)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    classified_as = Column(Integer, ForeignKey('classifier_client.id', name="fk_classifier_client"))
    clients = relationship('Client', back_populates='client')
    solicitations = relationship('Solicitation', back_populates='solicitation')
    logs = relationship('Log', back_populates='log')

# OK
