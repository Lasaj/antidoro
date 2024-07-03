from antidoro import AntiDoro
import sys


def new_activity():
    name = input("Enter the name of the activity: ")
    goal = float(input("Enter the goal in hours: "))
    return name, goal


def new_doro(doro):
    print("Welcome to AntiDoro!")
    print("Let's start by creating a new activity")
    name, goal = new_activity()
    doro.add_activity(name, goal)


def select_activity(doro):
    while True:
        print("1. Start a new activity")
        print("2. Select an activity")
        print("3. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            name, goal = new_activity()
            doro.add_activity(name, goal)
            break
        elif choice == "2":
            doro.report()
            name = input("Enter the name of the activity: ")
            valid = False
            while not valid:
                valid = doro.select_activity(name)
                if not valid:
                    print("Activity not found")
            break
        elif choice == "3":
            doro.save_file("doro.json")
            sys.exit()
        else:
            print("Invalid choice")

def manage_activity(doro):
    while True:
        print("1. Select an activity")
        print("2. Report")
        print("3. Reset")
        print("4. Change goal")
        print("5. Start timer")
        print("6. Pause timer")
        print("7. Stop Timer")
        print("8. Select an activity")
        print("9. Exit")
        doro
        choice = input("Enter your choice: ")
        if choice == "1":
            select_activity(doro)
        elif choice == "2":
            doro.report()
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
            doro.save_file("doro.json")
            sys.exit()
        else:
            print("Invalid choice")


def main():
    doro = AntiDoro()
    activities_exist = doro.open_file("doro.json")
    if not activities_exist:
        new_doro(doro)
    select_activity(doro)
    manage_activity(doro)


if __name__ == "__main__":
    main()