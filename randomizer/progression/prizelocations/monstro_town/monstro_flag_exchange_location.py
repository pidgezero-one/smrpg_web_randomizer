from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.progression.prizelocations.access import (can_access_monstro_town)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroFlagExchangeLocation(NPCLocationRow1):
    _bias = True
    _originally_held = GhostMedalPrize
    _rooms = [R399_MONSTRO_TOWN_3_MUSTY_FEARS_INN]
    _id = ShuffleLocationSelector.THREE_MUSTY_FEARS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 303),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitSet(MUSTY_FEARS_QUEST_COMPLETE, ["next"]),
        StoreItemAmountTo7000(DryBonesFlagItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(BigBooFlagItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        StoreItemAmountTo7000(GreaperFlagItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["monstro_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_monstro_town(world, inventory)
            and inventory.has_item(DryBonesFlagPrize)
            and inventory.has_item(GreaperFlagPrize)
            and inventory.has_item(BigBooFlagPrize)
        )


__all__ = ["MonstroFlagExchangeLocation"]
