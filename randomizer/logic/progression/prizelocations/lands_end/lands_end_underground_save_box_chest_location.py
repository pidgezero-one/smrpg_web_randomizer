from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_lands_end, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_dodge_lands_end_enemies, can_pass_whirlpools, can_access_temple)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_5)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndUndergroundSaveBoxChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = LandsEndVolcanoStarPrize
    _rooms = [R263_LANDS_END_UNDERGROUND_AREA_01]
    _npc_ids = [NPC_5]
    _id = ShuffleLocationSelector.LANDS_END_STAR_CHEST_1
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = []
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 255),
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
            NPC_5, R263_LANDS_END_UNDERGROUND_AREA_01, ["next"]
        ),
        Jmp(["lands_end_hint_text"]),
    ]
    _access_conditions = "Not a check if \"Shuffle EXP stars\" is turned off."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_pass_whirlpools(world, inventory)


__all__ = ["LandsEndUndergroundSaveBoxChestLocation"]
