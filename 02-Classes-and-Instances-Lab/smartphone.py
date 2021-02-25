class Smartphone:
    def __init__(self, memory):
        self.memory = memory
        self.memory_taken = 0
        self.apps = []
        self.is_on = False

    def install(self, app_name, app_memory):
        if app_memory > self.get_memory_left():
            return f"Not enough memory to install {app_name}"
        if not self.is_on:
            return f"Turn on your phone to install {app_name}"
        self.apps.append(app_name)
        self.memory_taken += app_memory
        return f"Installing {app_name}"

    def power(self):
        self.is_on = not self.is_on

    def status(self):
        return f"Total apps: {len(self.apps)}. Memory left: {self.get_memory_left()}"

    def get_memory_left(self):
        return self.memory - self.memory_taken
