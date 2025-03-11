from pydantic import BaseModel, field_validator
from datetime import datetime

class SensorDataInSchema(BaseModel):
    device_id: int
    value: float

class SensorDataOutSchema(BaseModel):
    value: float
    alert: bool
    timestamp: datetime
    class Config:
        from_attributes = True

    @field_validator("timestamp", "before")
    def convert_timestamp(cls, v):
        if isinstance(v, datetime):
            return int(v.timestamp())
        return v