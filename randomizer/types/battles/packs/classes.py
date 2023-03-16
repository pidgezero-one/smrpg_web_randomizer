"""Base class for a battle pack, consisting of 3 formations."""

from typing import List
from randomizer.types.numbers.classes import ByteField
from randomizer.types.patch.classes import Patch
from randomizer.types.battles.formations.constants.misc import TOTAL_FORMATIONS
from randomizer.types.battles.packs.constants.misc import PACK_BASE_ADDRESS
from randomizer.types.numbers.classes import UInt16, UInt8


class FormationPack:
    _formation_ids: List[UInt16] = []

    @property
    def formation_ids(self) -> List[UInt16]:
        """A list of all formation IDs included in this battle pack.
        If all three formations are the same, it will just return one ID."""
        if self.formation_ids[0] == self.formation_ids[1] == self.formation_ids[2]:
            return [self.formation_id]
        assert len(self._formation_ids) == 3
        return self._formation_ids

    @property
    def formation_id(self) -> "UInt16":
        """Returns one formation ID. It will fail if all three formation
        IDs are not the same in this pack."""
        assert self.formation_ids[0] == self.formation_ids[1] == self.formation_ids[2]
        return self.formation_ids[0]

    def set_formation_ids(self, *formation_ids: int) -> None:
        """Overwrites the formation IDs in this pack."""
        assert len(formation_ids) == 3
        pids = list(formation_ids)
        for form_id in pids:
            assert form_id < TOTAL_FORMATIONS
        self._formation_ids = [UInt16(id) for id in pids]

    def set_formation_id(self, formation_id: int) -> None:
        """Overwrites all three formation IDs in this pack with the one
        ID given as an argument to this function. In effect, this means
        all three formations will be the same and the pack will always load
        the same battle."""
        assert formation_id < TOTAL_FORMATIONS
        self.set_formation_ids(formation_id, formation_id, formation_id)

    def __init__(self, *formation_ids: int) -> None:
        if len(formation_ids) == 1:
            self.set_formation_ids(formation_ids[0], formation_ids[0], formation_ids[0])
        else:
            self.set_formation_ids(*formation_ids)

    def get_patch(self, pack_index: int) -> Patch:
        """Return the patch for this pack to be written to the ROM."""
        assert UInt8(pack_index)
        assert len(self._formation_ids) == 3

        patch = Patch()
        data = bytearray()
        hi_num = False

        for formation_id in self.formation_ids:
            val = formation_id
            if val > 255:
                hi_num = True
                val -= 256
            data += ByteField(val).as_bytes()

        # High bank indicator.
        val = 7 if hi_num else 0
        data += ByteField(val).as_bytes()

        base_addr = PACK_BASE_ADDRESS + (pack_index * 4)
        patch.add_data(base_addr, data)

        return patch
