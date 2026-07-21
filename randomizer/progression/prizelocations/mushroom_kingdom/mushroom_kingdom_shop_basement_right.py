from __future__ import annotations
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.types.prize import (FPFlowerPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)


class MushroomKingdomShopBasementRight(TreasureChestLocationRow2):
    _originally_held = FPFlowerPrize
    _rooms = [R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.MUSHROOM_KINGDOM_STORE_BASEMENT_2
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _blacklist = [EXPStarPrize, SecondMimicFightLauncher, ThirdMimicFightLauncher]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 19),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT, ["next"]
        ),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]


__all__ = ["MushroomKingdomShopBasementRight"]
