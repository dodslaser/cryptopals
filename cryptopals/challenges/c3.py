from cryptopals.challenges import BaseChallenge, BaseSolution
from cryptopals.challenges.c2 import xor_bytes
from cryptopals.ui import UI


class Challenge(BaseChallenge, id=3):
    """
    Challenge 1: Single-byte XOR cipher
    """
    challenge: bytes
    solution_hash: bytes

    def __init__(self) -> None:
        plaintext=Challenge.get_random_text()
        key = self.get_random_bytes(1) * len(plaintext)
        self.challenge = xor_bytes(plaintext, key)
        self.solution_hash = self.hash(plaintext)

class Solution(BaseSolution, id=3):
    solution: bytes
    challenge: bytes
    key: bytes

    def __init__(self, challenge: bytes) -> None:
        self.challenge = challenge
        self.key = b"\x00"
        self.solution = xor_bytes(self.challenge, self.key*len(challenge))
    

    def pretty(self) -> None:
        UI.table_view(
            data = {
                "Cipher": (self.challenge.hex(" "), 24),
                "Key": ((self.key*len(self.challenge)).hex(" "), 24),
                "Plain": (UI.hard_wrap(UI.sanitize(self.solution), 8), 8),
            }
    )