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
from randomizer.logic.progression.prizelocations.access import (can_clear_mines)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BucketGirlRewardLocation(NPCLocationRow1):
    _bias = True
    _originally_held = FrogCoin1Prize
    _rooms = [R108_MOLEVILLE_OUTSIDE]
    _id = ShuffleLocationSelector.BUCKET_GIRL
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 116),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["next"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        # If you don't have a carbo cookie and have progressive fireworks turned on, you still need to find a shuffled item. No hint.
        JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        # If you have vanilla fireworks turned on, you can just do the trade sequence.
        JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]),
        # Otherwise, if shuffle one is turned on, you can do the trade sequence if you have any of the three items.
        StoreItemAmountTo7000(FireworksItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        if not can_clear_mines(world, inventory):
            return False
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.PROGRESSIVE):
            return inventory.has_item_count(ProgressiveFireworksPrize, 3)
        if world.settings.is_flag_value(FireworksSetting, FireworksOptions.SHUFFLE_ONE):
            return inventory.has_item(RegularFireworksPrize)
        else:
            return True


__all__ = ["BucketGirlRewardLocation"]
