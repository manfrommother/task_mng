from fastapi import FastAPI
from app.routes import tack_router

app = FastAPI()

app.get('/')
def read_root():
    return {'message': 'Welcome to Task Manager API'}

app.include_router(tack_router)