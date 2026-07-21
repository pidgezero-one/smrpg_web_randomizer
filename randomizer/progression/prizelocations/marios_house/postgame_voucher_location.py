from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.progression.prizes import *
from randomizer.types.flags import *
from randomizer.progression.prizelocations.access import (can_access_fifth_dojo_boss, can_access_inner_mines, can_access_sealed_door_boss, can_access_temple_boss, can_access_tower, can_clear_chapel, can_clear_ship)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (KeyItemLocation, NPCLocationRow6, ShuffleLocationSelector, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class PostgameVoucherLocation(NPCLocationRow6, KeyItemLocation):
    _bias = True
    _originally_held = StayVoucherPrize
    _rooms = [R189_MARIOS_PIPEHOUSE]
    _id = ShuffleLocationSelector = ShuffleLocationSelector.POSTGAME_VOUCHER
    _world_area = WorldAreaEnum.MARIOS_PAD
    _remake_only = True

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return (
            can_access_inner_mines(world, inventory)
            and can_access_tower(world, inventory)
            and can_clear_chapel(world, inventory)
            and can_clear_ship(world, inventory)
            and can_access_temple_boss(world, inventory)
            and can_access_sealed_door_boss(world, inventory)
            and can_access_fifth_dojo_boss(world, inventory)
        )

    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 0),
        # RunDialog(
            # dialog_id=DI2010_DEBUG_7000,
            # above_object=BOWSER,
            # closable=True,
            # sync=False,
            # multiline=True,
            # use_background=True,
        # ),
        JmpIfBitSet(VOUCHER_CHECK_DONE, ["next"]),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(TOWER_BOSS_1_STAR_PIECE, ["next"]),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["next"]),
        JmpIfBitClear(SHIP_LIBERATED, ["next"]),
        JmpIfBitClear(TEMPLE_BOSS_DEFEATED, ["next"]),
        JmpIfBitClear(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["next"]),
        Jmp(["marios_pad_hint_text"]),
    ]


__all__ = ["PostgameVoucherLocation"]
