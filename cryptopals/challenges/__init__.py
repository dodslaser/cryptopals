from base64 import b64decode
from random import randint
from hashlib import sha256
from functools import singledispatchmethod

class BaseChallenge:
    """
    Class to represent a cryptopals challenge.
    """
    id: int
    challenge: object
    solution_hash: bytes

    def __init_subclass__(cls, id: int) -> None:
        cls.id = id

    def __init__(self) -> None:
        raise NotImplementedError
    
    @singledispatchmethod
    def check(self, solution) -> bool:
        """
        Check the if solution is valid for challenge
        """
        raise NotImplementedError
    
    @check.register
    def _(self, solution: bytes) -> bool:
        return self.hash(solution) == self.solution_hash

    @staticmethod
    def get_random_text() -> bytes:
        """
        Return a random string as bytes from corpus
        """
        enc = _corpus[randint(0, len(_corpus) - 1)]
        return b64decode(enc)
    
    @staticmethod
    def hash(solution: bytes) -> bytes:
        """
        Hash the solution.
        """
        return sha256(solution).digest()
    
    @staticmethod
    def get_random_bytes(n: int):
        """
        Return a random string of bytes of length n.
        """
        return bytes([randint(0, 255) for _ in range(n)])


class BaseSolution:
    """
    Class for solving a challenge.
    """
    id: int
    challenge: object
    solution: object

    def __init_subclass__(cls, id: int) -> None:
        cls.id = id

    def __init__(self):
        """
        Initialize the solution.
        """
        raise NotImplementedError
    
    def pretty(self) -> None:
        """
        Pretty print the solution.
        """
        raise NotImplementedError


_corpus = [
    "WW8gVklQLCBsZXQncyBraWNrIGl0",
    "QWxyaWdodCBzdG9wLCBjb2xsYWJvcmF0ZSBhbmQgbGlzdGVu",
    "SWNlIGlzIGJhY2sgd2l0aCB0aGUgYnJhbmQgbmV3IGludmVudGlvbg==",
    "U29tZXRoaW5nIGdyYWJzIGEgaG9sZCBvZiBtZSB0aWdodGx5",
    "RmxvdyBsaWtlIGEgaGFycG9vbiBkYWlseSBhbmQgbmlnaHRseQ==",
    "IldpbGwgaXQgZXZlciBzdG9wPyIgWW8sIEkgZG9uJ3Qga25vdw==",
    "VHVybiBvZmYgdGhlIGxpZ2h0cywgaHVoLCBhbmQgSSdsbCBnbG93",
    "VG8gdGhlIGV4dHJlbWUsIEkgcm9jayBhIG1pYyBsaWtlIGEgdmFuZGFs",
    "TGlnaHQgdXAgYSBzdGFnZSBhbmQgd2F4IGEgY2h1bXAgbGlrZSBhIGNhbmRsZQ==",
    "RGFuY2UsIHJ1c2ggdGhlIHNwZWFrZXIgdGhhdCBib29tcw==",
    "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t",
    "RGVhZGx5IHdoZW4gSSBwbGF5IGEgZG9wZSBtZWxvZHk=",
    "QW55dGhpbmcgbGVzcyB0aGFuIHRoZSBiZXN0IGlzIGEgZmVsb255",
    "TG92ZSBpdCBvciBsZWF2ZSBpdCwgeW91IGJldHRlciBnYW5nd2F5",
    "WW91IGJldHRlciBoaXQgdGhlIGJ1bGxzZXllLCB0aGUga2lkIGRvbid0IHBsYXk=",
    "QW5kIGlmIHRoZXJlIHdhcyBhIHByb2JsZW0sIHlvLCBJJ2xsIHNvbHZlIGl0",
    "Q2hlY2sgb3V0IHRoZSBob29rIHdoaWxlIG15IERKIHJldm9sdmVzIGl0",
    "Tm93IHRoYXQgdGhlIHBhcnR5IGlzIGp1bXBpbic=",
    "V2l0aCB0aGUgYmFzcyBraWNrZWQgaW4gYW5kIHRoZSBWZWdhcyBhcmUgcHVtcGluJw==",
    "UXVpY2sgdG8gdGhlIHBvaW50LCB0byB0aGUgcG9pbnQsIG5vIGZha2luJw==",
    "Q29va2luJyBNQ3MgbGlrZSBhIHBvdW5kIG9mIGJhY29u",
    "QnVybmluJyAnZW0gaWYgeW91J3JlIG5vdCBxdWljayBhbmQgbmltYmxl",
    "SSBnbyBjcmF6eSB3aGVuIEkgaGVhciBhIGN5bWJhbA==",
    "QW5kIGEgaGktaGF0IHdpdGggYSBzb3VwZWQgdXAgdGVtcG8=",
    "SSdtIG9uIGEgcm9sbCwgaXQncyB0aW1lIHRvIGdvIHNvbG8=",
    "Um9sbGluJyBpbiBteSA1LjA=",
    "V2l0aCB0aGUgcmFndG9wIGRvd24gc28gbXkgaGFpciBjYW4gYmxvdw==",
    "VGhlIGdpcmxpZXMgb24gc3RhbmRieSwgd2F2aW4nIGp1c3QgdG8gc2F5IGhp",
    "IkRpZCB5b3Ugc3RvcD8iIE5vLCBJIGp1c3QgZHJvdmUgYnk=",
    "S2VwdCBvbiwgcHVyc3VpbicgdG8gdGhlIG5leHQgc3RvcA==",
    "SSBidXN0ZWQgYSBsZWZ0IGFuZCBJJ20gaGVhZGluJyB0byB0aGUgbmV4dCBzdG9w",
    "VGhlIGJsb2NrIHdhcyBkZWFkLCB5bywgc28gSSBjb250aW51ZWQgdG8=",
    "QTFBIEJlYWNoZnJvbnQgQXZlbnVl",
    "R2lybHMgd2VyZSBob3Qgd2VhcmluZyBsZXNzIHRoYW4gYmlraW5pcw==",
    "Um9ja21hbiBsb3ZlcnMgZHJpdmluZyBMYW1ib3JnaGluaXM=",
    "SmVhbG91cywgJ2NhdXNlIEknbSBvdXQgZ2V0dGluZyBtaW5l",
    "U2hheSB3aXRoIGEgZ2F1Z2UgYW5kIFZhbmlsbGEgd2l0aCBhIDk=",
    "UmVhZHkgZm9yIHRoZSBjaHVtcHMgb24gdGhlIHdhbGw=",
    "VGhlIGNodW1wcyBhY3RpbmcgaWxsIGJlY2F1c2UgdGhleSdyZSBmdWxsIG9mIGVpZ2h0IGJhbGw=",
    "R3Vuc2hvdHMgcmFnZWQgb3V0IGxpa2UgYSBiZWxs",
    "SSBncmFiYmVkIG15IDksIGFsbCBJIGhlYXJkIHdlcmUgc2hlbGxz",
    "RmFsbGluZyBvbiB0aGUgY29uY3JldGUgcmVhbCBmYXN0",
    "SnVtcGVkIGluIG15IGNhciwgc2xhbW1lZCBvbiB0aGUgZ2Fz",
    "QnVtcGVyIHRvIGJ1bXBlciwgdGhlIGF2ZW51ZSdzIHBhY2tlZA==",
    "SSdtIHRyeWluZyB0byBnZXQgYXdheSBiZWZvcmUgdGhlIGphY2tlcnMgamFjaw==",
    "UG9saWNlIG9uIHRoZSBzY2VuZSwgeW91IGtub3cgd2hhdCBJIG1lYW4/",
    "VGhleSBwYXNzZWQgbWUgdXAsIGNvbmZyb250ZWQgYWxsIHRoZSBkb3BlIGZpZW5kcw==",
    "SWYgdGhlcmUgd2FzIGEgcHJvYmxlbSwgeW8sIEknbGwgc29sdmUgaXQ=",
    "Q2hlY2sgb3V0IHRoZSBob29rIHdoaWxlIG15IERKIHJldm9sdmVzIGl0",
    "VGFrZSBoZWVkICdjYXVzZSBJJ20gYSBseXJpY2FsIHBvZXQ=",
    "TWlhbWkncyBvbiB0aGUgc2NlbmUganVzdCBpbiBjYXNlIHlvdSBkaWRuJ3Qga25vdyBpdA==",
    "TXkgdG93biB0aGF0IGNyZWF0ZWQgYWxsIHRoZSBiYXNzIHNvdW5k",
    "RW5vdWdoIHRvIHNoYWtlIGFuZCBraWNrIGhvbGVzIGluIHRoZSBncm91bmQ=",
    "J0NhdXNlIG15IHN0eWxlJ3MgbGlrZSBhIGNoZW1pY2FsIHNwaWxs",
    "RmVhc2libGUgcmh5bWVzIHRoYXQgeW91IGNhbiB2aXNpb24gYW5kIGZlZWw=",
    "Q29uZHVjdGVkIGFuZCBmb3JtZWQsIHRoaXMgaXMgYSBoZWxsIG9mIGEgY29uY2VwdA==",
    "V2UgbWFrZSBpdCBoeXBlIGFuZCB5b3Ugd2FudCB0byBzdGVw",
    "V2l0aCB0aGlzLiBTaGF5IHBsYXlzIG9uIHRoZSBmYWRl",
    "U2xpY2UgbGlrZSBhIG5pbmphLCBjdXQgbGlrZSBhIHJhem9yIGJsYWRl",
    "U28gZmFzdCwgb3RoZXIgREpzIHNheSwgIkRhbW4hIg==",
    "SWYgcmh5bWUgd2FzIGEgZHJ1ZyBJJ2Qgc2VsbCBpdCBieSB0aGUgZ3JhbQ==",
    "S2VlcCBteSBjb21wb3N1cmUgd2hlbiBpdCdzIHRpbWUgdG8gZ2V0IGxvb3Nl",
    "TWFnbmV0aXplZCBieSB0aGUgbWljIHdoaWxlIEkga2ljayBteSBqdWljZQ==",
    "SWYgdGhlcmUgd2FzIGEgcHJvYmxlbSB5byBJJ2xsIHNvbHZlIGl0",
    "Q2hlY2sgb3V0IHRoZSBob29rIHdoaWxlIG15IERKIHJldm9sdmVzIGl0",
    "WW8gbWFuLCBsZXQncyBnZXQgb3V0IG9mIGhlcmU=",
    "V29yZCB0byB5b3VyIG1vdGhlcg==",
]
