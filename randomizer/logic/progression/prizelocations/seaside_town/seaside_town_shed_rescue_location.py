from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_access_seaside_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class SeasideTownShedRescueLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FlowerBoxPrize
    _rooms = [R314_SEASIDE_TOWN_SHED]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_RESCUE
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 212),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(SEASIDE_SHED_EMPTIED, ["next"]),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_6,
            R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            ["seaside_town_hint_text"],
        ),
        StoreItemAmountTo7000(ShedKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["seaside_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_seaside_boss(world, inventory) and inventory.has_item(
            ShedKeyPrize
        )


__all__ = ["SeasideTownShedRescueLocation"]
