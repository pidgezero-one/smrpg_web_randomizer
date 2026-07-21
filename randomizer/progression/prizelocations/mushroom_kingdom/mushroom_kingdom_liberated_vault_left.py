from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)


class MushroomKingdomLiberatedVaultLeft(TreasureChestLocationRow1):
    _originally_held = Coins10Prize
    _rooms = [
        R031_MUSHROOM_KINGDOM_CASTLE_VAULT,
    ]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_VAULT_1
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher, InfiniteCoinsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 13),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(NPC_0, R031_MUSHROOM_KINGDOM_CASTLE_VAULT, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]


__all__ = ["MushroomKingdomLiberatedVaultLeft"]
