from typing import Any
from django.core.serializers.json import DjangoJSONEncoder
from smrpgpatchbuilder.datatypes.allies.ally import Ally


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
    def addresses(self) -> list[int]:
        """A list of all addresses in the patch."""
        return list(self._data.keys())

    def get_data(self, addr: int) -> bytearray | bytes | list[int]:
        """Get data in the patch for this address.
        If the address is not present in the patch, returns empty bytes."""
        return self._data.get(addr, bytes())

    def add_data(
        self, addr: int, data: bytearray | bytes | list[int] | int | str, source: str = ""
    ) -> None:
        """Add data to the patch."""
        # For integers and strings, convert them to byte representations.
        if isinstance(data, int) and data <= 0xFF:
            data = data.to_bytes(1, "little")
        elif isinstance(data, str):
            data = data.encode("latin1")

        # Check for overlaps with existing data
        new_start = addr
        new_end = addr + len(data)
        for existing_addr, existing_data in self._data.items():
            existing_end = existing_addr + len(existing_data)
            # Check if ranges overlap
            if new_start < existing_end and existing_addr < new_end:
                print(f"⚠️  OVERLAP DETECTED!")
                print(f"    New data: 0x{new_start:06X}-0x{new_end:06X} ({len(data)} bytes) {source}")
                print(f"    Existing: 0x{existing_addr:06X}-0x{existing_end:06X} ({len(existing_data)} bytes)")

        self._data[addr] = data

    def add_dict(self, data: dict[int, bytearray], source: str = "") -> None:
        """Add data to the patch in `{0x123456: bytearray([0x00])}` format."""
        for addr, b in data.items():
            self.add_data(addr, b, source)

    def remove_data(self, addr: int) -> None:
        """Remove data from the patch."""
        if addr in self._data:
            del self._data[addr]

    def for_json(self) -> list[dict[int, bytes]]:
        """Return patch as a JSON serializable object."""
        patch = []
        addrs = list(self._data.keys())
        addrs.sort()

        for addr in addrs:
            patch.append({addr: self._data[addr]})

        return patch


class PatchJSONEncoder(DjangoJSONEncoder):
    """Extension of the Django JSON serializer to support randomizer patch data."""

    def default(self, o: Any):
        # Support bytes and bytearray objects, which are just lists of integers.
        if isinstance(o, (bytearray, bytes)):
            return list(o)
        if isinstance(o, Patch):
            return o.for_json()
        if isinstance(o, Ally):
            return o.name
        return super().default(o)
