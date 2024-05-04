
class InvalidTimeError(Exception):
    """An error raised when the end time is earlier than or equal to the start time."""
    def __init__(self):
        super().__init__("End time must be later than start time.")
                 
class SameDayOverlapError(Exception):
    """An error raised when a new class overlaps with another class on the same day."""
    def __init__(self, message="Class overlaps with another class on the same day."):
        self.message = message
        super().__init__(self.message)

class EmptyInputError(Exception):
    """An error raised when the user provides empty input for required fields."""
    def __init__(self):
        super().__init__("Please enter a value for this field.")


class ScheduleNotFoundError(Exception):
    """An error raised when the application cannot find the schedule file or encounters issues while reading or writing to it."""
    def __init__(self):
        super().__init__("Schedule file not found or inaccessible.")

class InvalidDayError(Exception):
    """An error raised when an invalid day name is entered."""
    def __init__(self):
        super().__init__("Invalid day name. Please enter a valid day.")