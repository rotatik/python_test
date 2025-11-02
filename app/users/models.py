from sqlalchemy import Column, String,Boolean,Integer,DateTime, PrimaryKeyConstraint
from datetime import datetime
from app.database import Base

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    email = Column(String, nullable=False)
    password = Column(String, nullable=False)



