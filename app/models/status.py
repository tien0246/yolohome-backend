import enum
from sqlalchemy import Column, Integer, Enum, TIMESTAMP, func, ForeignKey
from app.db.session import Base

class StatusEnum(enum.Enum):
    active = "active"
    inactive = "inactive"
    error = "error"
    maintenance = "maintenance"

class Status(Base):
    __tablename__ = "Status"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("Device.id"), nullable=False)
    type = Column(Enum(StatusEnum), nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
