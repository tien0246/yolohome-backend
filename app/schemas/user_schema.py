from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str

class UserOutSchema(BaseModel):
    id: int
    name: str
    email: str
    class Config:
        orm_mode = True
