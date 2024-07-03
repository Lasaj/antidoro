import json
import os
from activities import Activity

class AntiDoro:
    def __init__(self):
        self.activities = {}
        self.selected_activity = None

    def add_activity(self, name, goal):
        if name in self.activities:  # Check if activity already exists
            replace = input("Activity already exists. Replace? (y/n): ")
            if replace.lower() == "y":
                new_goal = float(input("Enter the goal in hours: "))
                self.activities[name] = Activity(name, new_goal)
            elif replace.lower() == "n":
                return
            else:
                print("Invalid choice")
        else:  # Add new activity
            self.activities[name] = Activity(name, goal)

    def remove_activity(self, name):
        if name in self.activities:
            del self.activities[name]
        else:
            print("Activity not found")

    def select_activity(self, name):
        if name in self.activities:
            self.selected_activity = self.activities[name]
            return True
        else:
            return False

    def report(self):
        for activity in self.activities.values():
            activity.report()

    def reset(self):
        for activity in self.activities.values():
            activity.reset()

    def change_goal(self, name, goal):
        self.activities[name].change_goal(goal)

    def start_timer(self, name):
        self.activities[name].start_timer()

    def pause_timer(self, name):
        self.activities[name].pause_timer()

    def stop_timer(self, name):
        self.activities[name].stop_timer()

    def reset_timer(self, name):
        self.activities[name].reset_timer()

    def open_file(self, filename):
        if not os.path.exists(filename): 
            with open(filename, "w") as file:
                json.dump({}, file)

        with open(filename, "r") as file:
            data = json.load(file)
            for name, goal in data.items():
                self.add_activity(name, goal)

        if len(self.activities) > 0:
            return True
        return False

    def save_file(self, filename):
        data = {}
        for name, activity in self.activities.items():
            data[name] = activity.goal
        with open(filename, "w") as file:
            json.dump(data, file)