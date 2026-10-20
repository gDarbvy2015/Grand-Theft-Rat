# Rat Theft Auto - Experimental Configuration

RAT_NAME = "Freddy"
SESSION_DURATION_STEPS = 80
BASE_LEARNING_RATE = 0.015
NOISE_LEVEL = 0.22

# Neural channels (simulated multi-electrode array)
CHANNELS = ["M1_left", "M1_right", "PFC_decision", "VTA_reward", "S1_whisker"]

# Action space
ACTIONS = ["idle", "forward", "left", "right", "interact", "boost"]

# Reward schedule (treats)
REWARD_SCHEDULE = {
    "steal_car": 1.0,
    "complete_short_drive": 2.0,
    "complete_medium_drive": 3.5,
    "evade_detection": 2.5,
    "idle_penalty": -0.1
}

# Physiological limits
MAX_HEART_RATE = 420
MIN_HEART_RATE = 280
STRESS_THRESHOLD = 0.75
