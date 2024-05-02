from title import main_logo
from simple_term_menu import TerminalMenu
from clear import clear 
import csv 
from datetime import datetime 
from unique_exceptions import InvalidTimeError, NumberInputError 

print(main_logo)

def main_greeting():
    print("Welcome to Your Class Schedule Manager")

def navigate_to_menu():
    input("Press Enter to return to the main menu.\n")
    print(main_logo) 
    main_menu()

def add_class_schedule():
    clear()
    while True:
        class_name = input("Enter Class Name: ")
        day = input("Enter Day (e.g., Monday): ")
        
        while True:
            start_time_str = input("Enter Start Time (HH:MM): ")
            try:
                start_time = datetime.strptime(start_time_str, "%H:%M")
                break  
            except ValueError:
                print("Invalid time format. Please enter time in HH:MM format.")
        
        while True:
            end_time_str = input("Enter End Time (HH:MM): ")
            try:
                end_time = datetime.strptime(end_time_str, "%H:%M")
                if end_time <= start_time:
                    raise InvalidTimeError  
                else:
                    break  
            except ValueError:
                print("Invalid time format. Please enter time in HH:MM format.")
            except InvalidTimeError as e:
                print(e)  
        
        room = input("Enter Room Number: ")

        # Write to the CSV file
        with open('schedule.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([class_name, day, start_time, end_time, room])

        print("Class added successfully.")

        choice = input("Press '#' to add another class, or press Enter to return to the main menu:: ")
        if choice != '#':
            break

    navigate_to_menu()

def update_class_schedule():
    clear()
    print("Update Class Schedule:")
    # Load existing schedule from CSV
    schedule = []
    with open('schedule.csv', 'r') as file:
        reader = csv.reader(file)
        schedule = list(reader)

    if not schedule:
        print("No classes found.")
        navigate_to_menu()

    print("Current Class Schedule:")
    for i, row in enumerate(schedule, start=1):
        print(f"{i}. {row[0]} - {row[1]} - {row[2]} to {row[3]} - Room {row[4]}")

    try:
        choice = int(input("Enter the number of the class to update: ")) - 1
        if 0 <= choice < len(schedule):
            class_name = input(f"Enter Class Name ({schedule[choice][0]}): ") or schedule[choice][0]
            day = input(f"Enter Day ({schedule[choice][1]}): ") or schedule[choice][1]
            start_time = input(f"Enter Start Time ({schedule[choice][2]}): ") or schedule[choice][2]
            end_time = input(f"Enter End Time ({schedule[choice][3]}): ") or schedule[choice][3]

            # Validate room number input
            while True:
                room_input = input(f"Enter Room Number ({schedule[choice][4]}): ") or schedule[choice][4]
                try:
                    room = int(room_input)
                    break  # Exit the loop if the input is a valid number
                except ValueError:
                    print("Invalid room number. Please enter a valid number.")

            schedule[choice] = [class_name, day, start_time, end_time, room]

            with open('schedule.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(schedule)

            print("Class schedule updated successfully.")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    navigate_to_menu()
        
def delete_class_schedule():
    clear()
    print("Delete Class Schedule:")
    # Load existing schedule from CSV
    schedule = []
    with open('schedule.csv', 'r') as file:
        reader = csv.reader(file)
        schedule = list(reader)

    if not schedule:
        print("No classes found.")
        navigate_to_menu()

    print("Current Class Schedule:")
    for i, row in enumerate(schedule, start=1):
        print(f"{i}. {row[0]} - {row[1]} - {row[2]} to {row[3]} - Room {row[4]}")

    try:
        choice = int(input("Enter the number of the class to delete: ")) - 1
        if 0 <= choice < len(schedule):
            del schedule[choice]

            with open('schedule.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerows(schedule)

            print("Class schedule deleted successfully.\n")
        else:
            print("Invalid selection.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

    navigate_to_menu()

def view_class_schedule():
    clear()
    print("View Class Schedule:")
    # Load existing schedule from CSV
    with open('schedule.csv', 'r') as file:
        reader = csv.reader(file)
        schedule = list(reader)

    if not schedule:
        print("No classes found.")
    else:
        print("Current Class Schedule:")
        days = {}
        for row in schedule:
            if row[1] not in days:
                days[row[1]] = []
            days[row[1]].append(f"{row[0]} - {row[2]} to {row[3]} - Room {row[4]}")

        for day in sorted(days.keys()):  # Sort the days for consistency
            print(f"\n{day}:")
            classes = days[day]
            for class_info in classes:
                print(f"- {class_info}")

    navigate_to_menu()

def main_menu():
    options = [
        "Add Class",
        "Update Class",
        "Delete Class",
        "View Class Schedule",
        "Exit"
    ]
    terminal_menu = TerminalMenu(options)
    menu_entry_index = terminal_menu.show()

    if menu_entry_index == 0:
        add_class_schedule()
    elif menu_entry_index == 1:
        update_class_schedule()
    elif menu_entry_index == 2:
        delete_class_schedule()
    elif menu_entry_index == 3:
        view_class_schedule()
    elif menu_entry_index == 4:
        exit_program()

def exit_program():
    print("Thank you for using Your Class Schedule Manager!")
    exit()

if __name__ == "__main__":
    main_greeting()
    while True:
        main_menu()