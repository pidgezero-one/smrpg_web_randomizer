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
from randomizer.logic.progression.prizelocations.access import (can_clear_temple_boss, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_dodge_lands_end_enemies, can_pass_whirlpools, can_access_temple)
from randomizer.logic.progression.prizelocations.lands_end.temple_boss_fight import (TempleBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TempleBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R268_BELOME_TEMPLE_AREA_08_BELOMES_ROOM]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_BOSS
    _world_area = WorldAreaEnum.TEMPLE
    _parent = TempleBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 284),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfBitSet(TEMPLE_BOSS_DEFEATED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_GATED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_clear_temple_boss(
            world, inventory
        )


__all__ = ["TempleBossFightStarPiece"]
