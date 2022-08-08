from cryptopals.challenges import BaseChallenge, BaseSolution
from cryptopals.ui import UI
from typing import Tuple

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR two bytes objects."""
    ai = int.from_bytes(a, byteorder="big")
    bi = int.from_bytes(b, byteorder="big") 
    return int.to_bytes(ai ^ bi, max(map(len, [a, b])), byteorder="big")


class Challenge(BaseChallenge, id=2):
    """Challenge 2
    Fixed XOR
    """
    challenge: Tuple[bytes, bytes]
    solution_hash: bytes

    def __init__(self) -> None:
        self.challenge = (
            Challenge.get_random_text().ljust(64, b"\x00")[:64],
            Challenge.get_random_text().ljust(64, b"\x00")[:64]
        )
        self.solution_hash = self.hash(xor_bytes(*self.challenge))


class Solution(BaseSolution, id=2):
    solution: bytes
    challenge: Tuple[bytes, bytes]

    def __init__(self, challenge: Tuple[bytes, bytes]) -> None:
        self.challenge = challenge 
        self.solution = xor_bytes(*challenge)
    
    def pretty(self) -> None:
        UI.table_view(
            data = {
                h: (UI.hard_wrap(UI.sanitize(v), 16), 16)
                for h, v in zip(["A", "B", "A^B"], [*self.challenge, self.solution])
            }
    )
