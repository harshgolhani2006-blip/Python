from typing import Dict, Any
import random

class EmailEnv:

    def __init__(self):
        self.emails = []
        self.current_index = 0
        self.done = False

    def reset(self) -> Dict:
        self.emails = [
            {"text": "Server is down!", "label": "urgent"},
            {"text": "Meeting at 5 PM", "label": "normal"},
            {"text": "Discount offer just for you", "label": "spam"}
        ]
        random.shuffle(self.emails)

        self.current_index = 0
        self.done = False

        return self.state()

    def state(self) -> Dict:
        if self.current_index >= len(self.emails):
            return {"message": "No emails left"}

        return {
            "email": self.emails[self.current_index]["text"]
        }

    def step(self, action: str):
        """
        action: 'urgent', 'normal', 'spam'
        """
        if self.done:
            return self.state(), 0, True, {}

        correct = self.emails[self.current_index]["label"]

        reward = 0

        if action == correct:
            reward = 1.0
        else:
            reward = -0.5

        self.current_index += 1

        if self.current_index >= len(self.emails):
            self.done = True

        return self.state(), reward, self.done, {}