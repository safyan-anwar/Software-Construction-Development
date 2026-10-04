MIN_MARK = 0
MAX_MARK = 100
INVALID_MARK_MESSAGE = "Invalid marks. Enter 0-100."
def validate_mark(mark):
    """Return True if the mark is between 0 and 100 (inclusive)."""
    return MIN_MARK <= mark <= MAX_MARK