from sqlalchemy import Column, Integer, String, Float, TIMESTAMP, func, ForeignKey
from app.db.session import Base

class Device(Base):
    __tablename__ = "Device"
    id = Column(Integer, primary_key=True, index=True)
    feed_id = Column(String(255), unique=True, nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    update_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
