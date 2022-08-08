"""Challenge 1"""

from base64 import b64encode

from cryptopals.challenges import BaseChallenge, BaseSolution
from cryptopals.ui import UI


class Challenge(BaseChallenge, id=1):
    """Challenge 1
    Hex to Base64
    """
    challenge: bytes

    def __init__(self) -> None:
        self.challenge = Challenge.get_random_text()
        self.solution_hash = self.hash(b64encode(self.challenge))
        super().__init__()

    def check(self, solution: bytes) -> bool:
        return self.hash(solution) == self.solution_hash


class Solution(BaseSolution, id=1):
    """Solution - Challenge 1
    Encodes challenge bytes to base64
    """
    solution: bytes
    challenge: bytes

    def __init__(self, challenge: bytes) -> None:
        self.challenge = challenge
        self.solution = b64encode(challenge)
        super().__init__()

    def pretty(self) -> None:
        UI.table_view(
            data={"UTF-8": self.challenge, "Base64": self.solution},
            widths=[16, 16]
        )
