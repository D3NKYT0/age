from pydantic import BaseModel


class Email(BaseModel):
    destination_email: str
    subject: str
    content: str

    class Config:
        orm_mode = True
