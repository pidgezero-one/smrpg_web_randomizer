from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_monstro_town)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroSecondSuperJumpRewardLocation(NPCLocationRow2):
    _bias = True
    _originally_held = SuperSuitPrize
    _rooms = [R397_MONSTRO_TOWN_SUPERJUMPING_ROOM]
    _id = ShuffleLocationSelector.SUPER_JUMPS_100
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 302),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitSet(SUPER_JUMP_PRIZE_2_GRANTED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        Jmp(["super_jump_hint_text"]),
    ]
    _access_conditions = "Not a check if none of your characters learn Super Jump."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_monstro_town(world, inventory) and inventory.has_item(
            SuperJumpSpellPrize
        )


__all__ = ["MonstroSecondSuperJumpRewardLocation"]
