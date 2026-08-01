from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_forest)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class RoseTownInnGazPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FingerShotPrize
    _rooms = [R086_ROSE_TOWN_INN_1F]
    _id = ShuffleLocationSelector.GAZ
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 74),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(ROSE_TOWN_GAZ_ITEM_GRANTED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory)


__all__ = ["RoseTownInnGazPrizeLocation"]
