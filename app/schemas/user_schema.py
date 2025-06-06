from pydantic import BaseModel

class UserCreateSchema(BaseModel):
    name: str
    email: str
    password: str

class UserOutSchema(BaseModel):
    id: str
    name: str
    email: str
    class Config:
        from_attributes = True
