from pydantic import BaseModel, field_validator
from datetime import datetime

class AlertOutSchema(BaseModel):
    device_id: str
    name: str
    value: float
    timestamp: int

    @field_validator("timestamp", mode="before", check_fields=False)
    def to_unix(cls, v):
        if isinstance(v, datetime):
            return int(v.timestamp())
        return v

    class Config:
        from_attributes = True
