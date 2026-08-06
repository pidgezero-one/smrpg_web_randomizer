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
from randomizer.logic.progression.prizelocations.access import (can_clear_forest, can_clear_mines)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (SlotsPrize)
from randomizer.types.prizelocation import (ShuffleLocationSelector, TreasureChestLocationRow2, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class RoseTownCloudLeftChestLocation(TreasureChestLocationRow2):
    _bias = True
    _originally_held = LazyShellWeaponPrize
    _rooms = [R419_LAZY_SHELL_CLOUD]
    _npc_ids = [NPC_1]
    _id = ShuffleLocationSelector.GARDENER_CLOUD_2
    _world_area = WorldAreaEnum.ROSE_TOWN
    _blacklist = [EXPStarPrize, SlotsPrize]
    _monstro_shuffle = True
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 72),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1, R419_LAZY_SHELL_CLOUD, ["next"]
        ),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(FOREST_LIBERATED, ["next"]),
        JmpIfBitSet(GAVE_SEED_AND_FERTILIZER, ["rose_town_hint_text"]),
        JmpIfBitSet(GAVE_SEED, ["hint_check_fertilizer2"]),
        StoreItemAmountTo7000(SeedItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        JmpIfBitSet(
            GAVE_FERTILIZER,
            ["rose_town_hint_text"],
            identifier="hint_check_fertilizer2",
        ),
        StoreItemAmountTo7000(FertilizerItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["rose_town_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            inventory.has_item(SeedPrize)
            and inventory.has_item(FertilizerPrize)
            and can_clear_mines(world, inventory)
            and can_clear_forest(world, inventory)
        )


__all__ = ["RoseTownCloudLeftChestLocation"]
