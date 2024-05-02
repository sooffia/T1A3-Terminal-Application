
class InvalidTimeError(Exception):
    """An error raised when the end time is earlier than or equal to the start time."""
    def __init__(self):
        super().__init__(
            "End time must be later than start time."
        )
