from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel
from app.task.router import router as router_task

app = FastAPI()

app.include_router(router_task)


    
