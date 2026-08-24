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
from randomizer.logic.progression.prizelocations.access import (can_do_valley_pipes, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class CasinoGrateGuyPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = StarEggPrize
    _rooms = [R092_GRATE_GUYS_CASINO_INSIDE_CASINO]
    _id = ShuffleLocationSelector.CASINO_GRATE_GUY_PRIZE
    _world_area = WorldAreaEnum.CASINO
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 338),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(CASINO_PRIZE_WON, ["next"]),
        StoreItemAmountTo7000(BrightCardItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(MAP_CASINO, ["bean_valley_hint_text"]),
        Jmp(["casino_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(BrightCardPrize) and can_do_valley_pipes(world, inventory)


__all__ = ["CasinoGrateGuyPrizeLocation"]
