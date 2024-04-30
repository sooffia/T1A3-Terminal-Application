from title import main_logo
from simple_term_menu import TerminalMenu
from clear import clear 
import json 

print(main_logo)

def main_greeting():
    print("Welcome to Your Personal Class Schedule Manager")

def navigate_to_menu():
    input("Press Enter to return to the main menu. \n")
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
    file_class = "schedule.json"
    with open(file_class, "w") as file:
        json.dump(schedule_entries, file, indent=4)
    navigate_to_menu()

def update_classes():
    file_class = "schedule.json"
    try:
        with open(file_class, "r") as file:
            schedule_entries = json.load(file)
    except FileNotFoundError:
        print("No class schedule found. Please log classes first.")
        navigate_to_menu()
        return

    print("Current Class Schedule:")
    for i, entry in enumerate(schedule_entries, start=1):
        print(f"{i}. {entry['day']} - {entry['start_time']} to {entry['end_time']} in {entry['class_room']} with {entry['teacher_name']}")

    update_index = int(input("Enter the number of the class to update: ")) - 1
    if 0 <= update_index < len(schedule_entries):
        entry = schedule_entries[update_index]
        print("Update Class Schedule:")
        entry["day"] = input(f"Enter Day ({entry['day']}): ") or entry["day"]
        entry["start_time"] = input(f"Enter Start Time ({entry['start_time']}): ") or entry["start_time"]
        entry["end_time"] = input(f"Enter End Time ({entry['end_time']}): ") or entry["end_time"]
        entry["class_room"] = input(f"Enter Class Room ({entry['class_room']}): ") or entry["class_room"]
        entry["teacher_name"] = input(f"Enter Teacher's Name ({entry['teacher_name']}): ") or entry["teacher_name"]

        with open(file_class, "w") as file:
            json.dump(schedule_entries, file, indent=4)
        print("Class schedule updated successfully.")
    else:
        print("Invalid class number. Update cancelled.")

    navigate_to_menu()


def main():
    options = ["Enter Classes",
               "Update Classes",
               "Delete Classes",
               "View Timetable \n"]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show() 
    if menu_entry_index == 0: 
        clear()
        main_greeting()
        class_logger()  
    elif menu_entry_index == 1:
        clear()
        main_greeting()
        update_classes()
        navigate_to_menu()
    elif menu_entry_index is not None:
        print(f"You have selected {options[menu_entry_index]}!")

main()