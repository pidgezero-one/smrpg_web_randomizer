from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_temple_boss, can_access_lands_end, can_access_monstro_town, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_dodge_lands_end_enemies, can_pass_whirlpools, can_access_temple)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TroopaClimbSub12PrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = TroopaPinPrize
    _rooms = [R407_LANDS_END_CLIFF_CLIMB_WSKY_TROOPAS]
    _id = ShuffleLocationSelector.TROOPA_CLIMB
    _world_area = WorldAreaEnum.LANDS_END
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 258),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitSet(TROOPA_CLIMB_COMPLETED, ["next"]),
        Jmp(["lands_end_hint_text"]),
    ]
    _access_conditions = "Requires the Belome Temple boss to be defeated and Monstro Town to be unlocked"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory) and can_access_monstro_town(
            world, inventory
        ) and can_clear_temple_boss(world, inventory)


__all__ = ["TroopaClimbSub12PrizeLocation"]
