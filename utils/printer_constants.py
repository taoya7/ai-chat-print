"""Constants for printer configuration and commands."""

# Character encodings
ENCODING_GB2312 = 'gb2312'
ENCODING_GB18030 = 'gb18030'
ENCODING_UTF8 = 'utf-8'

# Printer commands (in hex)
CMD_ENABLE_CHINESE = b'\x1C\x26'  # FS &
CMD_SELECT_CHINESE = b'\x1C\x43\x01'  # FS C 1
CMD_DENSITY = b'\x1B\x37\x07\x07'  # ESC 7 n1 n2

# Printer settings
DEFAULT_FONT = 'a'
DEFAULT_WIDTH = 1
DEFAULT_HEIGHT = 1
DEFAULT_ALIGN = 'left'

# Error messages
ERR_NOT_CONNECTED = 'Printer not connected'
ERR_PRINTING_FAILED = 'Printing failed'
ERR_CONNECTION_FAILED = 'Failed to connect to printer'
ERR_INVALID_PORT = 'Port must be a number'
ERR_MISSING_PARAMS = 'IP and port are required'