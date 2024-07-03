import time
from datetime import timedelta

class Timer():
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.is_running = False
        self.elapsed_time = 0

    def start(self):
        self.start_time = time.time()
        self.is_running = True

    def stop(self):
        self.end_time = time.time()
        self.elapsed_time += self.end_time - self.start_time
        self.is_running = False

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.is_running = False
        self.elapsed_time = 0

    def get_elapsed_time(self):
        if self.is_running:
            return time.time() - self.start_time
        return self.elapsed_time

    def is_running(self):
        return self.is_running

    def __str__(self):
        return f"Elapsed time: {self.elapsed_time} seconds"


class Activity:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.elapsed = 0
        self.isRunning = False
        self.timer = Timer()

    def report(self):
        time_spent = str(timedelta(seconds=self.elapsed))
        td = timedelta(seconds=self.elapsed)
        print(f"elapsed time spent on {self.name}: {time_spent} out of "
              f"{self.goal} hours")
        print(f"Time spent: {td.days} days, {td.seconds // 3600} hours, "
              f"{(td.seconds // 60) % 60} minutes, {td.seconds % 60} seconds")
    
    def reset(self):
        self.elapsed = 0
        self.isRunning = False

    def change_goal(self, goal):
        self.goal = goal
        
    def start_timer(self):
        self.timer.start()

    def pause_timer(self):
        self.timer.stop()

    def stop_timer(self):
        self.timer.stop()
        self.elapsed += self.timer.get_elapsed_time()
        self.timer.reset()
    
    def reset_timer(self):
        self.timer.reset()
    
    def is_running(self):
        return self.timer.is_running

