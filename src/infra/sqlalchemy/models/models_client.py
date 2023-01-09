from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP, DATE
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df

from src.infra.sqlalchemy.models.models_solicitation import *
from src.infra.sqlalchemy.models.models_user import *
from src.infra.sqlalchemy.models.models_status_client import *
from src.infra.sqlalchemy.models.models_lse import *
from src.infra.sqlalchemy.models.models_response import *


class Client(Base):
    __tablename__ = df.__prefixo__+"client"
    id = Column(Integer, primary_key=True, index=True)
    create_at = Column(TIMESTAMP)
    birth_date = Column(DATE)
    CPF = Column(String)
    name = Column(String)
    cep = Column(String)
    UF = Column(String)
    city = Column(String)
    address = Column(String)
    number = Column(Integer)
    complement = Column(String)
    phone = Column(String)
    line_of_credit = Column(String)
    line_of_business = Column(String)
    start_of_business = Column(DATE)

    status_id = Column(Integer, ForeignKey(df.__prefixo__+'status_client.id', name="fk_status_client"))
    lse_id = Column(Integer, ForeignKey(df.__prefixo__+'lse.id', name="fk_lse"))
    user_id = Column(Integer, ForeignKey(df.__prefixo__+'user.id', name="fk_user"))

    status = relationship('StatusClient', back_populates='clients')
    lses = relationship('Lse', back_populates='clients')
    user = relationship('User', back_populates='clients')
    
    solicitations = relationship('Solicitation', back_populates='client')
    responses_client = relationship('Response', back_populates='client')

# OK
