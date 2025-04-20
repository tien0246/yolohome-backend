from pydantic import BaseModel
from enum import Enum
from datetime import datetime

class StatusEnum(str, Enum):
    active = "active"
    inactive = "inactive"
    error = "error"
    maintenance = "maintenance"

class StatusInSchema(BaseModel):
    device_id: str
    type: StatusEnum

class StatusOutSchema(BaseModel):
    id: str
    device_id: str
    type: StatusEnum
    timestamp: datetime
    class Config:
        from_attributes = True
