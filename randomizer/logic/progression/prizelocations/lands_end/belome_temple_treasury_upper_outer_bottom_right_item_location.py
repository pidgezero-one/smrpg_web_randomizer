from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.data.physical_objects.items import (DefaultItem, FlowerObject, FrogCoinObject, RecoveryMushroomObject, SmallFrogCoinObject)
from randomizer.data.variables.variable_names import (PRIMARY_TEMP_7000)
from randomizer.logic.progression.prizelocations.access import (can_access_lands_end, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame, can_dodge_lands_end_enemies, can_pass_whirlpools, can_access_temple)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StandingLocationRow15, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_14)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class BelomeTempleTreasuryUpperOuterBottomRightItemLocation(StandingLocationRow15):
    _bias = True
    _originally_held = FireBombPrize
    _rooms = [R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM]
    _npc_ids = [NPC_14]
    _id = ShuffleLocationSelector.BELOME_TEMPLE_TREASURE_3
    _world_area = WorldAreaEnum.TEMPLE
    _model_allowlist = [
        DefaultItem,
        FrogCoinItemObject,
        FrogCoinObject,
        SmallFrogCoinObject,
        FlowerItemObject,
        RecoveryMushroomObject,
        CoinStillObject,
        FlowerObject,
        SmallCoinItemObject,
        SmallCoinStillObject,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 283),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(LANDS_END_GATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_14, R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM, ["next"]
        ),
        JmpIfBitSet(TEMPLE_KEY_USED, ["belome_temple_hint_text"]),
        StoreItemAmountTo7000(TempleKeyItem),
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["belome_temple_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_temple(world, inventory) and inventory.has_item(
            TempleKeyPrize
        )


__all__ = ["BelomeTempleTreasuryUpperOuterBottomRightItemLocation"]
