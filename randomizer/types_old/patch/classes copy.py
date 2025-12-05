"""Base classes supporting the production of a ROM patch."""

from typing import Dict, List, Union


class Patch:
    """Class representing a patch for a specific seed that can be added to as we build it."""

    def __init__(self):
        self._data = {}

    def __add__(self, other: "Patch") -> "Patch":
        """Add another patch to this patch and return a new Patch object."""

        patch = Patch()
        patch += self
        patch += other
        return patch

    def __iadd__(self, other: "Patch") -> "Patch":
        """Add another patch to this patch in place."""

        for addr in other.addresses:
            self.add_data(addr, other.get_data(addr))

        return self

    @property
    def addresses(self) -> List[int]:
        """A list of all addresses in the patch."""
        return list(self._data.keys())

    def get_data(self, addr: int) -> Union[bytearray, bytes, List[int]]:
        """Get data in the patch for this address.
        If the address is not present in the patch, returns empty bytes."""
        return self._data.get(addr, bytes())

    def add_data(
        self, addr: int, data: Union[bytearray, bytes, List[int], int, str]
    ) -> None:
        """Add data to the patch."""
        # For integers and strings, convert them to byte representations.
        if isinstance(data, int) and data <= 0xFF:
            data = data.to_bytes(1, "little")
        elif isinstance(data, str):
            data = data.encode("latin1")
        self._data[addr] = data

    def remove_data(self, addr: int) -> None:
        """Remove data from the patch."""
        if addr in self._data:
            del self._data[addr]

    def for_json(self) -> List[Dict[int, bytes]]:
        """Return patch as a JSON serializable object."""
        patch = []
        addrs = list(self._data.keys())
        addrs.sort()

        for addr in addrs:
            patch.append({addr: self._data[addr]})

        return patch
