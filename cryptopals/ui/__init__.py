from functools import singledispatchmethod
from rich import print, box
from rich.table import Table, Column

import re


class UI:
    """
    Class holding methods for generating and displaying UI.
    """

    @staticmethod
    def hard_wrap(string: str, width: int) -> str:
        """
        Wrap a string to a given width.
        """
        return "\n".join([string[n : n + width] for n in range(0, len(string), width)])

    @singledispatchmethod
    @staticmethod
    def sanitize(data):
        """
        Sanitize data by replacing non-printable characters with '?'.
        """
        raise NotImplementedError

    @sanitize.register
    @staticmethod
    def sanitize_bytes(data: bytes):
        _data = data.decode("ascii", errors="replace")
        return UI.sanitize(_data)
    
    @sanitize.register
    @staticmethod
    def sanitize_str(data: str):
        return re.sub(r"[^\x20-\x7e]", "?", data)

    @staticmethod
    def hex_view(data: bytes, width=16) -> None:
        """
        View the hex and utf-8 representation of a byte string as a table.
        """
        hex = "\n".join(
            data[n : n + width].hex(" ")
            for n in range(0, len(data), width)
        )
        utf8 = UI.hard_wrap(UI.sanitize(data.decode("utf-8", errors="replace")), width)

        UI.table_view(data = {"Hex": (hex, width*3), "UTF-8": (utf8, width)})

    @staticmethod
    def table_view(data: dict[str, tuple[str, int]]) -> None:
        table = Table(
            *(
                Column(h, width=w, overflow="fold")
                for h, (_, w) in data.items()
            ),
            box=box.SIMPLE
        )

        table.add_row(*(v for v, _ in data.values()))

        print(table)
