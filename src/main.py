### MAIN SECTION ###    
from title import main_logo
from simple_term_menu import TerminalMenu
from clear import clear 

print(main_logo)

def main_greeting():
    print("Welcome to Your Personal Class Schedule Manager")

def navigate_to_menu():
    while True:
        try:
            navigate = input("To return to the main menu, press '#':  ").lower()
            if navigate == '#':
                clear()
                print("Returning to the main menu...")
                return
            else:
                raise ValueError("\nError! Please type '#'.\n")
        except ValueError as InvalidInput:
            print(InvalidInput)

def class_logger(): 
    clear()
    class_name = input("Enter Class Name: ")
    group_section = input("Enter Group/Section: ")
    year = int(input("Enter Year (YYYY): "))

    num_days = int(input("Enter Number of days per week: "))
    schedule_entries = []
    for i in range(num_days):
        day = input(f"Enter Day {i+1} (e.g., Monday): ")
        start_time = input(f"Enter Start Time {i+1} (HH:MM): ")
        end_time = input(f"Enter End Time {i+1} (HH:MM): ")
        class_room = input(f"Enter Class Room {i+1}: ")
        teacher_name = input(f"Enter Teacher's Name {i+1}: ")
        schedule_entries.append({"day": day, "start_time": start_time, "end_time": end_time, "class_room": class_room, "teacher_name": teacher_name})

    print("Class schedule logged successfully.")
    print(schedule_entries)

navigate_to_menu()

def main():
    options = ["Enter Classes",
               "Update Classes",
               "Delete Classes",
               "View Timetable"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()
    if menu_entry_index == 0: 
        clear()
        main_greeting()
        class_logger()  
        navigate_to_menu()  # After logging classes, return to the main menu
    elif menu_entry_index is not None:
        print(f"You have selected {options[menu_entry_index]}!")
    else:
        print("No option selected.")

main()