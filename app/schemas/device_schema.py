from pydantic import BaseModel

class DeviceCreateSchema(BaseModel):
    feed_id: str
    name: str
    type: str
    location: str
    min_value: float
    max_value: float

class DeviceOutSchema(BaseModel):
    name: str
    type: str
    location: str
    min_value: float
    max_value: float
    class Config:
        from_attributes = True
