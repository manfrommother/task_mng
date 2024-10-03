from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Task
from .database import SessionLocal, init_db

task_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.clouse()

#CRUD операции

def create_task(title: str, description: str, db: Session=Depends(get_db)):
    task = Task(title=title, description=description)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

@task_router.get('/tasks/'):
def read_tasks(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

#DOTO Дописать CRUD