from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create the URL for SQLAlchemy
# Will create a file named 'sql_app.db' in current directory
# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
SQLALCHEMY_DATABASE_URL = "sqlite:////home/nootaku/dev/engie_2/app/database/database.db"

# Establishing connection
# https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
# note: the 'check_same_thread' is only required for SQLite, not for other DBs
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)

# SessionLocal is not a DB session yet, however the instance of SessionLocal
# will be our DB session once created.
# The name SessionLocal is used to distinguish from Session (from SQLAlchemy)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
