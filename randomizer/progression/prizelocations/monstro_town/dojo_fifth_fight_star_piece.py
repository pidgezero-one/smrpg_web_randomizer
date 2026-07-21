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
from randomizer.progression.prizelocations.access import (can_access_fifth_dojo_boss)
from randomizer.progression.prizelocations.monstro_town.dojo_fifth_fight import (DojoFifthFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class DojoFifthFightStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R255_MONSTRO_TOWN_JINXS_DOJO]
    _id = ShuffleLocationSelector.DOJO_BOSS_POSTGAME
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _override_id = 525
    _remake_only = True
    _parent = DojoFifthFight
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 295),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitSet(DOJO_POSTGAME_COMPLETED, ["next"]),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitClear(DOJO_BOSS_4_DEFEATED, ["next"]),
        JmpIfBitSet(STAY_VOUCHER_USED, ["monstro_town_hint_text"]),
        StoreItemAmountTo7000(StayVoucherItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["next"]),
        Jmp(["marrymore_hotel_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_fifth_dojo_boss(
            world, inventory
        )


__all__ = ["DojoFifthFightStarPiece"]
