class Mission:
    def __init__(self):
        self.active = None
        self.progress = 0
        self.target = 0

    def start(self, mission_type):
        self.active = mission_type
        if mission_type == "short_drive":
            self.target = 4
        elif mission_type == "medium_drive":
            self.target = 8
        self.progress = 0
        return f"Mission started: {mission_type}"

    def update(self, action):
        if not self.active:
            return None
        if action in ("forward", "boost"):
            self.progress += 1
        if self.progress >= self.target:
            completed = self.active
            self.active = None
            self.progress = 0
            return completed
        return None

    def status(self):
        if not self.active:
            return "No active mission"
        return f"{self.active}: {self.progress}/{self.target}"