from sqlalchemy import create_engine

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from functools import wraps
from configparser import ConfigParser
from utils.log_config import LogConfig
import os

logger = LogConfig.setup_logger("dao")

class DBConnection:
    _instance = None
    _engine = None
    _SessionFactory = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DBConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        config = ConfigParser()
        config_path = os.path.join("conf", "conf.ini")
        config.read(config_path)
        db_url = config.get("database", "db_url")
        
        if not self._engine:
            self._engine = create_engine(
                db_url,
                pool_pre_ping=True,
                pool_recycle=3600,
                echo=False
            )
            self._SessionFactory = scoped_session(sessionmaker(bind=self._engine))


def session_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        session = DBConnection()._SessionFactory
        try:
            kwargs['session'] = session
            result = func(*args, **kwargs)
            session.commit()
            return result
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
    return wrapper


