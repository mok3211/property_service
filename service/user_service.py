from dao.user_dao import UserDAO
from utils.log_config import LogConfig

logger = LogConfig.setup_logger('service')

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, user_data):
        try:
            logger.info(f"Creating new user with data: {user_data}")
            # 直接调用 DAO 方法，不需要关心 session 的处理
            user = self.user_dao.insert_user(user_data)
            logger.info(f"User created successfully with id: {user.id}")
            return user
        except Exception as e:
            logger.error(f"Failed to create user: {str(e)}")


    def get_user(self, user_id):
        try:
            logger.info(f"Getting user with id: {user_id}")
            return self.user_dao.get_user_by_id(user_id)
        except Exception as e:
            logger.error(f"Failed to get user: {str(e)}")