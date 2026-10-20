import numpy as np
from config import CHANNELS, RAT_NAME

class Freddy:
    def __init__(self):
        self.name = RAT_NAME
        self.treats = 0.0
        self.total_actions = 0
        self.successful_missions = 0
        self.baseline_activity = np.random.uniform(0.3, 0.6, len(CHANNELS))

    def generate_neural_activity(self, intent="explore"):
        """Generate realistic multi-channel neural vector based on internal state"""
        activity = self.baseline_activity.copy()
        if intent == "forward":
            activity[0] += 0.45  # M1_left
            activity[1] += 0.35
        elif intent == "turn":
            activity[0] += 0.55
            activity[2] += 0.3   # PFC
        elif intent == "interact":
            activity[2] += 0.6
            activity[3] += 0.4   # VTA anticipation
        activity += np.random.normal(0, 0.12, len(activity))
        return np.clip(activity, 0, 1.2)

    def receive_reward(self, amount, reason):
        self.treats += amount
        if amount > 0:
            self.successful_missions += 1
        print(f"    [{self.name}] +{amount:.1f} treats ({reason}) | Total: {self.treats:.1f}")

    def get_status(self):
        return {
            "name": self.name,
            "treats": round(self.treats, 2),
            "actions": self.total_actions,
            "missions": self.successful_missions
        }