"""打印机管理器核心类"""
from escpos.printer import Network
import codecs
from utils.printer_commands import *
from utils.printer_logger import log_printer_error, log_printer_info, log_printer_debug

class PrinterManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrinterManager, cls).__new__(cls)
            cls._instance.printer = None
        return cls._instance

    def connect(self, ip, port):
        """连接网络打印机并初始化设置"""
        try:
            log_printer_info(f"正在连接打印机 {ip}:{port}")
            self.printer = Network(ip, port)
            self._initialize_printer()
            log_printer_info("打印机连接成功")
            return True
        except Exception as e:
            log_printer_error("连接错误", str(e))
            return False

    def _initialize_printer(self):
        """初始化打印机设置"""
        if not self.printer:
            return

        try:
            # 初始化打印机
            self.printer._raw(INIT_PRINTER)

            # 设置打印浓度（深度）
            self.printer._raw(get_density_command(3))

            # 设置中文模式
            self._set_chinese_mode()

            # 设置字符间距
            self.printer._raw(CHAR_SPACING)

            log_printer_info("打印机初始化完成")
        except Exception as e:
            log_printer_error("初始化错误", str(e))
            raise

    def _set_chinese_mode(self):
        """设置中文打印模式"""
        if not self.printer:
            return
        try:
            self.printer._raw(CHINESE_MODE['ENABLE'])
            self.printer._raw(CHINESE_MODE['SELECT'])
            log_printer_debug("中文模式设置成功")
        except Exception as e:
            log_printer_error("中文模式设置错误", str(e))
            raise

    def print_text(self, text):
        """打印文本内容"""
        if not self.printer:
            log_printer_error("打印错误", "打印机未连接")
            return False

        try:
            # 重置打印机状态
            self.printer._raw(INIT_PRINTER)

            # 设置加粗模式
            self.printer._raw(FONT_COMMANDS['BOLD_ON'])

            # 打印内容
            self.printer._raw(text.encode('gb2312'))
            self.printer._raw("\n\n\n".encode('gb2312'))
            self.printer._raw(LINE_FEED)

            # 关闭加粗模式
            self.printer._raw(FONT_COMMANDS['BOLD_OFF'])

            log_printer_info(f"成功打印内容: {text[:50]}...")
            return True

        except Exception as e:
            log_printer_error("打印错误", str(e))
            return False

    def is_connected(self):
        """检查打印机连接状态"""
        return self.printer is not None