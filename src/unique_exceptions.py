
class InvalidTimeError(Exception):
    """An error raised when the end time is earlier than or equal to the start time."""
    def __init__(self):
        super().__init__(
            "End time must be later than start time."
        )
class NumberInputError(Exception):
    """An error raised when symbols and alphabet characters are detected in an integer input prompt."""
    def __init__(self):
        super().__init__(
            "You have entered an invalid character. Please enter a number." 
        )