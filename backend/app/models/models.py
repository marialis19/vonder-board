from sqlalchemy import Column, String, Boolean, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
from uuid import uuid4
from datetime import datetime

from app.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    email = Column(String, unique=True, nullable=False)
    username = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    projects = relationship("Project", back_populates="owner")
    tasks = relationship("Task", back_populates="assigned_user")


class Project(Base):
    __tablename__ = "projects"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    name = Column(String, nullable=False)
    description = Column(Text)
    status = Column(String, default="planning")
    created_at = Column(DateTime, default=datetime.utcnow)
    owner_id = Column(String, ForeignKey("users.id"))

    owner = relationship("User", back_populates="projects")
    tasks = relationship("Task", back_populates="project")


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, default=lambda: str(uuid4()))
    title = Column(String, nullable=False)
    description = Column(Text)
    priority = Column(String, default="medium")
    status = Column(String, default="todo")
    created_at = Column(DateTime, default=datetime.utcnow)
    project_id = Column(String, ForeignKey("projects.id"))
    assigned_user_id = Column(String, ForeignKey("users.id"))

    project = relationship("Project", back_populates="tasks")
    assigned_user = relationship("User", back_populates="tasks")