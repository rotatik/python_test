from fastapi import FastAPI
from app.task.router import router as router_task
from app.users.router import router as router_user
app = FastAPI()


app.include_router(router_user)
app.include_router(router_task)


    
