"""打印机相关路由处理"""
from flask import Blueprint, request
from printer_manager import PrinterManager
from utils.response_utils import success_response, error_response
from utils.time_utils import get_timestamp

printer_bp = Blueprint('printer', __name__)
printer_manager = PrinterManager()


@printer_bp.route('/api/print', methods=['POST'])
def print_message():
    """处理打印消息请求"""
    data = request.json
    message = data.get('message')
    print_type = data.get('type', 'text')

    if not message:
        return error_response('No message provided')

    if not printer_manager.is_connected():
        return error_response('Printer not connected', 503)

    timestamp = get_timestamp()

    success = False
    if print_type == 'text':
        formatted_message = f"[{timestamp}] {message}"
        success = printer_manager.print_text(formatted_message)
    elif print_type == 'barcode':
        success = printer_manager.print_barcode(message)
    elif print_type == 'qr':
        success = printer_manager.print_qr(message)
    elif print_type == 'image':
        success = printer_manager.print_image(message)
    else:
        return error_response('Invalid print type')

    if success:
        return success_response({
            'message': message,
            'timestamp': timestamp,
            'type': print_type
        })
    return error_response('Printing failed', 500)


@printer_bp.route('/api/printer/connect', methods=['POST'])
def connect_printer():
    """处理打印机连接请求"""
    data = request.json
    ip = data.get('ip')
    port = data.get('port')

    if not ip or not port:
        return error_response('IP and port are required')

    try:
        port = int(port)
    except ValueError:
        return error_response('Port must be a number')

    success = printer_manager.connect(ip, port)
    return success_response() if success else error_response('Failed to connect to printer', 500)