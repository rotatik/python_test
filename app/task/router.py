from fastapi import APIRouter
from sqlalchemy import select
from app.database import async_session_maker

from app.task.models import Task
router = APIRouter(
    prefix="/tasks",
    tags=["Бронирования"]
)

@router.get("")
async def get_tasks():
    async with async_session_maker() as session:
        query = select(Task)
        result = await session.execute(query)
        return (result.scalars().all())
