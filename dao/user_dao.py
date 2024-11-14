from dao.db_conn import session_decorator
from utils.log_config import LogConfig
from models.User import User

logger = LogConfig.setup_logger('dao')

class UserDAO:
    @session_decorator
    def insert_user(self, user_data, **kwargs) -> User:
        try:
            logger.info(f"Inserting user into database: {user_data}")
            # 使用 session 进行数据库操作
            new_user = User(**user_data)
            kwargs.get("session").add(new_user)
            # 不需要手动 commit，装饰器会处理
            logger.info("User inserted successfully")
            return new_user
        except Exception as e:
            logger.error(f"Database error while inserting user: {str(e)}")
        return None

    @session_decorator
    def get_user_by_id(self, user_id, **kwargs) -> User:
        try:
            logger.info(f"Querying user with id: {user_id}")
            user = kwargs.get("session").query(User).filter(User.id == user_id).first()
            return user
        except Exception as e:
            logger.error(f"Error fetching user: {str(e)}")
        return None
    
    @session_decorator
    def get_user_by_name(self, user_name, **kwargs) -> User:
        try:
            logger.info(f"Querying user with name error: {user_name}")
            user = kwargs.get("session").query(User).filter(User.username == user_name).first()
            return user
        except Exception as e:
            logger.error(f"Error fetching user: {str(e)}")
        return None
    
    @session_decorator
    def get_user_by_email(self, user_email, **kwargs) -> User:
        try:
            logger.info(f"Querying user with name error: {user_email}")
            user = kwargs.get("session").query(User).filter(User.email== user_email).first()
            return user
        except Exception as e:
            logger.error(f"Error fetching user: {str(e)}")
        return None
    

    @session_decorator
    def update_user(self, user_id, update_data, **kwargs) -> User:
        try:
            logger.info(f"Updating user {user_id} with data: {update_data}")
            user = kwargs.get("session").query(User).filter(User.id == user_id).first()
            if user:
                for key, value in update_data.items():
                    setattr(user, key, value)
            return user
        except Exception as e:
            logger.error(f"Error updating user: {str(e)}")
        return None