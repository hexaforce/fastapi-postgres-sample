from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import settings

# MAIN DB
engine_main = create_engine(settings.DATABASE_URI[0], pool_pre_ping=True, echo=True)
session_main = sessionmaker(autocommit=False, autoflush=False, bind=engine_main)

# TEST DB
engine_test = create_engine(settings.DATABASE_URI[1], pool_pre_ping=True, echo=True)
session_test = sessionmaker(autocommit=False, autoflush=False, bind=engine_test)
