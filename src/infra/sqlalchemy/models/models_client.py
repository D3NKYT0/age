from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from sqlalchemy.orm import relationship
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class Client(Base):
    __tablename__ = df.__prefixo__ + "client"
    id = Column(Integer, primary_key=True, index=True)
    
    create_at = Column(TIMESTAMP)
    birth_date = Column(TIMESTAMP)
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
    start_of_business = Column(TIMESTAMP)

    status_id = Column(Integer, ForeignKey(df.__prefixo__ + 'status_client.id', name="fk_status_client"))
    lse_id = Column(Integer, ForeignKey(df.__prefixo__ + 'lse.id', name="fk_lse"))
    user_id = Column(Integer, ForeignKey(df.__prefixo__ + 'user.id', name="fk_user"))
    solicitations = relationship('Solicitation', back_populates=df.__prefixo__ + 'solicitation')

# OK
