from sqlalchemy import Column, Integer, String, TIMESTAMP, func
from app.db.session import Base

class User(Base):
    __tablename__ = "User"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    create_at = Column(TIMESTAMP, server_default=func.current_timestamp())
    update_at = Column(TIMESTAMP, server_default=func.current_timestamp(), onupdate=func.current_timestamp())
