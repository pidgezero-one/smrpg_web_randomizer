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
from randomizer.logic.progression.prizelocations.access import (can_access_inner_mines)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class InnerMinesTracksChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = MolevilleMinesStarPrize
    _rooms = [R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM]
    _npc_ids = [NPC_0]
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_STAR_CHEST
    _world_area = WorldAreaEnum.MOLEVILLE
    _blacklist = [ThirdMimicFightLauncher, SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 122),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0, R285_MOLEVILLE_MINES_AREA_13_LONG_MINECART_TRACKS_ROOM, ["next"]
        ),
        JmpIfBitSet(MINES_BACK_OPENED, ["mines_hint_text"]),
        StoreItemAmountTo7000(BambinoBombItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["mines_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_inner_mines(world, inventory)


__all__ = ["InnerMinesTracksChestLocation"]
