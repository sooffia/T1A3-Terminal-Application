
class InvalidTimeError(Exception):
    """An error raised when the end time is earlier than or equal to the start time."""
    def __init__(self):
        super().__init__(
            "End time must be later than start time."
        )
class EmptyInputError(Exception):
    """An error raised when the user provides empty input for required fields."""
    def __init__(self):
        super().__init__("Please enter a value for this field.")

class InvalidRoomError(Exception):
    """An error raised when the room number input is not within a valid range or format."""
    def __init__(self):
        super().__init__("Invalid room number. Please enter a valid room number.")

class DuplicateClassError(Exception):
    """An error raised when the user tries to add a class with the same name and time as an existing class."""
    def __init__(self):
        super().__init__("A class with the same name and time already exists.")

class ScheduleNotFoundError(Exception):
    """An error raised when the application cannot find the schedule file or encounters issues while reading or writing to it."""
    def __init__(self):
        super().__init__("Schedule file not found or inaccessible.")

class InvalidDayError(Exception):
    """An error raised when an invalid day name is entered."""
    def __init__(self):
        super().__init__("Invalid day name. Please enter a valid day.")