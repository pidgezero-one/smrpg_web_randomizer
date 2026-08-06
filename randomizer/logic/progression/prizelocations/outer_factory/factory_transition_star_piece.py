from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_factory, not_earlygame)
from randomizer.logic.progression.prizelocations.outer_factory.factory_transition_boss_fight import (FactoryTransitionBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FactoryTransitionStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM]
    _id = ShuffleLocationSelector.FACTORY_BOSS_2
    _world_area = WorldAreaEnum.FACTORY
    _parent = FactoryTransitionBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 433),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MAP_GATE, ["next"]),
        JmpIfBitSet(ABYSS_BOSS_2_DEFEATED, ["next"]),
        Jmp(["factory_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_factory(world, inventory)
            and not_earlygame(world, inventory)
        )


__all__ = ["FactoryTransitionStarPiece"]
