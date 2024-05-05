
class InvalidTimeError(Exception):
    """An error raised when an invalid time is entered."""
    def __init__(self, message):
        super().__init__(message) 

class EmptyInputError(Exception):
    """An error raised when the user provides empty input for required fields."""
    def __init__(self):
        super().__init__("Please enter a value for this field.")

class InvalidClassSelectionError(Exception):
    """An error raised when an invalid class number is selected."""
    def __init__(self):
        super().__init__("Invalid class selection. Please enter a valid class number.")

class InvalidScheduleFormatError(Exception):
    """Custom exception raised when the format of the schedule data is invalid."""
    def __init__(self, message="Invalid schedule format."):
        self.message = message
        super().__init__(self.message) 
                 
# class SameDayOverlapError(Exception):
#     """An error raised when a new class overlaps with another class on the same day."""
#     def __init__(self, message="Class overlaps with another class on the same day."):
#         self.message = message
#         super().__init__(self.message)

# class InvalidDayError(Exception):
#     """An error raised when an invalid day name is entered."""
#     def __init__(self):
#         super().__init__("Invalid day name. Please enter a valid day.")