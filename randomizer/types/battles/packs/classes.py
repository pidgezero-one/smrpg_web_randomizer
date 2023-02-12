from typing import List
from randomizer.types.numbers.classes import ByteField
from randomizer.types.patch.classes import Patch
from randomizer.types.battles.formations.constants.misc import TOTAL_FORMATIONS
from randomizer.types.battles.packs.constants.misc import PACK_BASE_ADDRESS, TOTAL_PACKS
from randomizer.types.numbers.classes import UInt16, UInt8


class FormationPack:
    _formation_ids: List[UInt16] = []

    @property
    def formation_ids(self) -> List[UInt16]:
        if self.formation_ids[0] == self.formation_ids[1] == self.formation_ids[2]:
            return [self.formation_id]
        assert len(self._formation_ids) == 3
        return self._formation_ids

    @property
    def formation_id(self) -> "UInt16":
        assert self.formation_ids[0] == self.formation_ids[1] == self.formation_ids[2]
        return self.formation_ids[0]

    def set_formation_ids(self, *formation_ids: int) -> None:
        assert len(formation_ids) == 3
        pids = list(formation_ids)
        for id in pids:
            assert id < TOTAL_FORMATIONS
        self._formation_ids = [UInt16(id) for id in pids]

    def set_formation_id(self, formation_id: int) -> None:
        assert formation_id < TOTAL_FORMATIONS
        self.set_formation_ids(formation_id, formation_id, formation_id)

    def __init__(self, *formation_ids: int) -> None:
        if len(formation_ids) == 1:
            self.set_formation_ids(formation_ids[0], formation_ids[0], formation_ids[0])
        else:
            self.set_formation_ids(*formation_ids)

    def get_patch(self, pack_index: int) -> Patch:
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
