"""Base classes related to dialogs and dialog collections"""

from typing import List

from .ids import (
    DIALOG_BANK_22,
)
from .ids.types import DialogBankID


class Dialog:
    """An individual dialog in the overworld"""

    _bank: DialogBankID
    _index: int
    _position: int

    @property
    def bank(self) -> DialogBankID:
        """The bank that this dialog belongs to"""
        return self._bank

    @property
    def index(self) -> int:
        """The index of the dialog"""
        return self._index

    @property
    def position(self) -> int:
        """The starting position within the raw text where this dialog begins"""
        return self._position

    def set_position(self, position: int) -> None:
        """Overwrite the starting position within the raw text where this dialog begins"""
        self._position = position

    def __init__(self, bank: DialogBankID, index: int, pos: int) -> None:
        self._bank = bank
        self._index = index
        self.set_position(pos)


class DialogCollection:
    """Houses all dialog banks to allow retrieval and manipulation of any dialog."""

    _dialogs: List[Dialog]
    _raw_data: List[list[str]]

    @property
    def dialogs(self) -> List[Dialog]:
        """The dialogs belonging to this seed."""
        return self._dialogs

    def _set_dialogs(self, dialogs: List[Dialog]) -> None:
        """Overwrite the dialogs belonging to this seed."""
        assert len(dialogs) == 4096
        self._dialogs = dialogs

    @property
    def raw_data(self) -> List[list[str]]:
        """The raw string data comprising dialogs."""
        return self._raw_data

    def _set_raw_data(self, raw_data: List[list[str]]) -> None:
        """Overwrite the raw string data comprising dialogs."""
        assert len(raw_data) == 3
        self._raw_data = raw_data

    def replace_dialog(self, identifier: int, content: str):
        """Replace a whole dialog by its unique ID."""
        dialog = self.dialogs[identifier]
        raw_index = dialog.bank - DIALOG_BANK_22
        self.raw_data[raw_index][dialog.index] = content

    def search_and_replace_in_all_dialogs(self, search: str, replace: str):
        """Replace all instances of the substring across all dialogs."""
        for bank_index, bank in enumerate(self.raw_data):
            for index, string in enumerate(bank):
                self.raw_data[bank_index][index] = string.replace(search, replace)

    def __init__(self, dialogs: List[Dialog], raw_data: List[list[str]]) -> None:
        self._set_dialogs(dialogs)
        self._set_raw_data(raw_data)
