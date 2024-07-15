import datetime
from activities import Activity


class DoroHistory():
    def __init__(self, history_data = None):
        self.history_data = history_data
        self.history = {}

    def load_history(self):
        if self.history_data:
            for date, activities in self.history_data.items():
                date = self.string_to_date(date)
                self.history[date] = {}
                for name, activity in activities.items():
                    self.history[date][name] = Activity(name, activity[0], activity[1])

    def save_history(self):
        history_data = {}
        for date, activities in self.history.items():
            date = self.date_to_string(date)
            history_data[date] = {}
            for name, activity in activities.items():
                history_data[date][name] = [activity.goal, activity.elapsed]
        return history_data

    def record_week(self, start_date, activities):
        self.history[start_date] = activities

    ### Helper functions ###
    def date_to_string(self, date):
        return date.strftime("%d %b %Y")
    
    def string_to_date(self, date_string):
        return datetime.datetime.strptime(date_string, "%d %b %Y").date()