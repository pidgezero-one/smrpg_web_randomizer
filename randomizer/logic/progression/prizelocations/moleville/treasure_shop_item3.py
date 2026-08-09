from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_mines, can_clear_volcano)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow3, ShuffleLocationSelector, TreasureShopLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class TreasureShopItem3(TreasureShopLocation, NPCLocationRow3):
    _bias = True
    _originally_held = FryingPanPrize
    _rooms = [R336_MOLEVILLE_ITEM_SHOP]
    _id = ShuffleLocationSelector.TREASURE_SELLER_3
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 112),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(VOLCANO_LIBERATED, ["next"]),
        JmpIfBitSet(TREASURE_SHOP_ITEM_3_PURCHASED, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]
    _access_conditions = "Requires inner Moleville Mines and Barrel Volcano bosses to be defeated"

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory) and can_clear_volcano(world, inventory)

    def render(self, world: GameWorld):
        if world.settings.is_flag_value(ItemQuality, ItemQualityOptions.COMPLETELY_EMPTY):
            world.update_dialog(
                DI2914_TREASURE_SELLER_ITEM_3, f" Item #3: A “Mystery Box”.\n It might be something good. Or, it\n might be empty.[await][page]\n I'll sell it for 300 coins.\n  [select] (I'll take it)\n  [select] (No thanks)[await]"
            )
            return super().render(world)
        assert isinstance(self.prize, StandardPrize)
        assert self.originally_held is not None
        if not isinstance(self.prize, self.originally_held):
            world.update_dialog(
                DI2914_TREASURE_SELLER_ITEM_3, self.prize.nickname.get_slot_3_dialog()
            )
        return super().render(world)


__all__ = ["TreasureShopItem3"]
