from functools import singledispatchmethod
from rich import print, box
from rich.table import Table, Column
from typing import Dict, Tuple, List, Union

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
        UI.table_view(data = {"Hex": (data.hex(" "), width*3), "ASCII": (data, width)})

    @staticmethod
    def table_view(data: Dict[str, Union[str, bytes]], widths = List[int]) -> None:
        print(max(map(len, (*data.values()))))
        table = Table(
            *(
                Column(h, width=w if w is not None else max(map(len, data.values())), overflow="fold")
                for h, w in zip(data.keys(), widths)
            ),
            box=box.SIMPLE
        )

        for (r, w) in zip(zip(*data.values()), widths):
            row = (UI.sanitize(c) for c in r)
            row = (UI.hard_wrap(c, w) if w is not None else c for c in row)
            table.add_row(*row)

        print(table)
    
    @staticmethod
    def grid_view(data: List[List[str]]) -> None:
        grid = Table.grid(padding=(0, 1), pad_edge=True)
        for r in zip(*data):
            grid.add_row(*r)

        print(grid)
