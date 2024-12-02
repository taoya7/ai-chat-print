from flask import Blueprint, request
from printer_manager import PrinterManager
from utils.response_utils import success_response, error_response
from utils.time_utils import get_timestamp

printer_bp = Blueprint('printer', __name__)
printer_manager = PrinterManager()

@printer_bp.route('/api/print', methods=['POST'])
def print_message():
    """Handle print message requests."""
    data = request.json
    message = data.get('message')
    
    if not message:
        return error_response('No message provided')
    
    timestamp = get_timestamp()
    formatted_message = "[{}] {}".format(timestamp, message)
    
    if printer_manager.is_connected():
        if printer_manager.print_text(formatted_message):
            return success_response({
                'message': message,
                'timestamp': timestamp
            })
        return error_response('Printing failed', 500)
    return error_response('Printer not connected', 503)

@printer_bp.route('/api/printer/connect', methods=['POST'])
def connect_printer():
    """Handle printer connection requests."""
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