from sqlalchemy import Column, String, TIMESTAMP, func, ForeignKey
from app.db.session import Base

class UserLog(Base):
    __tablename__ = "User_Log"
    id = Column(String(36), primary_key=True, index=True)
    user_id = Column(String(36), ForeignKey("User.id"), nullable=False)
    device_id = Column(String(36), ForeignKey("Device.id"), nullable=False)
    action = Column(String(255), nullable=False)
    timestamp = Column(TIMESTAMP, server_default=func.current_timestamp())
