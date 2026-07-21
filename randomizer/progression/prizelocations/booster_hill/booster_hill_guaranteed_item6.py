from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_access_hill)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (BoosterHillLocation, ShuffleLocationSelector, StandingLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterHillGuaranteedItem6(BoosterHillLocation, StandingLocation):
    _bias = True
    _70B1_id = 5
    _originally_held = FPFlowerPrize
    _rooms = [R054_BOOSTER_HILL_DUMMY, R014_BOOSTER_HILL]
    _id = ShuffleLocationSelector.BOOSTER_HILL_FLOWER_6
    _world_area = WorldAreaEnum.BOOSTER_HILL
    _designated_packet_ids = [
        P046_BOOSTER_HILL_PRIZE_5,
        P077_BOOSTER_HILL_PRIZE_STANDING_5,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 177),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(BOOSTER_HILL_CLOSED, ["next"]),
        CopyVarToVar(from_var=BOOSTER_HILL_FLOWER_COUNTER, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 6),
        JmpIfComparisonResultIsGreaterOrEqual(["next"]),
        Jmp(["booster_hill_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_hill(world, inventory)


__all__ = ["BoosterHillGuaranteedItem6"]
