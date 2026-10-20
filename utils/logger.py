import json
from datetime import datetime

class SessionLogger:
    def __init__(self):
        self.events = []

    def log(self, step, data):
        entry = {"step": step, "timestamp": datetime.now().isoformat(), **data}
        self.events.append(entry)

    def save(self, filename="session_log.json"):
        with open(filename, "w") as f:
            json.dump(self.events, f, indent=2)
        print(f"Session log saved to {filename}")

    def summary(self):
        return {
            "total_events": len(self.events),
            "last_event": self.events[-1] if self.events else None
        }