from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_19)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndCaveSideRemake(StandingLocationRow1):
    _bias = True
    _originally_held = FlowerTabPrize
    _rooms = [R142_LANDS_END_AREA_05_SKY_BRIDGE]
    _world_area = WorldAreaEnum.LANDS_END
    _npc_ids = [NPC_19]
    _remake_only = True
    _id = ShuffleLocationSelector.LANDS_END_CAVE_SIDE_REMAKE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 251),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_19, R142_LANDS_END_AREA_05_SKY_BRIDGE, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and world.settings.is_flag_value(
            Remake, True
        )


__all__ = ["LandsEndCaveSideRemake"]
