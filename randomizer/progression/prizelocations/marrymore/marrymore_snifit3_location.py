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
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow3, PacketLocation, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreSnifit3Location(KeyItemLocation, NPCLocationRow3, PacketLocation):
    _bias = True
    _originally_held = RingPrize
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER]
    _world_area = WorldAreaEnum.MARRYMORE
    _packet_id = P129_CHAPEL_RING
    _container_event = E0251_NPC_QUEST_3_GRANT
    _id = ShuffleLocationSelector.MARRYMORE_SNIFIT_3
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 198),
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
        JmpIfBitSet(CHAPEL_ITEM_3_RETRIEVED, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_chapel(world, inventory)


__all__ = ["MarrymoreSnifit3Location"]
