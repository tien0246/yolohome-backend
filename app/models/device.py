from sqlalchemy import Column, String, Float, TIMESTAMP, func, ForeignKey
from app.db.session import Base
import uuid

class Device(Base):
    __tablename__ = "Device"
    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4)
    feed_id = Column(String(255), unique=True, nullable=False, index=True)
    user_id = Column(String(36), ForeignKey("User.id"), nullable=True)
    name = Column(String(255), nullable=False)
    type = Column(String(255), nullable=False)
    location = Column(String(255), nullable=False)
    min_value = Column(Float, nullable=False)
    max_value = Column(Float, nullable=False)
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    update_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __init__(self, feed_id, user_id, name, type, location, min_value, max_value):
        self.feed_id = feed_id
        self.user_id = user_id
        self.name = name
        self.type = type
        self.location = location
        self.min_value = min_value
        self.max_value = max_value
