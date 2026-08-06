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
from randomizer.logic.progression.prizelocations.access import (can_access_nimbus_castle, not_earlygame)
from randomizer.logic.progression.prizelocations.nimbus_land.statue_room_boss_fight import (StatueRoomBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class StatueRoomStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _override_id = 520
    _id = ShuffleLocationSelector.NIMBUS_LAND_STAR_PIECE_1
    _world_area = WorldAreaEnum.NIMBUS_LAND
    _parent = StatueRoomBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 344),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(STATUE_KEEPER_STAR_PIECE, ["next"]),
        JmpIfBitClear(NIMBUS_MAINLAND_UNLOCKED, ["next"]),
        JmpIfBitSet(STATUE_GAME_DONE, ["nimbus_castle_hint_text"]),
        JmpIfBitClear(PAINT_GATING, ["nimbus_castle_hint_text"]),
        StoreItemAmountTo7000(GoldPaintItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["nimbus_land_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        boss_condition = world.settings.isflag_enabled(
            SkipBossFights
        ) or not_earlygame(world, inventory)
        return (
            super().can_access(inventory, world)
            and can_access_nimbus_castle(world, inventory)
            and boss_condition
        )


__all__ = ["StatueRoomStarPiece"]
