from sqlalchemy import Column, Integer, Float, Boolean, TIMESTAMP, func, ForeignKey
from app.db.session import Base

class SensorData(Base):
    __tablename__ = "Sensor_Data"
    id = Column(Integer, primary_key=True, index=True)
    device_id = Column(Integer, ForeignKey("Device.id"), nullable=False)
    value = Column(Float, nullable=False)
    alert = Column(Boolean, default=False)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
