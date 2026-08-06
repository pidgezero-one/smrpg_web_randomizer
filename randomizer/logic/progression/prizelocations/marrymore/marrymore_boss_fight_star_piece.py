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
from randomizer.logic.progression.prizelocations.access import (can_clear_chapel)
from randomizer.logic.progression.prizelocations.marrymore.marrymore_boss_fight import (MarrymoreBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MarrymoreBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER, R294_UNMAPPED_HOUSE_ROOM]
    _id = ShuffleLocationSelector.MARRYMORE_STAR_PIECE
    _world_area = WorldAreaEnum.MARRYMORE
    _parent = MarrymoreBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 200),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(MARRYMORE_BACKDOOR_OPEN, ["next"]),
        JmpIfBitClear(CHAPEL_ITEMS_ANYWHERE_ENABLED, ["marrymore_hint_text"]),
        StoreItemAmountTo7000(RingItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(CrownItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(ShoesItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(BroochItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_chapel(world, inventory)


__all__ = ["MarrymoreBossFightStarPiece"]
