from pydantic import BaseModel
from datetime import datetime

class SensorDataInSchema(BaseModel):
    device_id: int
    value: float

class SensorDataOutSchema(BaseModel):
    id: int
    device_id: int
    value: float
    alert: bool
    timestamp: datetime
    class Config:
        from_attributes = True
