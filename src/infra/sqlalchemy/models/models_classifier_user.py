from sqlalchemy import Column, Integer, String, ForeignKey, TIMESTAMP
from src.infra.sqlalchemy.config.database import Base
from src.data import default as df


class ClassifierClient(Base):
    __tablename__ = df.__prefixo__ + "classifier_client"
    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    create_at = Column(TIMESTAMP)
    authorization_id = Column(Integer, ForeignKey(df.__prefixo__ + 'authorization.id', name="fk_authorization"))

# OK
