from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_access_fifth_dojo_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow2, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroDojoPostgameClearRewardLocation(NPCLocationRow2):
    _bias = True
    _originally_held = TeamworkBandPrize
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME_REWARD
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _remake_only = True
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 296),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitSet(DOJO_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["monstro_town_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_fifth_dojo_boss(world, inventory)


__all__ = ["MonstroDojoPostgameClearRewardLocation"]
