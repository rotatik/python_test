from app.task.models import Task
from app.dao.base import BaseDao

class TaskDao(BaseDao):
    model = Task
