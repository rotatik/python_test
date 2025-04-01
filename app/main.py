from fastapi import FastAPI
from datetime import date
from pydantic import BaseModel

app = FastAPI()

@app.get('/challanges')
def challang(message: str, type: str = None, day: int = None, hours = None):
    return {'message': message}

class ToDoItem(BaseModel):
    challange: str
    day: date
    type: str

@app.post('/to_do')
def todo(item: ToDoItem):
    return {'message': 'ToDo item created successfully', 'item': item}
