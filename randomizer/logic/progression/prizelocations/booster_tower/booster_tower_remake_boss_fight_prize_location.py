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
from randomizer.logic.progression.prizelocations.access import (can_access_tower_postgame_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerRemakeBossFightPrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = Stella023Prize
    _rooms = [R199_BOOSTER_TOWER_9F_AREA_01_THREE_YELLOW_PLATFORMS_WSAVE_POINT]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_POSTGAME_DROP
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _remake_only = True
    _monstro_shuffle = True
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 170),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check_______"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check_______"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check_______"],
            identifier="returned_mario_doll_check_______",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check_______"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        JmpIfBitClear(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check_______"
        ),
        JmpIfBitSet(STAY_VOUCHER_USED, ["___tower_postgame_completed_check"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
        JmpIfBitSet(
            POSTGAME_TOWER_COMPLETED,
            ["next"],
            identifier="___tower_postgame_completed_check",
        ),
        Jmp(["booster_tower_hint_text"]),
    ]
    _access_conditions = "Must first defeat the boss fight in the Booster Tower curtain room and use the Stay Voucher. Not a check if \"Enable Remake content\" is turned off."


    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower_postgame_boss(world, inventory)


__all__ = ["BoosterTowerRemakeBossFightPrizeLocation"]
