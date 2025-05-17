from sqlalchemy import Column, String,Boolean,Integer,DateTime, PrimaryKeyConstraint,ForeignKey
from datetime import datetime
from app.database import Base


class Task(Base):
    __tablename__ = "task"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(ForeignKey("users.id"))
    description = Column(String, nullable=True)
    completed = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.now)





