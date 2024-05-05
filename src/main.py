from title import main_logo, add_logo, update_logo, delete_logo, view_logo 
from clear import clear 
import csv  
from datetime import datetime  
from unique_exceptions import InvalidTimeError, EmptyInputError, InvalidClassSelectionError, InvalidScheduleFormatError  

def main_greeting():
    print("\nWelcome to Your Class Schedule Manager!")

def navigate_to_menu():
    input("Press Enter to return to the main menu.\n")
    clear()
    main_menu()

def add_class_schedule():
    clear()
    print(add_logo)
    
    while True:
        class_name = input("Enter Class Name: ")

        while True:
            day = input("Enter Day (e.g., Monday): ")
            if day.lower() in ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]:
                break
            else:
                print("Invalid day name. Please enter a valid day.")

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
                    raise InvalidTimeError("End time must be later than start time.")
                else:
                    break
            except ValueError:
                print("Invalid time format. Please enter time in HH:MM format.")
            except InvalidTimeError as e:
                print(e)
                continue

        room = input("Enter Room Number: ")

        with open('src/schedule.csv', 'r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if len(row) >= 4 and row[1] == day and row[2] <= start_time_str <= row[3]:
                    print("Error: Class overlaps with another class on the same day.")
                    break
            else:  # No overlap found, write to CSV
                with open('src/schedule.csv', 'a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([class_name, day, start_time_str, end_time_str, room])

                print("Class added successfully.")
                choice = input("Press '#' to add another class, or press Enter to return to the main menu: ")
                if choice != '#':
                    break

        navigate_to_menu()

def update_class_schedule():
    clear()
    print(update_logo)
    print("Update Class Schedule:")
    # Load existing schedule from CSV
    schedule = []
    with open('src/schedule.csv', 'r') as file:
        reader = csv.reader(file)
        schedule = list(reader)

    if not schedule:
        print("No classes found.")
        navigate_to_menu()

    print("Current Class Schedule: \n")
    for i, row in enumerate(schedule, start=1):
        if row and len(row) >= 5: 
            print(f"{i}. {row[0]} - {row[1]} - {row[2]} to {row[3]} - Room {row[4]}")
        elif row:  
            print(f"Invalid data format in row {i}: {row}")

    while True:
        try:
            choice = int(input("Enter the number of the class to update: ")) - 1
            if 0 <= choice < len(schedule):
                break
            else:
                print("Invalid selection.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            class_name = input(f"Enter Class Name ({schedule[choice][0]}): ") or schedule[choice][0]
            if class_name.strip(): 
                break
            else:
                raise EmptyInputError()
        except EmptyInputError as e:
            print(e)  
            continue  

    day = input(f"Enter Day ({schedule[choice][1]}): ") or schedule[choice][1]
    start_time = input(f"Enter Start Time ({schedule[choice][2]}): ") or schedule[choice][2]
    end_time = input(f"Enter End Time ({schedule[choice][3]}): ") or schedule[choice][3]
    room = input(f"Enter Room Number ({schedule[choice][4]}): ")


    schedule[choice] = [class_name, day, start_time, end_time, room]

    with open('src/schedule.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(schedule)

    print("Class schedule updated successfully.")

    choice = input("Press '#' to update another class, or press Enter to return to the main menu: \n")
    if choice == '#':
        update_class_schedule() 
    else:
        navigate_to_menu()

def delete_class_schedule():
    clear()
    print(delete_logo)
    print("Delete Class Schedule:")
    # Load existing schedule from CSV
    schedule = []
    with open('src/schedule.csv', 'r') as file:
        reader = csv.reader(file)
        schedule = list(reader)

    if not schedule:
        print("No classes found.")
        navigate_to_menu()
        return  

    print("Current Class Schedule:")
    for i, row in enumerate(schedule, start=1):
        if len(row) >= 5: 
            print(f"{i}. {row[0]} - {row[1]} - {row[2]} to {row[3]} - Room {row[4]}")
        else:
            print(f"{i}. Invalid data in CSV")  

    valid_choices = list(range(1, len(schedule) + 1))  # List of valid class numbers
    try:
        choice = int(input("Enter the number of the class to delete: "))
        if choice not in valid_choices:
            raise InvalidClassSelectionError()
        else:
            choice -= 1  # Adjust index for list deletion

            del schedule[choice]

            with open('src/schedule.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                for row in schedule:
                    writer.writerow(row)

            print("Class schedule deleted successfully.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except InvalidClassSelectionError as e:
        print(e)

    choice = input("Press '#' to delete another class, or press Enter to return to the main menu: ")
    if choice == '#':
        delete_class_schedule()
    else:
        navigate_to_menu()

def view_class_schedule():
    clear()
    print(view_logo)
    print("View Class Schedule:")
    # Load existing schedule from CSV
    try:
        with open('src/schedule.csv', 'r') as file:
            reader = csv.reader(file)
            schedule = [row for row in reader if row]

        if not schedule:
            print("No classes found.")
        else:
            print("Current Class Schedule:")
            days = {}
            for row in schedule:
                if len(row) >= 5:
                    if row[1] not in days:
                        days[row[1]] = []
                    days[row[1]].append(f"{row[0]} - {row[2]} to {row[3]} - Room {row[4]} \n")
                else:
                    raise InvalidScheduleFormatError()

            day_order = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
            sorted_days = sorted(days.items(), key=lambda x: day_order.index(x[0].lower()))

            for day, classes in sorted_days:
                print(f"\n{day.capitalize()}:") 
                for class_info in classes:
                    print(f"- {class_info}")

    except InvalidScheduleFormatError:
        print("Error: Invalid schedule format. Please check the format of your schedule file.")
    except FileNotFoundError:
        print("Error: Schedule file not found.")
    finally:
        navigate_to_menu()

def main_menu():
    options = [
        "Add Class",
        "Update Class",
        "Delete Class",
        "View Class Schedule",
        "Exit"
    ]

    print(main_logo) 

    if not options:  # Check if options list is empty
        print("Error: No menu options defined.")
        return

    print("\nPlease select from the following options:\n"
          "\n(Enter the number of your choice and press <Enter>)\n")

    for i, option in enumerate(options, start=1):
        print(f"{i}. {option}")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_class_schedule()
    elif choice == '2':
        update_class_schedule()
    elif choice == '3':
        delete_class_schedule()
    elif choice == '4':
        view_class_schedule()
    elif choice == '5':
        exit_program()
    else:
        print("Invalid choice. Please enter a valid option number.")

def exit_program():
    print("Thank you for using ScheduGenius!")
    exit()

if __name__ == "__main__":
    main_greeting()
    while True:
        main_menu()

# def main_menu():
#     print("\nPlease select from the following options:\n"
#           "\n(Use the up and down arrow keys to navigate the menu.)\n"
#           "\n(Press <Enter> to choose an option)\n")

#     options = [
#         "Add Class",
#         "Update Class",
#         "Delete Class",
#         "View Class Schedule",
#         "Exit\n"
#     ]

#     print(main_logo) 

#     if not options:
#         print("Error: No menu options defined.")
#         return

#     terminal_menu = TerminalMenu(options)
#     menu_entry_index = terminal_menu.show()

#     if menu_entry_index == 0:
#         add_class_schedule()
#     elif menu_entry_index == 1:
#         update_class_schedule()
#     elif menu_entry_index == 2:
#         delete_class_schedule()
#     elif menu_entry_index == 3:
#         view_class_schedule()
#     elif menu_entry_index == 4:
#         exit_program()


# def exit_program():
#     print("Thank you for using ScheduGenius!")
#     exit()

# if __name__ == "__main__":
#     main_greeting()
#     while True:
#         main_menu()