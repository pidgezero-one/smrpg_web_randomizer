from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_lands_end)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (FPFlowerPrize, SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow1, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_7)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class LandsEndGrottoEntranceChestLocation(TreasureChestLocationRow1):
    _bias = True
    _originally_held = FPFlowerPrize
    _rooms = [R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS]
    _npc_ids = [NPC_7]
    _id = ShuffleLocationSelector.LANDS_END_SECRET_1
    _world_area = WorldAreaEnum.LANDS_END
    _blacklist = [SlotsPrize]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 252),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_7,
            R270_LANDS_END_SECRET_UNDERGROUND_AREA_01_LEADS_TO_KERO_SEWERS,
            ["next"],
        ),
        Jmp(["lands_end_grotto_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_lands_end(world, inventory)


__all__ = ["LandsEndGrottoEntranceChestLocation"]
