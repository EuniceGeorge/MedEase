# Script to initialize the database

from app.database import Base, engine

def init_db():
    print("Defining Base...")
    Base.metadata.create_all(bind=engine)
    print("Tables created.")


if __name__ == "__main__":
    init_db()
