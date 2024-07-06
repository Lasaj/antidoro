import json
import os
from activities import Activity

class AntiDoro:
    def __init__(self):
        self.activities = {}
        self.selected_activity = None

    def add_activity(self, name, goal, elapsed=0):
        if name in self.activities:  # Check if activity already exists
            replace = input("Activity already exists. Replace? (y/n): ")
            if replace.lower() == "y":
                new_goal = float(input("Enter the goal in hours: "))
                self.activities[name] = Activity(name, new_goal, elapsed)
            elif replace.lower() == "n":
                return
            else:
                print("Invalid choice")
        else:  # Add new activity
            self.activities[name] = Activity(name, goal, elapsed)

    def remove_activity(self, name):
        if name in self.activities:
            del self.activities[name]
            print("Activity removed")
        else:
            print("Activity not found")

    def select_activity(self, name):
        if name in self.activities:
            self.selected_activity = self.activities[name]
            return True
        else:
            return False

    def report(self):
        for name, activity in self.activities.items():
            activity.report()

    def report_activity(self):
        self.selected_activity.report()

    def reset(self):
        self.selected_activity.reset()

    def change_goal(self, goal):
        self.selected_activity.change_goal(goal)

    def start_timer(self):
        self.selected_activity.start_timer()

    def pause_timer(self):
        self.selected_activity.pause_timer()

    def stop_timer(self):
        self.selected_activity.stop_timer()

    def reset_timer(self):
        self.selected_activity.reset_timer()

    def get_current_activity(self):
        return self.selected_activity

    # TODO: load elapsed time from file
    def open_file(self, filename):
        if not os.path.exists(filename): 
            with open(filename, "w") as file:
                json.dump({}, file)

        with open(filename, "r") as file:
            data = json.load(file)
            for name, record in data.items():
                self.add_activity(name, record[0], record[1])

        if len(self.activities) > 0:
            return True
        return False

    # TODO: save elapsed time to file
    def save_file(self, filename):
        data = {}
        for name, activity in self.activities.items():
            data[name] = [activity.goal, activity.elapsed]
        with open(filename, "w") as file:
            json.dump(data, file)