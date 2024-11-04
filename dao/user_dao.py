from dao.db_conn import DBConnection, session_decorator
from utils.log_config import LogConfig

logger = LogConfig.setup_logger('dao')

class UserDAO:
    @session_decorator
    def insert_user(self, session, user_data):  # 注意这里需要添加 session 参数
        try:
            logger.info(f"Inserting user into database: {user_data}")
            # 使用 session 进行数据库操作
            new_user = User(**user_data)
            session.add(new_user)
            # 不需要手动 commit，装饰器会处理
            logger.info("User inserted successfully")
            return new_user
        except Exception as e:
            logger.error(f"Database error while inserting user: {str(e)}")
            raise

    @session_decorator
    def get_user_by_id(self, session, user_id):
        try:
            logger.info(f"Querying user with id: {user_id}")
            user = session.query(User).filter(User.id == user_id).first()
            return user
        except Exception as e:
            logger.error(f"Error fetching user: {str(e)}")
            raise

    @session_decorator
    def update_user(self, session, user_id, update_data):
        try:
            logger.info(f"Updating user {user_id} with data: {update_data}")
            user = session.query(User).filter(User.id == user_id).first()
            if user:
                for key, value in update_data.items():
                    setattr(user, key, value)
                # 不需要手动 commit，装饰器会处理
                return user
            return None
        except Exception as e:
            logger.error(f"Error updating user: {str(e)}")
            raise