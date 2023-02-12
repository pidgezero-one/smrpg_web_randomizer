from randomizer.entities.dialogs.overworld_dialogs.constants.dialog_bank_ids import (
    DIALOG_BANK_22,
)


class DialogBankID(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0x22 <= num <= 0x24
        return super(DialogBankID, cls).__new__(cls, num)


class Dialog:
    _bank: DialogBankID
    _index: int
    _position: int

    @property
    def bank(self) -> DialogBankID:
        return self._bank

    def set_bank(self, bank: DialogBankID) -> None:
        self._bank = bank

    @property
    def index(self) -> int:
        return self._index

    def set_index(self, index: int) -> None:
        self._index = index

    @property
    def position(self) -> int:
        return self._position

    def set_position(self, position: int) -> None:
        self._position = position

    def __init__(self, bank: DialogBankID, index: int, pos: int) -> None:
        self.set_bank(bank)
        self.set_index(index)
        self.set_position(pos)


class DialogCollection:
    _dialogs: List[Dialog]
    _raw_data: List[list[str]]

    @property
    def dialogs(self) -> List[Dialog]:
        return self._dialogs

    def _set_dialogs(self, dialogs: List[Dialog]) -> None:
        assert len(dialogs) == 4096
        self._dialogs = dialogs

    @property
    def raw_data(self) -> List[list[str]]:
        return self._raw_data

    def _set_raw_data(self, raw_data: List[list[str]]) -> None:
        assert len(raw_data) == 3
        self._raw_data = raw_data

    def replace_dialog(self, id: int, content: str):
        dialog = self.dialogs[id]
        raw_index = dialog.bank - DIALOG_BANK_22
        self.raw_data[raw_index][dialog.index] = content

    def search_and_replace_in_all_dialogs(self, search: str, replace: str):
        for bank_index, bank in enumerate(self.raw_data):
            for i, s in enumerate(bank):
                self.raw_data[bank_index][i] = s.replace(search, replace)

    def __init__(self, dialogs: List[Dialog], raw_data: List[list[str]]) -> None:
        self._set_dialogs(dialogs)
        self._set_raw_data(raw_data)
