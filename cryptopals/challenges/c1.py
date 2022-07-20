from cryptopals.challenges import BaseChallenge, BaseSolution
from cryptopals.ui import UI
from base64 import b64encode

class Challenge(BaseChallenge, id=1):
    """
    Challenge 1: Hex to Base64
    """
    challenge: bytes

    def __init__(self) -> None:
        """
        Initialize the challenge.
        """
        self.challenge = Challenge.get_random_text()
        self.solution_hash = self.hash(b64encode(self.challenge))


class Solution(BaseSolution, id=1):
    solution: bytes
    challenge: bytes

    def __init__(self, challenge: bytes) -> None:
        self.challenge = challenge
        self.solution = b64encode(challenge)
    
    def pretty(self) -> None:
        UI.table_view(
            data={
                "UTF-8": (UI.hard_wrap(UI.sanitize(self.challenge), 16), 16),
                "Base64": (UI.sanitize(self.solution), 16),
            }
    )