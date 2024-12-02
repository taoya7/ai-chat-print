from flask import jsonify

def success_response(data=None):
    """Create a success response."""
    response = {'success': True}
    if data:
        response.update(data)
    return jsonify(response)

def error_response(message, status_code=400):
    """Create an error response."""
    return jsonify({
        'success': False,
        'error': message
    }), status_code