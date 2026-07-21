from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (not_earlygame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BeanValleyBossNoteLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = SeedPrize
    _rooms = [R254_BEAN_VALLEY_SMILAX_AREA]
    _id = ShuffleLocationSelector.BEAN_VALLEY_MEGASMILAX_ROOM
    _world_area = WorldAreaEnum.BEAN_VALLEY
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 315),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(BEAN_VALLEY_BOSS_DEFEATED, ["next"]),
        JmpIfBitSet(SEED_CHECKED, ["next"]),
        Jmp(["bean_valley_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return not_earlygame(world, inventory)


__all__ = ["BeanValleyBossNoteLocation"]
