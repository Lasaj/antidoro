import time

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
        self.current = 0
        self.isRunning = False
        self.timer = Timer()

    def report(self):
        print(f"Current time spent on {self.name}: {self.current} out of "
              f"{self.goal} hours")
    
    def reset(self):
        self.current = 0
        self.isRunning = False

    def change_goal(self, goal):
        self.goal = goal
        
    def start_timer(self):
        self.timer.start()

    def pause_timer(self):
        self.timer.stop()

    def stop_timer(self):
        self.timer.stop()
        self.current += self.timer.get_elapsed_time()
        self.timer.reset()
    
    def reset_timer(self):
        self.timer.reset()
    
    def is_running(self):
        return self.timer.is_running

