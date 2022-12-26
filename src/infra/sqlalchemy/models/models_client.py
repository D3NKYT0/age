from sqlalchemy import Column, Integer, String, ForeignKey, DATETIME
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class Client(Base):
    __tablename__ = df.__prefixo__ + "client"
    id = Column(Integer, primary_key=True, index=True)
    
    create_at = Column(DATETIME)
    birth_date = Column(DATETIME)
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
    start_of_business = Column(DATETIME)

    status_id = Column(Integer, ForeignKey('status.id', name="fk_status"))
    lse_id = Column(Integer, ForeignKey('lse.id', name="fk_lse"))
    user_id = Column(Integer, ForeignKey('user.id', name="fk_user"))
    solicitations = relationship('Solicitation', back_populates='solicitation')

# OK
