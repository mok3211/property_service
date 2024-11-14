from sqlalchemy import Column, Integer, String, DateTime, Boolean, Enum
from sqlalchemy.ext.declarative import declarative_base
import datetime
import enum
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

Base = declarative_base()

class UserStatus(enum.Enum):
    INACTIVE = "inactive"
    SUSPENDED = "suspended"

class User(Base):
    """用户模型类
    
    属性:
        id: 用户唯一标识
        username: 用户名
        email: 电子邮件
        _password: 加密后的密码
        phone: 手机号
        status: 用户状态
        last_login: 最后登录时间
        login_attempts: 登录尝试次数
        is_admin: 是否为管理员
        created_at: 创建时间
        updated_at: 更新时间
    """
    
    __tablename__ = 'tbl_user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False, index=True)
    email = Column(String(120), unique=True, nullable=False, index=True)
    _password = Column('password_hash', String(128), nullable=False)
    phone = Column(String(20), unique=True, nullable=True)
    status = Column("is_active", Boolean, default=True, nullable=False)
    last_login = Column(DateTime, nullable=True)
    login_attempts = Column(Integer, default=0)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    updated_at = Column(DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, username, email, password, phone=None, is_admin=False):
        self.username = username
        self.email = email
        self.password = password  # 这里会调用 password.setter
        self.phone = phone
        self.is_admin = is_admin

    @property
    def password(self):
        """获取密码时抛出异常，防止直接访问密码"""
        raise AttributeError('密码不可读')

    @password.setter
    def password(self, password):
        """设置密码，自动进行加密"""
        self._password = pwd_context.hash(password)

    def verify_password(self, password):
        """验证密码
        
        Args:
            password: 待验证的密码

        Returns:
            bool: 密码是否正确
        """
        return pwd_context.verify(self._password, password)

    def update_login_info(self, success=True):
        """更新登录信息
        
        Args:
            success: 登录是否成功
        """
        if success:
            self.last_login = datetime.datetime.now()
            self.login_attempts = 0
        else:
            self.login_attempts += 1

    def to_dict(self, exclude_fields=None):
        """转换为字典格式
        
        Args:
            exclude_fields: 需要排除的字段列表

        Returns:
            dict: 用户信息字典
        """
        if exclude_fields is None:
            exclude_fields = ['_password']
        else:
            exclude_fields.append('_password')

        data = {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'phone': self.phone,
            'status': self.status,
            'last_login': self.last_login.isoformat() if self.last_login else None,
            'login_attempts': self.login_attempts,
            'is_admin': self.is_admin,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }
        
        return {k: v for k, v in data.items() if k not in exclude_fields}

    def __repr__(self):
        """返回用户的字符串表示"""
        return f"<User {self.username}>"

    def __str__(self):
        """返回用户的可读字符串表示"""
        return f"User(username={self.username}, email={self.email})"