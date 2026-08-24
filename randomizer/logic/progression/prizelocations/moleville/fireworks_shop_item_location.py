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
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow1, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FireworksShopItemLocation(KeyItemLocation, NPCLocationRow1):
    _bias = True
    _originally_held = RegularFireworksPrize
    _rooms = [R339_MOLEVILLE_FIREWORKS_SHOP]
    _id = ShuffleLocationSelector.FIREWORKS_SHOP
    _world_area = WorldAreaEnum.MOLEVILLE
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 113),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(FIREWORKS_HOUSE_ITEM_SOLD, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]
    _access_conditions = "Requires the inner Moleville Mines boss to be defeated. Only a check if \"Progressive Fireworks\" or \"Shuffle One Fireworks\" is enabled"

    def key(self, world: GameWorld) -> bool:
        return not world.settings.is_flag_value(
            FireworksSetting, FireworksOptions.VANILLA
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_mines(world, inventory)


__all__ = ["FireworksShopItemLocation"]
