from sqlalchemy import Column, String, Float, Boolean, TIMESTAMP, func, ForeignKey
from app.db.session import Base

class SensorData(Base):
    __tablename__ = "Sensor_Data"
    id = Column(String(36), primary_key=True, index=True)
    device_id = Column(String(36), ForeignKey("Device.id"), nullable=False)
    value = Column(Float, nullable=False)
    alert = Column(Boolean, default=False)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())

    def __init__(self, device_id, value):
        self.device_id = device_id
        self.value = value
