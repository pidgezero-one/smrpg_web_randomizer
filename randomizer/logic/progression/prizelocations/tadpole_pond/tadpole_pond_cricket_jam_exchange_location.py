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
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TadpolePondCricketJamExchangeLocation(NPCLocationRow2):
    _bias = True
    _originally_held = FrogCoin10Prize
    _rooms = [R075_TADPOLE_POND_AREA_01]
    _id = ShuffleLocationSelector.CRICKET_JAM_REWARD
    _world_area = WorldAreaEnum.TADPOLE_POND
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 52),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(CRICKET_PIE_EXCHANGED, ["next"]),
        JmpIfBitSet(CRICKET_JAM_EXCHANGED, ["next"]),
        StoreItemAmountTo7000(CricketJamItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["tadpole_pond_hint_text"]),
    ]
    _access_conditions = "Requires the Cricket Pie to be exchanged first."

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return inventory.has_item(CricketPiePrize) and inventory.has_item(
            CricketJamPrize
        )


__all__ = ["TadpolePondCricketJamExchangeLocation"]
