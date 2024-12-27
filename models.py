#create a Database Model
from fastapi import FastAPI, Path
from pydantic import BaseModel
from sqlalchemy import create_engine, Column,Integer, String, Date
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.ext.declarative import declarative_base
#from sqlalchemy.dialects.sqlite import *

app= FastAPI()

DATABASE_URL = "sqlite:///./test.db"

connect_args = {"check_same_thread": False}
engine = create_engine(DATABASE_URL, connect_args=connect_args)

session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    date_of_birth = Column(Date)
    phone = Column(String)
    email = Column(String, nullable=True)
    address = Column(String)
    emergency_contact = Column(String, nullable=True)
