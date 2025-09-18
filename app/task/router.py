from fastapi import APIRouter
from app.task.dao import TaskDao
from app.task.schemas import STask


router = APIRouter(
    prefix="/tasks",
    tags=["Бронирования"]
)

@router.get("")
async def get_tasks() -> list[STask]:
    return await TaskDao.find_all()

