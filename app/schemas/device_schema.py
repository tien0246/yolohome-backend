from pydantic import BaseModel

class DeviceCreateSchema(BaseModel):
    feed_id: str
    user_id: int = None
    name: str
    type: str
    location: str
    min_value: float
    max_value: float

class DeviceOutSchema(BaseModel):
    id: int
    feed_id: str
    user_id: int = None
    name: str
    type: str
    location: str
    min_value: float
    max_value: float
    class Config:
        from_attributes = True
