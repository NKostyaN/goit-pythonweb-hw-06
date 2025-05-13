from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


# DATABASE_URL = "postgresql+psycopg2://postgres:supersecret@localhost:5432/postgres"
# DATABASE_URL = "postgresql+psycopg2://postgres:qwerty@localhost:5432/postgres"


engine = create_engine("postgresql+psycopg2://postgres:qwerty@localhost:5432/postgres")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# db = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
