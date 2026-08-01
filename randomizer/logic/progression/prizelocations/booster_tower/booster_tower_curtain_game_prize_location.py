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
from randomizer.logic.progression.prizelocations.access import (can_do_tower_curtain_game)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerCurtainGamePrizeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = AmuletPrize
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_CURTAIN_GAME
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _blacklist = [RecoveryMushroomPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 166),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check__"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check__"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check__"],
            identifier="returned_mario_doll_check__",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check__"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check__"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory)


__all__ = ["BoosterTowerCurtainGamePrizeLocation"]
