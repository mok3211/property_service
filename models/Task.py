from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()
class Task(Base):
    __tablename__ = 'tbl_user_tasks'
    id = Column(Integer, primary_key=True, autoincrement=True)
    task_name = Column(String(100), nullable=False, index=True)
    task_description = Column(String(120), unique=True, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    progress = Column(float, default=0.0)
    status = Column(String(30), default="pending")
    
    
    
    
    