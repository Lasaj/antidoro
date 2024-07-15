import json
import os
import datetime
from activities import Activity
from history import DoroHistory

class AntiDoro:
    def __init__(self):
        self.activities = {}
        self.selected_activity = None
        self.start_date = None
        self.history = None

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

    def open_file(self, filename):
        if not os.path.exists(filename): 
            with open(filename, "w") as file:
                json.dump({}, file)

        with open(filename, "r") as file:
            data = json.load(file)

            # Load history
            history_data = data.pop("history", {})
            self.history = DoroHistory(history_data)

            
            # Load current activities
            for name, record in data.items():
                self.add_activity(name, record[0], record[1])

        if len(self.activities) > 0:
            return True
        return False

    def save_file(self, filename):
        data = {}
        
        # Save current activities
        for name, activity in self.activities.items():
            data[name] = [activity.goal, activity.elapsed]
        
        # Save history
        data["history"] = self.history.save_history()

        with open(filename, "w") as file:
            json.dump(data, file)

    def update_week(self):
        if self.start_date is None:
            self.start_date = self.get_last_sunday()
        else:
            last_sunday = self.get_last_sunday()
            if last_sunday != self.start_date:  # Update week
                self.history.record_week(self.start_date, self.activities)
                self.start_date = last_sunday
                for name, activity in self.activities.items():
                    activity.reset()
                print("Week updated")

    ### Helper functions ###
    def get_last_sunday(self):
        current_day = datetime.date.today()
        idx = current_day.isoweekday()
        last_sunday = current_day - datetime.timedelta(days=idx)
        return last_sunday

    def archive(self):
        self.history[self.start_date] = self.activities

    def date_to_string(self, date):
        return date.strftime("%d %b %Y")
    
    def string_to_date(self, date_string):
        return datetime.datetime.strptime(date_string, "%d %b %Y").date()


if __name__ == "__main__":
    doro = AntiDoro()
    doro.update_week()
