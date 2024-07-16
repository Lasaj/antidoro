from antidoro import AntiDoro
import sys


def new_activity():
    name = input("Enter the name of the activity: ")
    hours_valid = False
    while not hours_valid:
        try:
            goal = float(input("Enter the goal in hours: "))
            hours_valid = True
        except ValueError:
            print("Invalid input. Please enter a number")
    return name, goal


def new_doro(doro):
    print("Welcome to AntiDoro!")
    print("Let's start by creating a new activity")
    name, goal = new_activity()
    doro.add_activity(name, goal)
    doro.select_activity(name)


def select_activity(doro):
    while True:
        print("\nMain Menu:")
        print("1. Start a new activity")
        print("2. List activities")
        print("3. Select an activity")
        print("4. Remove an activity")
        print("5. Show history")
        print("6. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name, goal = new_activity()
            doro.add_activity(name, goal)
            doro.select_activity(name)
            break
        elif choice == "2":
            doro.report()
        elif choice == "3":
            doro.report()
            valid = False
            while not valid:
                name = input("Enter the name of the activity: ")
                valid = doro.select_activity(name)
                if not valid:
                    print("Activity not found")
            break
        elif choice == "4":
            doro.report()
            name = input("Enter the name of the activity: ")
            doro.remove_activity(name)
        elif choice == "5":
            doro.show_history()
        elif choice == "6":
            doro.save_file("doro.json")
            sys.exit()
        else:
            print("Invalid choice")

def manage_activity(doro, filename):  
    while True:
        print("\nWeek of", doro.start_date.strftime("%d %b %Y"))
        print("Activity Menu:")
        print("1. Select an activity")
        print("2. Report")
        print("3. Reset")
        print("4. Change goal")
        print("5. Start timer")
        print("6. Pause timer")
        print("7. Stop Timer")
        print("8. Exit")
        print("Current activity:", doro.selected_activity.name, end='')
        if doro.selected_activity.is_running():
            print(" (Running)")
            doro.report_activity()
        else:
            print(": (Not running)")
        choice = input("Enter your choice: ")
        if choice == "1":
            select_activity(doro)
        elif choice == "2":
            doro.report_activity()
        elif choice == "3":
            doro.reset()
        elif choice == "4":
            goal = float(input("Enter the new goal in hours: "))
            doro.change_goal(goal)
        elif choice == "5":
            doro.start_timer()
        elif choice == "6":
            doro.pause_timer()
        elif choice == "7":
            doro.stop_timer()
        elif choice == "8":
            doro.save_file(filename)
            sys.exit()
        else:
            print("Invalid choice")


def main(filename=None):
    if not filename:
        filename="doro.json"
    doro = AntiDoro()
    try:
        activities_exist = doro.open_file(filename)
    except Exception as e:
        print(e)
        activities_exist = False
    doro.update_week()
    if not activities_exist:
        new_doro(doro)
    else:
        select_activity(doro)
    manage_activity(doro, filename=filename)


if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")

    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        filename = None

    main(filename)