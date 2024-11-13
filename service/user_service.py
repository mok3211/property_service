from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from dao.user_dao import UserDAO
from models.User import User
from utils.log_config import LogConfig

logger = LogConfig.setup_logger('service')

class UserService:
    def __init__(self):
        self.user_dao = UserDAO()

    def create_user(self, user_data) -> User:
        try:
            logger.info(f"Creating new user with data: {user_data}")
            # 直接调用 DAO 方法，不需要关心 session 的处理
            user = self.user_dao.insert_user(user_data)
            logger.info(f"User created successfully with id: {user.id}")
            return user
        except Exception as e:
            logger.error(f"Failed to create user: {str(e)}")
            return None

    def get_user(self, user_id) -> User:
        try:
            logger.info(f"Getting user with id: {user_id}")
            return self.user_dao.get_user_by_id(user_id)
        except Exception as e:
            logger.error(f"Failed to get user: {str(e)}")
            return None
    
    def get_user_by_name(self, user_name) -> User:
        try:
            return self.user_dao.get_user_by_name(user_name)
        except Exception as e:
            logger.error(f"Failed to get user: {str(e)}")
            return None
        
    def get_user_by_email(self, email) -> User:
        try:
            return self.user_dao.get_user_by_name(email)
        except Exception as e:
            logger.error(f"Failed to get user: {str(e)}")
        return None
    
    def authenticate_user(self, user_name: str, password: str) -> User:
        user = self.get_user_by_name(user_name)
        try:
            if not user:
                return False
            if not User.verify_password(password, user._password):
                return False
        except Exception as e:
            return False
        return user
    
    def send_password_reset_email(self, user):
        # 生成重置密码的链接
        reset_token = self.create_reset_token(user)
        reset_link = f"http://yourapp.com/reset_password?token={reset_token}"

        # 发送电子邮件
        subject = "Reset Your Password"
        body = f"Click the link to reset your password: {reset_link}"
        self.send_email(user.email, subject, body)
    
    def send_email(self, to_email, subject, body):
        # 设置SMTP服务器和端口
        smtp_server = "smtp.your-email-provider.com"
        smtp_port = 587
        sender_email = "your-email@example.com"
        sender_password = "your-email-password"

        # 创建邮件内容
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        try:
            # 连接到SMTP服务器并发送邮件
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  # 启用TLS加密
                server.login(sender_email, sender_password)
                server.send_message(msg)
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")
            