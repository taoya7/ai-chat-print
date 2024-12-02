from datetime import datetime

def get_timestamp():
    """Generate a formatted timestamp string."""
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')