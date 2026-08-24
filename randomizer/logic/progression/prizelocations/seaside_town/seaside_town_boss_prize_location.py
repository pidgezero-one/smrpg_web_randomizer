from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_seaside_boss, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, ShuffleLocationSelector, StandingLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class SeasideTownBossPrizeLocation(KeyItemLocation, StandingLocationRow1):
    _bias = True
    _originally_held = ShedKeyPrize
    _rooms = [R316_SEASIDE_TOWN_BEACH]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.SEASIDE_TOWN_BOSS_PRIZE
    _world_area = WorldAreaEnum.SEASIDE_TOWN
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 211),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(SEASIDE_BOSS_AVAILABLE, ["next"]),
        JmpIfBitClear(SEASIDE_LIBERATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_0, R316_SEASIDE_TOWN_BEACH, ["next"]
        ),
        Jmp(["seaside_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_seaside_boss(world, inventory)


__all__ = ["SeasideTownBossPrizeLocation"]
