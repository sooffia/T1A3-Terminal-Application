### MAIN SECTION ###    
from title import main_logo
from simple_term_menu import TerminalMenu
from clear import clear 

print(main_logo)

def main_greeting():
  print("Welcome to Your Personal Class Schedule Manager")
main_greeting()

# Function to display a single class entry
def main():
    options = ["Enter Classes",
               "Update Classes",
               "Delete Classes",
               "View Timetable"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index is not None:
        print(f"You have selected {options[menu_entry_index]}!")
    else:
        print("No option selected.")
main()

# Allows users to navigate back to the main menu
def navigate_to_menu():
    while True:
        try:
            navigate = input("To go back to the main menu, press '#':  ").lower()
            if navigate == '#':
                clear()
                return
            else:
                raise ValueError("\nInvalid Input! Please type '#'.\n")
        except ValueError as InvalidInput:
            print(InvalidInput)

# Main function to log classes
navigate_to_menu()
