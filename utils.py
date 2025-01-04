from datetime import datetime

def validate_date(date):
    """
    Validate the date format (YYYY-MM-DD).
    """
    try:
        datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False
