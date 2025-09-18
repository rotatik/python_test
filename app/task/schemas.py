from pydantic import BaseModel
from datetime import datetime

class STask(BaseModel):
    id : int
    user_id: int
    description: str
    completed: bool
    created_at : datetime

    class Config:
        orm_mode = True
