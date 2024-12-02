"""打印机指令常量和命令生成工具"""

# 基础打印机指令
INIT_PRINTER = b'\x1B\x40'  # 初始化打印机
LINE_FEED = b'\x0A'  # 换行
PAPER_CUT = b'\x1D\x56\x41\x00'  # 切纸
CHAR_SPACING = b'\x1B\x20\x00'  # 字符间距

# 中文相关指令
CHINESE_MODE = {
    'ENABLE': b'\x1C\x26',  # 启用中文模式
    'SELECT': b'\x1C\x43\x01',  # 选择中文模式
    'CANCEL': b'\x1C\x2E'  # 取消中文模式
}

# 打印浓度和速度控制
PRINT_DENSITY = {
    'LIGHT': b'\x1B\x37\x07\x07',  # 轻度打印浓度
    'MEDIUM': b'\x1B\x37\x0A\x0A',  # 中等打印浓度
    'DARK': b'\x1B\x37\x0F\x0F'  # 深度打印浓度
}

# 字体和样式
FONT_COMMANDS = {
    'DEFAULT': b'\x1B\x4D\x00',  # 默认字体
    'BOLD_ON': b'\x1B\x45\x01',  # 加粗开启
    'BOLD_OFF': b'\x1B\x45\x00'  # 加粗关闭
}

def get_density_command(level=3):
    """
    生成打印浓度命令
    level: 1-3 (轻、中、重)
    """
    if level == 1:
        return PRINT_DENSITY['LIGHT']
    elif level == 2:
        return PRINT_DENSITY['MEDIUM']
    else:
        return PRINT_DENSITY['DARK']