import random
from config import MAX_HEART_RATE, MIN_HEART_RATE, STRESS_THRESHOLD

class PhysiologyMonitor:
    def __init__(self):
        self.heart_rate = 340
        self.stress = 0.2
        self.arousal = 0.4

    def update(self, action, reward):
        # Simulate realistic physiological response
        if action in ("interact", "boost"):
            self.heart_rate += random.randint(8, 18)
            self.stress += 0.04
        elif reward > 1.5:
            self.stress = max(0.1, self.stress - 0.06)
            self.arousal += 0.05
        else:
            self.heart_rate -= random.randint(2, 6)

        self.heart_rate = max(MIN_HEART_RATE, min(MAX_HEART_RATE, self.heart_rate))
        self.stress = max(0.0, min(1.0, self.stress))

    def is_stressed(self):
        return self.stress > STRESS_THRESHOLD

    def get_state(self):
        return {
            "hr": self.heart_rate,
            "stress": round(self.stress, 2),
            "arousal": round(self.arousal, 2)
        }