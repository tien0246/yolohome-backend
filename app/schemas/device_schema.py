from pydantic import BaseModel

class DeviceCreateSchema(BaseModel):
    feed_id: str
    name: str
    type: str
    location: str
    min_value: float
    max_value: float

class DeviceUpdateSchema(BaseModel):
    name: str | None = None
    type: str | None = None
    location: str | None = None
    min_value: float | None = None
    max_value: float | None = None

class DeviceOutSchema(BaseModel):
    id: str
    user_id: str | None
    name: str
    type: str
    location: str
    min_value: float
    max_value: float
    class Config:
        from_attributes = True
