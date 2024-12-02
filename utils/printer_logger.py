"""打印机日志记录工具"""
import logging
from datetime import datetime

# 配置日志记录器
logger = logging.getLogger('printer')
logger.setLevel(logging.DEBUG)

# 创建控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 创建文件处理器
file_handler = logging.FileHandler('printer.log')
file_handler.setLevel(logging.INFO)

# 设置日志格式
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

# 添加处理器到日志记录器
logger.addHandler(console_handler)
logger.addHandler(file_handler)

def log_printer_error(error_type, details):
    """记录打印机错误"""
    logger.error(f"打印机错误 - {error_type}: {details}")

def log_printer_info(message):
    """记录打印机信息"""
    logger.info(message)

def log_printer_debug(message):
    """记录打印机调试信息"""
    logger.debug(message)