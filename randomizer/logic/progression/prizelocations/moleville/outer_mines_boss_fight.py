from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_moleville_entrance, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_2, NPC_3)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class OuterMinesBossFight(BossFightLocation):
    _bias = True
    _originally_held = Croco2BossFight
    _rooms = [
        R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
        R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
        R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
        R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
        R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
        R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
    ]
    _override_id = 518
    _default_battlefield = BF25_UNDERGROUND
    _id = ShuffleLocationSelector.MOLEVILLE_MINES_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.MOLEVILLE
    _pack_id = PACK164_MINES_FIRST_BOSS
    _post_unlocks_event_id = E1199_OUTER_MNES_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE,
            NPC_0,
            sequence_setter_event_id=E0777_MINES_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            NPC_0,
            sequence_setter_event_id=E0779_MINES_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R275_MOLEVILLE_MINES_AREA_06_SMALL_ROOM_LEADING_TO_AREA_06,
            NPC_0,
            sequence_setter_event_id=E0781_MINES_TINY_ROOM_2_LEFT_OF_TRAMPOLINE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R281_MOLEVILLE_MINES_AREA_07_FROM_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0783_MINES_ROOM_THAT_SPLITS_TO_PA_MOLE_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R279_MOLEVILLE_MINES_AREA_08_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0785_MINES_SMALL_NORTH_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
        BossFightLocationNPC(
            R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM,
            NPC_0,
            sequence_setter_event_id=E0787_MINES_LONG_ROOM_IN_MINIBOSS_PATH_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R273_MOLEVILLE_MINES_AREA_04_WTRAMPOLINE],
            [NPC_1],
            PACK142_MINES_HENCHMAN_MIDDLE,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [
                R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
                R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
                R277_MOLEVILLE_MINES_AREA_05_LEFT_OF_TRAMPOLINE_ROOM,
            ],
            [NPC_1, NPC_2, NPC_3],
            PACK141_MINES_HENCHMAN_LEFT,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [R283_MOLEVILLE_MINES_AREA_09_LEADS_LEFT_TO_CROCOS_BOMBED_ROOM],
            [NPC_1],
            PACK079_MINES_HENCHMAN_RIGHT,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_moleville_entrance(world, inventory)


__all__ = ["OuterMinesBossFight"]
