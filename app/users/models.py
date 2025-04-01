from sqlalchemy import Column, String, PrimaryKeyConstraint

from app.database import Base

class user(Base):
    __tablename__ = "users"
    id = Column(String,primary_key= True,nullable=False)
    name = Column(String,nullable = False)


