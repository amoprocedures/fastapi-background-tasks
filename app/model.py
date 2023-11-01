from pydantic import BaseModel


class Message(BaseModel):
    title: str
    message: str
