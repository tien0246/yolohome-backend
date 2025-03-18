from sqlalchemy import Column, String, TIMESTAMP, func
from app.db.session import Base

class User(Base):
    __tablename__ = "User"
    id = Column(String(36), primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    update_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
