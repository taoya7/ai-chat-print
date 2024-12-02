"""打印机管理器核心类"""
from escpos.printer import Network
import base64
from PIL import Image
import io
from config import Config

class PrinterManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(PrinterManager, cls).__new__(cls)
            cls._instance.printer = None
        return cls._instance

    def connect(self, ip, port):
        """连接网络打印机"""
        try:
            self.printer = Network(ip, port)
            # 初始化打印机
            self.printer._raw(b'\x1B\x40')
            return True
        except Exception as e:
            print(f"打印机连接错误: {str(e)}")
            return False

    def print_text(self, text):
        """打印文本"""
        if not self.printer:
            return False

        try:
            self.printer._raw(text.encode('gb2312'))
            self.printer.text('\n\n\n')
            return True
        except Exception as e:
            print(f"打印错误: {str(e)}")
            return False

    def print_barcode(self, data, barcode_type="CODE128"):
        """打印条形码"""
        if not self.printer:
            return False
        try:
            self.printer.set(align='center')

            # 处理特殊字符
            formatted_data = "{B" + data  # 添加 CODE128 B 模式前缀
            # 打印条形码
            self.printer.barcode(formatted_data, barcode_type)
            return True
        except Exception as e:
            print(f"条形码打印错误: {str(e)}")
            return False

    def print_qr(self, data):
        """打印二维码"""
        if not self.printer:
            return False
        try:
            self.printer.set(align='center')
            self.printer.qr(data, size=8)
            return True
        except Exception as e:
            print(f"二维码打印错误: {str(e)}")
            return False

    def print_image(self, image_data):
        """打印图片"""
        if not self.printer:
            return False

        try:
            # 解码base64图片数据
            image_binary = base64.b64decode(image_data.split(',')[1])
            image = Image.open(io.BytesIO(image_binary))

            # 调整图片大小以适应打印机
            max_width = 512
            ratio = max_width / image.width
            new_size = (max_width, int(image.height * ratio))
            image = image.resize(new_size)

            self.printer.set(align='center')
            self.printer.image(image)
            self.printer.text("\n\n")
            self.printer.set(align='left')
            self.printer.cut()
            return True
        except Exception as e:
            print(f"图片打印错误: {str(e)}")
            return False

    def is_connected(self):
        """检查打印机连接状态"""
        return self.printer is not None