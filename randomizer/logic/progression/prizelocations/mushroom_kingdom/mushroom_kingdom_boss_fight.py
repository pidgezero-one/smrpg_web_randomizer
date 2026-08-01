from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (can_access_bandits_way, can_damage_enemies_with_spells)
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from randomizer.utils.npcs import (set_npc_direction_if_swse_only)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_10, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


class MushroomKingdomBossFight(BossFightLocation):
    _bias = True
    _originally_held = MackBossFight
    _rooms = [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM]
    _id = ShuffleLocationSelector.INVASION_BOSS_FIGHT
    _world_area = WorldAreaEnum.MUSHROOM_KINGDOM
    _pack_id = PACK179_MUSHROOM_KINGDOM_BOSS
    _post_unlocks_event_id = E1196_MUSHROOM_KINGDOM_BOSS_UNLOCKS
    _henchman_can_run_away = False

    _npc_slots = [
        BossFightLocationNPC(
            R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM,
            NPC_3,
            sequence_setter_event_id=E0761_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_4],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_5],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_6],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_7],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_8],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
        BossFightLocationHenchmanNPC(
            [R326_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_THRONE_ROOM],
            [NPC_9],
            skip_swap_if_flag=KeepMinigameSpritesIntact,
        ),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC(
            [
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                R017_MUSHROOM_KINGDOM_CASTLE_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
                R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                R191_MUSHROOM_KINGDOM_OUTSIDE,
            ],
            [
                NPC_3,
                NPC_5,
                NPC_0,
                NPC_4,
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_3,
                NPC_4,
                NPC_0,
                NPC_1,
                NPC_4,
                NPC_10,
            ],
            pack_id=PACK010_KINGDOM_HENCHMEN_1,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0051_HENCHMAN_CONTAINER_1,
        ),
        BossFightLocationHenchmanNPC(
            [
                R325_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_MAIN_HALL,
            ],
            [
                NPC_3,
            ],
        ),
        BossFightLocationHenchmanNPC(
            [
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
                R323_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_THRONE_ROOM,
                R327_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_STAIRWELL_TO_TOADSTOOLS_ROOM,
                R329_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_BRANCH_ROOM_TO_VAULTGUEST_ROOM,
                R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                R332_MUSHROOM_KINGDOM_CASTLE_DURING_MACK_ENTRANCE_TO_TOADSTOOLS_ROOM,
                R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
                R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ],
            [
                NPC_0,
                NPC_1,
                NPC_2,
                NPC_4,
                NPC_6,
                NPC_1,
                NPC_1,
                NPC_0,
                NPC_0,
                NPC_1,
                NPC_3,
                NPC_1,
            ],
            pack_id=PACK011_KINGDOM_HENCHMEN_2,
            skip_swap_if_flag=KeepMinigameSpritesIntact,
            container_event=E0052_HENCHMAN_CONTAINER_2,
        ),
    ]

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_access_bandits_way(world, inventory)

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        for slot, henchman in henchmen_assignments:
            model = henchman.model
            if model is not None:
                npc_base = model().base
                for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                    set_npc_direction_if_swse_only(world, room_id, npc_id, npc_base)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(KeroSewersGate, KeroSewersGating.KINGDOM):
            content.extend(
                [
                    ClearBit(SEWERS_CLOSED),
                    RemoveObjectFromSpecificLevel(NPC_0, R333_KERO_SEWERS_ENTRANCE),
                    RemoveObjectFromSpecificLevel(NPC_1, R333_KERO_SEWERS_ENTRANCE),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])


__all__ = ["MushroomKingdomBossFight"]
