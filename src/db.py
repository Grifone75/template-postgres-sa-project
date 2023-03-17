from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from contextlib import contextmanager


#TODO this is just temporary
engine = create_engine("postgresql://postgres:postgres@localhost:5440/postgres")

@contextmanager
def session_context():
    session_factory = sessionmaker(bind=engine)
    session = scoped_session(session_factory)
    try:
        yield session
        session.commit()
    except:
        session.rollback()
    finally:
        session.close()
