from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://ivan:12345@db/taskdb' 

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoFlush=False, bing=engine)

Base = declarative_base()

def init_db():
    Base.metadata.create_all(bind=engine)