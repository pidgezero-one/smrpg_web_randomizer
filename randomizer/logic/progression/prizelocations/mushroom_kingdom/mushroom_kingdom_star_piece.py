from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_bandits_way)
from randomizer.logic.progression.prizelocations.mushroom_kingdom.mushroom_kingdom_boss_fight import (MushroomKingdomBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece1
    _rooms = [R018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_STAR_PIECE
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _parent = MushroomKingdomBossFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 26),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(BANDITS_WAY_LIBERATED, ["next"]),
        JmpIfBitSet(MUSHROOM_KINGDOM_LIBERATED, ["next"]),
        Jmp(["mushroom_kingdom_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_bandits_way(
            world, inventory
        )


__all__ = ["MushroomKingdomStarPiece"]
