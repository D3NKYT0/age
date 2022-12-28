from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class User(Base):
    __tablename__ = df.__prefixo__ + "user"
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(TIMESTAMP)
    name = Column(String)
    login = Column(String)
    password = Column(String)
    email = Column(String)
    classified_as = Column(Integer, ForeignKey(df.__prefixo__ + 'classifier_user.id', name="fk_classifier_user"))
    clients = relationship('Client', back_populates=df.__prefixo__ + 'client')
    solicitations = relationship('Solicitation', back_populates=df.__prefixo__ + 'solicitation')
    logs = relationship('Log', back_populates=df.__prefixo__ + 'log')

# OK
