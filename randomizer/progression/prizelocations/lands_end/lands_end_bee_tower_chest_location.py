from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndBeeTowerChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R141_LANDS_END_AREA_04_ROTATING_FLOWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LNDS_END_BEE_ROOM
    _world_area = WorldAreaEnum.LANDS_END
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 250),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6, R141_LANDS_END_AREA_04_ROTATING_FLOWERS, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)


__all__ = ["LandsEndBeeTowerChestLocation"]
