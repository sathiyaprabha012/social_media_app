from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL )

SessionLocal = sessionmaker(autocommit = False , autoflush = False , bind = engine)

Base = declarative_base()


def get_db() :
    db = SessionLocal()
    try :
        yield db
    finally : 
        db.close()




# When connecting with the Postgres using driver
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from datetime import time
# while True :
#     try :
#         conn = psycopg2.connect(host = "localhost", database = "fastapi" , user="postgres" , password = "Vinayagarrr@7" , cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Postgres Connected successfully!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error" , error)
#         time.sleep(4)


