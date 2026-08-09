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
from randomizer.logic.progression.prizelocations.access import (can_access_sealed_postgame_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroSealedDoorClearRewardLocationPostgame(KeyItemLocation, NPCLocationRow2):
    _bias = True
    _originally_held = CrystalShardPrize
    _rooms = [R351_CULEXS_ROOM]
    _id = ShuffleLocationSelector.CULEX_POSTGAME_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 300),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["culex_pg_prereq2"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(ExtraShinyStoneItem, identifier="culex_pg_prereq2"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]
    _access_conditions = "Requies the X.ShinyStone. Must first defeat the sealed door boss fight and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_sealed_postgame_boss(world, inventory)


__all__ = ["MonstroSealedDoorClearRewardLocationPostgame"]
