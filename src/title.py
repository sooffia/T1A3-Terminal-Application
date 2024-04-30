# Tittle Art

main_logo = """
 ____       _              _        ____            _           
/ ___|  ___| |__   ___  __| |_   _ / ___| ___ _ __ (_)_   _ ___ 
\___ \ / __| '_ \ / _ \/ _` | | | | |  _ / _ \ '_ \| | | | / __|
 ___) | (__| | | |  __/ (_| | |_| | |_| |  __/ | | | | |_| \__ \ 
|____/ \___|_| |_|\___|\__,_|\__,_|\____|\___|_| |_|_|\__,_|___/
                                                                
""" 
from title import main_logo
from simple_term_menu import TerminalMenu
from clear import clear 
import json 

print(main_logo)

def main_greeting():
    print("Welcome to Your Personal Class Schedule Manager")

def navigate_to_menu():
    input("Press Enter to return to the main menu.")
    clear()
    print(main_logo)
    main_greeting()
    main()

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
    print(json.dumps(schedule_entries, indent=4))
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
    elif menu_entry_index is not None:
        print(f"You have selected {options[menu_entry_index]}!")
main()