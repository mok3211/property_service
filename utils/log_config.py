import os
import time
import logging
from logging.handlers import RotatingFileHandler

class LogConfig:
    # 日志级别映射
    LEVEL_MAPPING = {
        'DEBUG': logging.DEBUG,
        'INFO': logging.INFO,
        'WARNING': logging.WARNING,
        'ERROR': logging.ERROR,
        'CRITICAL': logging.CRITICAL
    }
    
    # 200MB in bytes
    MAX_BYTES = 200 * 1024 * 1024
    # 保留的备份文件数量
    BACKUP_COUNT = 5

    @staticmethod
    def setup_logger(module_name, level='INFO'):
        """
        设置logger
        :param module_name: 模块名称 (如 'service', 'dao')
        :param level: 日志级别
        :return: logger实例
        """
        # 创建logs目录
        log_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'logs')
        if not os.path.exists(log_dir):
            os.makedirs(log_dir)
        
        # 生成日志文件名 (模块名_年月日.log)
        current_date = time.strftime('%Y%m%d')
        log_file = os.path.join(log_dir, f'{module_name}_{current_date}.log')
        
        # 创建logger
        logger = logging.getLogger(module_name)
        if logger.handlers:  # 避免重复添加handler
            return logger
            
        logger.setLevel(LogConfig.LEVEL_MAPPING.get(level.upper(), logging.INFO))
        
        # 创建RotatingFileHandler
        file_handler = RotatingFileHandler(
            filename=log_file,
            maxBytes=LogConfig.MAX_BYTES,
            backupCount=LogConfig.BACKUP_COUNT,
            encoding='utf-8'
        )
        
        # 设置日志格式
        formatter = logging.Formatter(
            '[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
        )
        file_handler.setFormatter(formatter)
        
        # 添加handler
        logger.addHandler(file_handler)
        
        return logger