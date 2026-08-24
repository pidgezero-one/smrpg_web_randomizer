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
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_6)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndGrottoEndChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = RecoveryMushroomPrize
    _rooms = [R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_6]
    _id = ShuffleLocationSelector.LANDS_END_SHY_AWAY
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [EXPStarPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 254),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(LANDS_END_GATED, ["lands_end_grotto_end_chest_sewers_closed"]),
        JmpIfBitSet(SEWERS_CLOSED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_6,
            R401_LANDS_END_SECRET_UNDERGROUND_AREA_02_LEADS_TO_KERO_SEWERS,
            ["next"],
            identifier="lands_end_grotto_end_chest_sewers_closed",
        ),
        Jmp(["lands_end_grotto_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple(world, inventory)


__all__ = ["LandsEndGrottoEndChestLocation"]
