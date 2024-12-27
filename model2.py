from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://MedEase_user:medease@localhost/MedEase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

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
