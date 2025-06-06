from sqlalchemy import Column, String, Boolean, TIMESTAMP, func, ForeignKey, Numeric
from app.db.session import Base
import uuid

class SensorData(Base):
    __tablename__ = "Sensor_Data"
    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4)
    device_id = Column(String(36), ForeignKey("Device.id"), nullable=False)
    value = Column(Numeric, nullable=False)
    alert = Column(Boolean, default=False)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())

    def __init__(self, device_id, value, alert=False):
        self.device_id = device_id
        self.value = value
        self.alert = alert