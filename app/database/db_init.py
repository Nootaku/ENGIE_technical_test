from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session(
    db_url: str = "sqlite:///app/database/database.db",
):
    """Create and return a DB session."""
    # Create connection
    # https://docs.sqlalchemy.org/en/14/tutorial/engine.html#tutorial-engine
    if db_url.startswith("sqlite"):
        engine = create_engine(
            db_url,
            connect_args={"check_same_thread": False}
        )

    else:
        engine = create_engine(db_url)

    # The sessionmake object is not a DB session yet. But once created it will
    # be.
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)
