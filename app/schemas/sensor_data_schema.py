from pydantic import BaseModel, field_validator
from datetime import datetime

class SensorDataInSchema(BaseModel):
    device_id: int
    value: float

class SensorDataOutSchema(BaseModel):
    value: float
    alert: bool
    timestamp: int

    @field_validator("timestamp", mode="before", check_fields=False)
    def convert_timestamp(cls, v):
        if isinstance(v, datetime):
            return int(v.timestamp())
        return v

    class Config:
        from_attributes = True