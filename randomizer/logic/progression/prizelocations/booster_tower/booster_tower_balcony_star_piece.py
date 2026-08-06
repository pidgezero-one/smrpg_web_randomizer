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
from randomizer.logic.progression.prizelocations.access import (can_access_tower, not_earlygame)
from randomizer.logic.progression.prizelocations.booster_tower.booster_tower_balcony_boss_fight import (BoosterTowerBalconyBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BoosterTowerBalconyStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R202_BOOSTER_TOWER_ENTRANCE]
    _id = ShuffleLocationSelector.BOOSTER_TOWER_STAR_PIECE_2
    _world_area = WorldAreaEnum.BOOSTER_TOWER
    _parent = BoosterTowerBalconyBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 171),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(TOWER_OPENED, ["returned_mario_doll_check______"]),
        JmpIfBitSet(TOWER_CHARACTER_RECRUITED, ["returned_mario_doll_check______"]),
        Jmp(["next"]),
        JmpIfBitClear(
            MARIO_DOLL_SHUFFLE_ENABLED,
            ["tower_boss_2_check______"],
            identifier="returned_mario_doll_check______",
        ),
        JmpIfBitSet(RETURNED_MARIO_DOLL, ["tower_boss_2_check______"]),
        StoreItemAmountTo7000(MarioDollItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            TOWER_BOSS_2_DEFEATED, ["next"], identifier="tower_boss_2_check______"
        ),
        Jmp(["booster_tower_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_tower(world, inventory) and not_earlygame(world, inventory)


__all__ = ["BoosterTowerBalconyStarPiece"]
