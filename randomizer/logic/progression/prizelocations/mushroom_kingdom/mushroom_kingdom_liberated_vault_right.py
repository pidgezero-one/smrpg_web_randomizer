from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)


class MushroomKingdomLiberatedVaultRight(TreasureChestLocationRow2):
    _originally_held = RecoveryMushroomPrize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
    ]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher, InfiniteCoinsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 14),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(NPC_1, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]


__all__ = ["MushroomKingdomLiberatedVaultRight"]
