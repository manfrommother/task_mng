from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .models import Task
from .database import SessionLocal
from app.schemas import TaskCreate

task_router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@task_router.get('/')
def read_root():
    return {'message': 'Welcome to Task Manager API'}
#CRUD операции


@task_router.post('/tasks/')
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

@task_router.get('/tasks/')
def read_tasks(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    tasks = db.query(Task).offset(skip).limit(limit).all()
    return tasks

@task_router.get('/tasks/{task_id}')
def update_task(task_id: int, title: int, description: str, db: Session=Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    task.title = title
    task.description = description
    db.commit()
    db.refresh(task)
    return task

@task_router.delete('/tasks/{task_id}')
def delete_task(task_id: int, db: Session=Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    db.delete(task)
    db.commit()
    return {'detail' : 'Task delete'}