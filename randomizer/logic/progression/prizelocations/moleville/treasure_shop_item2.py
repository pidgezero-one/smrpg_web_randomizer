from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_mines, can_clear_seaside_boss)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow2, ShuffleLocationSelector, TreasureShopLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TreasureShopItem2(TreasureShopLocation, NPCLocationRow2):
    _bias = True
    _originally_held = ProgressiveEggPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_2
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 111),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(SEASIDE_LIBERATED, ["next"]),
        JmpIfBitSet(TREASURE_SHOP_ITEM_2_PURCHASED, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and can_clear_seaside_boss(
            world, inventory
        )

    def render(self, world: GameWorld):
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY):
            world.update_dialog(
                DI2908_TREASURE_SELLER_ITEM_2, f" Item #2: A “Mystery Box”.\n It might be something good. Or, it\n might be empty.[await][page]\n It's yours for 200 coins.\n  [select] (Okay)\n  [select] (No thanks)[await]"
            )
            return super().render(world)
        assert isinstance(self.prize, StandardPrize)
        assert self.originally_held is not None
        if not isinstance(self.prize, self.originally_held):
            world.update_dialog(
                DI2908_TREASURE_SELLER_ITEM_2, self.prize.nickname.get_slot_2_dialog()
            )
        return super().render(world)


__all__ = ["TreasureShopItem2"]
