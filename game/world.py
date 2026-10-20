import random

class World:
    def __init__(self):
        self.cars_available = 8
        self.detection_level = 0.0
        self.current_zone = "industrial"
        self.zones = ["industrial", "downtown", "docks", "suburbs"]

    def attempt_steal(self):
        if self.cars_available <= 0:
            return False, "no cars left"
        success = random.random() > 0.25
        if success:
            self.cars_available -= 1
            self.detection_level += 0.15
            return True, "car stolen"
        self.detection_level += 0.08
        return False, "steal failed"

    def drive_distance(self, steps=1):
        self.detection_level = max(0, self.detection_level - 0.05 * steps)
        return steps

    def check_detection(self):
        if self.detection_level > 0.8:
            return True, "high detection"
        return False, "clear"

    def change_zone(self):
        self.current_zone = random.choice(self.zones)
        return self.current_zone