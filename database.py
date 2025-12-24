from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://todoapplicationdatabase_hdqe_user:MVh2f40VCJkkxVigjnCTCrDy1ZF82gLO@dpg-d55s4663jp1c73a2bdq0-a/todoapplicationdatabase_hdqe"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



