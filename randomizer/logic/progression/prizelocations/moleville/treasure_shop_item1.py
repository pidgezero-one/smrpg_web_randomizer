from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_mines, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, TreasureShopLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TreasureShopItem1(TreasureShopLocation, NPCLocationRow1):
    _bias = True
    _originally_held = LuckyJewelPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 110),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(TREASURE_SHOP_ITEM_1_PURCHASED, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]
    _access_conditions = "Requires inner Moleville Mines boss to be defeated"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)

    def render(self, world: GameWorld):
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY):
            world.update_dialog(
                DI2911_TREASURE_SELLER_ITEM_1, f" Item #1: A “Mystery Box”!\n It might be something good. Or, it\n might be empty.[await][page]\n I'll sell it to you for 100 coins.\n  [select] (It's a deal)\n  [select] (I'll pass)[await]"
            )
            return super().render(world)
        assert isinstance(self.prize, StandardPrize)
        assert self.originally_held is not None
        if not isinstance(self.prize, self.originally_held):
            world.update_dialog(
                DI2911_TREASURE_SELLER_ITEM_1, self.prize.nickname.get_slot_1_dialog()
            )
        return super().render(world)


__all__ = ["TreasureShopItem1"]
