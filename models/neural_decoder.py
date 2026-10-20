import numpy as np
from config import CHANNELS, ACTIONS, BASE_LEARNING_RATE, NOISE_LEVEL

class NeuralDecoder:
    def __init__(self):
        self.weights = np.random.randn(len(CHANNELS), len(ACTIONS)) * 0.3
        self.bias = np.zeros(len(ACTIONS))
        self.learning_rate = BASE_LEARNING_RATE
        self.history = []

    def decode(self, neural_vector):
        """Decode multi-channel neural activity into action probabilities"""
        noisy = neural_vector + np.random.normal(0, NOISE_LEVEL, len(neural_vector))
        logits = noisy @ self.weights + self.bias
        exp_logits = np.exp(logits - np.max(logits))
        probs = exp_logits / exp_logits.sum()
        action_idx = np.argmax(probs)
        confidence = probs[action_idx]
        return ACTIONS[action_idx], confidence, probs

    def update(self, neural_vector, action, reward):
        """Simple online adaptation based on reward"""
        action_idx = ACTIONS.index(action)
        error = reward - 0.5  # centered
        self.weights[:, action_idx] += self.learning_rate * error * neural_vector
        self.bias[action_idx] += self.learning_rate * error * 0.1
        self.history.append({"action": action, "reward": reward, "error": error})

    def get_weight_summary(self):
        return {
            "mean_weight": float(np.mean(self.weights)),
            "max_weight": float(np.max(self.weights)),
            "updates": len(self.history)
        }