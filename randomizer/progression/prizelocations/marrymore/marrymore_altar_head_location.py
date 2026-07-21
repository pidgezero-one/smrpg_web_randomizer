from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_chapel)
from randomizer.types.logic import (Inventory)
from randomizer.types.packet_type import (PacketType)
from randomizer.types.prizelocation import (KeyItemLocation, PacketLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreAltarHeadLocation(KeyItemLocation, PacketLocationRow1):
    _bias = True
    _originally_held = CrownPrize
    _replace = "spawn_chapel_crown_item"
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _world_area = WorldAreaEnum.MARRYMORE
    _packet_type = PacketType.STATIC
    _packet_id = P130_CHAPEL_CROWN
    _id = ShuffleLocationSelector.MARRYMORE_ALTAR
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 199),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitSet(CROWN_COLLECTED, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)


__all__ = ["MarrymoreAltarHeadLocation"]
