from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_clear_volcano, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_1, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class VolcanoBridgeBossFight(BossFightLocation):
    _bias = True
    _originally_held = CzarDragonBossFight
    _rooms = [R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM]
    _id = ShuffleLocationSelector.BARREL_VOLCANO_BOSS_FIGHT_1
    _world_area = WorldAreaEnum.BARREL_VOLCANO
    _pack_id = PACK172_VOLCANO_FIRST_BOSS
    _post_unlocks_event_id = E1233_VOLCANO_MID_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            NPC_1,
            sequence_setter_event_id=E0840_VOLCANO_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
                R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            ],
            [NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9],
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_volcano(world, inventory)


__all__ = ["VolcanoBridgeBossFight"]
