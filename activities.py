import time
from datetime import timedelta

class Timer():
    def __init__(self):
        self.start_time = None
        self.end_time = None
        self.isRunning = False
        self.elapsed_time = 0

    def start(self):
        if self.isRunning:
            return
        self.start_time = time.time()
        self.isRunning = True

    def stop(self):
        if not self.isRunning:
            return
        self.end_time = time.time()
        self.elapsed_time += self.end_time - self.start_time
        self.isRunning = False

    def pause(self):
        if not self.isRunning:
            return
        self.end_time = time.time()
        self.elapsed_time += self.end_time - self.start_time
        self.isRunning = False

    def reset(self):
        self.start_time = None
        self.end_time = None
        self.isRunning = False
        self.elapsed_time = 0

    def get_elapsed_time(self):
        if self.isRunning:
            return time.time() - self.start_time
        return self.elapsed_time

    def is_running(self):
        return self.isRunning

    def __str__(self):
        return f"Elapsed time: {self.elapsed_time} seconds"


class Activity:
    def __init__(self, name, goal, elapsed=0):
        self.name = name
        self.goal = goal
        self.elapsed = elapsed
        self.timer = Timer()

    def report(self): 
        td = timedelta(seconds=(self.elapsed + self.timer.get_elapsed_time()))
        print(f"Activity: {self.name}\n"
              f"Time spent: {td.seconds // 3600} hours, "
              f"{(td.seconds // 60) % 60} minutes, {td.seconds % 60} seconds "
              f"out of {self.goal} hours")
    
    def reset(self):
        self.elapsed = 0

    def change_goal(self, goal):
        self.goal = goal
        
    def start_timer(self):
        if self.timer.is_running():
            return
        self.timer.start()

    # TODO: Pause timer does not work
    def pause_timer(self):
        self.timer.pause()
        self.elapsed += self.timer.get_elapsed_time()

    def stop_timer(self):
        self.timer.stop()
        self.elapsed += self.timer.get_elapsed_time()
        self.timer.reset()
    
    def reset_timer(self):
        self.timer.reset()
    
    def is_running(self):
        return self.timer.isRunning

