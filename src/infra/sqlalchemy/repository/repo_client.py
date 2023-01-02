from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session

from src.schemas import schemas_client
from src.infra.sqlalchemy.models import models_client


class RepositoryClient():
    
    def __init__(self, db: Session):
        self.db = db

    def searchById(self, id: int):
        query = select(models_client.Client).where(models_client.Client.id == id)
        Client = self.db.execute(query).first()
        return Client

    def register_client(self, client: schemas_client.Client):

        # conversao do schema em model
        db_client = models_client.Client(
            create_at = client.create_at,
            birth_date = client.birth_date,
            name = client.name,
            cep = client.cep,
            UF = client.UF,
            city = client.city,
            address = client.address,
            number = client.number,
            complement = client.complement,
            phone = client.phone,
            line_of_credit = client.line_of_credit,
            line_of_business = client.line_of_business,
            start_of_business = client.start_of_business,
            status_id = client.status_id,
            lse_id = client.lse_id,
            user_id = client.user_id

        )

        # operações no banco de dados
        self.db.add(db_client)
        self.db.commit()
        self.db.refresh(db_client)

        return db_client

    def edit_client(self, client_id: int, client: schemas_client.Client):
            update_statement = update(models_client.Client).where(
                models_client.Client.id == client_id
            ).values(
                birth_date = client.birth_date,
                cep = client.cep,
                UF = client.UF,
                city = client.city,
                address = client.address,
                number = client.number,
                complement = client.complement,
                phone = client.phone,
                line_of_credit = client.line_of_credit,
                line_of_business = client.line_of_business,
                start_of_business = client.start_of_business,
                status_id = client.status_id,
                lse_id = client.lse_id,
                user_id = client.user_id
            )

            self.db.execute(update_statement)
            self.db.commit()
            return client_id

    def show_all_clients(self):
        client = self.db.query(models_client.Client).all()
        return client

    def remove(self, client_id: int):
        statement = select(models_client.Client).filter_by(id=client_id)
        client_id = self.db.execute(statement).first()

        statement = delete(models_client.Client).where(models_client.Client.id == client_id)
        self.db.execute(statement)
        self.db.commit()

        return client_id
