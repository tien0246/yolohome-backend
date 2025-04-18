from pydantic import BaseModel
from typing import Union

class DeviceCreateSchema(BaseModel):
    feed_id: str
    name: str
    type: str
    location: str
    min_value: Union[int, float]
    max_value: Union[int, float]

class DeviceUpdateSchema(BaseModel):
    name: str | None = None
    type: str | None = None
    location: str | None = None
    min_value: Union[int, float] | None = None
    max_value: Union[int, float] | None = None

class DeviceOutSchema(BaseModel):
    id: str
    user_id: str | None
    name: str
    type: str
    location: str
    min_value: Union[int, float]
    max_value: Union[int, float]
    class Config:
        from_attributes = True
