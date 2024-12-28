# SQLAlchemy models

from sqlalchemy import Column, Integer, String, ForeignKey,Text, Date, DateTime
from sqlalchemy.orm import relationship
from app.database import Base


class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    gender = Column(String)
    date_of_birth = Column(Date)
    phone = Column(String)
    email = Column(String, nullable=True)
    address = Column(String)
    emergency_contact = Column(String, nullable=True)

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    specialization = Column(String)

class Appointment(Base):
    __tablename__ = "appointments"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    date = Column(DateTime)
    reason = Column(String)
    doctor = Column(String)
    status = Column(String, default="Scheduled")


class MedicalRecord(Base):
    __tablename__ = "medical_records"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"))
    diagnosis = Column(Text)
    prescriptions = Column(Text)
    allergies = Column(Text, nullable=True)
    lab_results = Column(Text, nullable=True)
    created_at = Column(DateTime, default=DateTime.utcnow)
    updated_at = Column(DateTime, default=DateTime.utcnow, onupdate=DateTime.utcnow)

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    password = Column(String)  # Store hashed passwords
    role = Column(String)
    created_at = Column(DateTime, default=DateTime.utcnow)



    patient = relationship("Patient")
    doctor = relationship("Doctor")
