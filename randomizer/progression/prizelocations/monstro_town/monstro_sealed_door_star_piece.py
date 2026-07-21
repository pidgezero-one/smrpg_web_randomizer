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
from randomizer.progression.prizelocations.access import (can_access_sealed_door_boss)
from randomizer.progression.prizelocations.monstro_town.monstro_sealed_door_boss_fight import (MonstroSealedDoorBossFight)
from randomizer.types.logic import (Inventory)
from randomizer.types.prizelocation import (BossFightLocationNPC, ShuffleLocationSelector, StarPieceLocation, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1, NPC_2)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MonstroSealedDoorStarPiece(StarPieceLocation):
    _bias = True
    _originally_held = None
    _rooms = [R324_MONSTRO_TOWN_OUTSIDE]
    _id = ShuffleLocationSelector.CULEX_BOSS
    _world_area = WorldAreaEnum.MONSTRO_TOWN
    _parent = MonstroSealedDoorBossFight
    _npc_slots = [
        BossFightLocationNPC(
            R351_CULEXS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0816_MONSTRO_SUPERBOSS_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _hint = [
        # SetVarToConst(PRIMARY_TEMP_7000, 297),
        # RunDialog(
        #     dialog_id=DI2010_DEBUG_7000,
        #     above_object=BOWSER,
        #     closable=True,
        #     sync=False,
        #     multiline=True,
        #     use_background=True,
        # ),
        JmpIfBitClear(MAP_MONSTRO_TOWN, ["next"]),
        JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["next"]),
        JmpIfBitSet(CULEX_POSTGAME_COMPLETED, ["next"]),
        # door will be open if you have progressive fireworks or single fireworks enabled and have gotten to the carbo cookie
        JmpIfObjectNotInSpecificLevel(
            NPC_2, R324_MONSTRO_TOWN_OUTSIDE, ["monstro_town_hint_text"]
        ),
        # door is always openable if you have a shiny stone
        StoreItemAmountTo7000(ShinyStoneItem),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["monstro_town_hint_text"]),
        # if none of the above are true, you need to turn in the fireworks if moleville is liberated and shuffle one is turned on
        # or just buy a fireworks if vanilla behaviour enabled
        # but if progressive is turned on, you're blocked until you find another upgrade
        JmpIfBitSet(PROGRESSIVE_FIREWORKS_ENABLED, ["next"]),
        JmpIfBitClear(MINES_BOSS_2_DEFEATED, ["next"]),
        JmpIfBitClear(
            SHUFFLE_ONE_FIREWORKS_ENABLED, ["moleville_hint_text"]
        ),  # should tell you to go to moleville since thats where the shiny stone is
        StoreItemAmountTo7000(
            FireworksItem
        ),  # final branch: shuffle 1 is turned on and moleville is cleared: if you have a fireworks you can exchange it now
        JmpIfVarNotEqualsConst(PRIMARY_TEMP_7000, 1, ["next"]),
        Jmp(["moleville_hint_text"]),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_access(inventory, world) and can_access_sealed_door_boss(
            world, inventory
        )


__all__ = ["MonstroSealedDoorStarPiece"]
