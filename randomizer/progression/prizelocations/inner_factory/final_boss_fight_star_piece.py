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
from randomizer.progression.prizelocations.access import (can_access_inner_factory_final_boss, not_earlygame)
from randomizer.progression.prizelocations.inner_factory.final_boss_fight import (FinalBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_14)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class FinalBossFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = StarPiece7
    _id = ShuffleLocationSelector.INNER_FACTORY_BOSS_FINAL
    _world_area = WorldAreaEnum.INNER_FACTORY
    _parent = FinalBossFight
    _rooms = [
        R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM,
        R108_MOLEVILLE_OUTSIDE,
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 439),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(FACTORY_BOSS_DEFEATED, ["next"]),
        JmpIfObjectNotInSpecificLevel(
            NPC_14, R470_FACTORY_GROUNDS_AREA_04_GUN_YOLKS_ROOM, ["next"]
        ),
        JmpIfBitSet(MAP_GATE, ["factory_hint_text"]),
        JmpIfBitClear(CASINO_WARP_ENABLED, ["check_bucket_warp"]),
        StoreItemAmountTo7000(BrightCardItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["check_bucket_warp"]),
        JmpIfBitClear(MAP_CASINO, ["bean_valley_hint_text"]),
        Jmp(["casino_hint_text"]),
        JmpIfBitClear(BUCKET_WARP_ENABLED, ["next"], identifier="check_bucket_warp"),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitSet(CARBO_COOKIE_GIVEN, ["next"]),
        StoreItemAmountTo7000(CarboCookieItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        JmpIfBitClear(SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]),
        StoreItemAmountTo7000(FireworksItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            super().can_access(inventory, world)
            and can_access_inner_factory_final_boss(world, inventory)
            and not_earlygame(world, inventory)
        )


__all__ = ["FinalBossFightStarPiece"]
