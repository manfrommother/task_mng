from fastapi import FastAPI
from app.routes import task_router

app = FastAPI()

app.get('/')
def read_root():
    return {'message': 'Welcome to Task Manager API'}

app.include_router(task_router)