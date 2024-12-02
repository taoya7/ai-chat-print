"""应用配置"""
from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    """应用配置类"""
    SECRET_KEY = os.getenv('SECRET_KEY', 'your-secret-key-here')
    PRINTER_IP = os.getenv('PRINTER_IP', '192.168.1.200')
    PRINTER_PORT = int(os.getenv('PRINTER_PORT', '9100'))

    # 打印机配置
    PRINTER_DENSITY = 3  # 1=轻度, 2=中等, 3=深度
    PRINTER_ENCODING = 'gb18030'
    PRINTER_DEFAULT_FONT = 'a'