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
from randomizer.logic.progression.prizelocations.access import (can_do_tower_curtain_game, not_earlygame, is_early_midgame, is_late_midgame, is_lategame)
from randomizer.logic.progression.prizelocations.booster_tower.booster_tower_indoor_boss_fight import (BoosterTowerIndoorBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerIndoorStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R192_BOOSTER_TOWER_9F_AREA_02_BOOSTERS_CURTAIN_GAME_ROOM]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_1
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _parent = BoosterTowerIndoorBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 168),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check____"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check____"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check____"],
            identifier="returned_mario_doll_check____",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check____"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_BOSS_1_STAR_PIECE, ["next"], identifier="tower_boss_2_check____"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_do_tower_curtain_game(world, inventory) and not_earlygame(
            world, inventory
        )


__all__ = ["BoosterTowerIndoorStarPiece"]
