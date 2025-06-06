from sqlalchemy import Column, String, TIMESTAMP, func
from app.db.session import Base
import uuid

class User(Base):
    __tablename__ = "User"
    id = Column(String(36), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    expo_token = Column(String(255), nullable=True)
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    update_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
