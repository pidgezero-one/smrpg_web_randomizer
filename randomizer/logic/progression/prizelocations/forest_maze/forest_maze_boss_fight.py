from __future__ import annotations
from typing import TYPE_CHECKING
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands import *
from randomizer.data.variables.room_names import *
from randomizer.data.variables.event_script_names import *
from randomizer.data.variables.action_script_names import *
from randomizer.data.variables.pack_names import *
from randomizer.logic.progression.prizes import *
from randomizer.types.flags import *
from randomizer.logic.progression.prizelocations.access import (boss_slot_min_vram_cap_for_room, can_clear_forest, can_damage_enemies_with_spells, expect_good_movement, not_earlygame, expect_halfway_decent_movement, almost_earlygame, is_midgame, expect_ok_movement, lategame)
from randomizer.logic.progression.prizelocations.forest_maze.forest_maze_character import ForestMazeCharacter
from randomizer.types.logic import (Inventory)
from randomizer.types.prize import (Prize)
from randomizer.types.prizelocation import (BossFightLocation, BossFightLocationHenchmanNPC, BossFightLocationNPC, ShuffleLocationSelector, WorldAreaEnum)
from randomizer.utils.npcs import (set_npc_direction_if_swse_only)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.area_objects import (NPC_0, NPC_1, NPC_11, NPC_13, NPC_2, NPC_3, NPC_4, NPC_5, NPC_6, NPC_7, NPC_8, NPC_9)
from smrpgpatchbuilder.datatypes.overworld_scripts.arguments.directions import (SOUTHEAST)
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.classes import (EventScript, UsableEventScriptCommand)
if TYPE_CHECKING:
    from randomizer.types.gameworld import (GameWorld)


def _forest_maze_boss_min_vram_cap(world: GameWorld) -> int:
    return boss_slot_min_vram_cap_for_room(
        world,
        R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
        base_budget=1,
        recruit_location=ForestMazeCharacter,
    )


class ForestMazeBossFight(BossFightLocation):
    _bias = True
    _originally_held = BowyerBossFight
    _rooms = [R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD]
    _id = ShuffleLocationSelector.FOREST_MAZE_BOSS
    _world_area = WorldAreaEnum.FOREST_MAZE
    _pack_id = PACK181_FOREST_BOSS
    _post_unlocks_event_id = E1198_FOREST_MAZE_BOSS_UNLOCKS
    _npc_slots = [
        BossFightLocationNPC(
            R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD,
            NPC_11,
            sequence_setter_event_id=E0775_FOREST_MAZE_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
            # Adaptive cap: tighten when protagonist pushes ally buffer up or
            # when ForestMazeCharacter recruits Bowser.
            min_vram_size_override=_forest_maze_boss_min_vram_cap,
            min_vram_from_seq0_override=_forest_maze_boss_min_vram_cap,
        ),
    ]
    _character_henchman_slots = [
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_1]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_7]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_3]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_9]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_4]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_5]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_2]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_8]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_0]),
        BossFightLocationHenchmanNPC([R232_FOREST_MAZE_BOWYERS_PRACTICE_PAD], [NPC_6]),
    ]
    _mook_henchman_slots = [
        BossFightLocationHenchmanNPC([R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE], [NPC_7]),
        BossFightLocationHenchmanNPC([R083_ROSE_TOWN_DURING_BOWYER_OUTSIDE], [NPC_8]),
        BossFightLocationHenchmanNPC([R228_FOREST_MAZE_AREA_04], [NPC_1]),
        BossFightLocationHenchmanNPC(
            [R230_FOREST_MAZE_4WAY_PATH_FROM_AREA_09], [NPC_13]
        ),
    ]

    def can_accept(self, prize: Prize, inventory: Inventory, world: GameWorld) -> bool:
        return super().can_accept(prize, inventory, world) and (
            can_damage_enemies_with_spells(world, inventory)
            or not isinstance(prize, MokuraBossFight)
        )

    def can_access(self, inventory: Inventory, world: GameWorld) -> bool:
        return can_clear_forest(world, inventory)

    def post_unlocks(self, world: GameWorld) -> EventScript:
        content: list[UsableEventScriptCommand] = []
        if world.settings.is_flag_value(Moleville1Gate, Moleville1Gating.FOREST):
            content.extend(
                [
                    ClearBit(MOLEVILLE_MINES_ENTRANCE_GATING),
                ]
            )
        if world.settings.is_flag_value(PipeVaultGate, PipeVaultGating.FOREST):
            content.extend(
                [
                    ClearBit(PIPE_VAULT_GATED),
                ]
            )
        parent = super().post_unlocks(world)
        return EventScript(content + parent.contents + [Return()])

    def render(self, world: GameWorld) -> tuple[
        list[list[UsableEventScriptCommand]],
        list[UsableEventScriptCommand],
        list[tuple[int, int, int]],
    ]:
        result = super().render(world)
        # Fix directions for all character henchman NPCs in the boss room.
        # super().render() only runs _on_henchmen_assigned when the prize
        # differs from the original, but the vanilla Aero NPCs also face
        # NORTHEAST/SOUTHWEST despite being SWSE-only sprites.
        if self._character_henchman_slots is None:
            return result
        for slot in self._character_henchman_slots:
            for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                room = world.rooms._rooms[room_id]
                assert room is not None
                obj = room.get_npc_by_target_id(npc_id)
                if obj is not None:
                    npc_base = obj._npc
                    set_npc_direction_if_swse_only(
                        world, room_id, npc_id, npc_base, SOUTHEAST
                    )
        return result

    def _on_henchmen_assigned(
        self,
        world: GameWorld,
        henchmen_assignments: list[
            tuple[BossFightLocationHenchmanNPC, BossFightHenchman]
        ],
    ) -> None:
        if self._character_henchman_slots is None:
            return

        # Build a lookup of slot -> henchman for quick access
        assignment_map: dict[BossFightLocationHenchmanNPC, BossFightHenchman] = {
            slot: henchman for slot, henchman in henchmen_assignments
        }

        removed_ctr = 0

        # Loop through ALL character henchman slots, not just assigned ones
        for slot in self._character_henchman_slots:
            henchman = assignment_map.get(slot)
            for npc_id, room_id in zip(slot.npc_ids, slot.room_ids):
                # Check if this slot was assigned
                if henchman is not None:
                    npc_base = henchman.model().base
                    set_npc_direction_if_swse_only(
                        world, room_id, npc_id, npc_base, SOUTHEAST
                    )
                else:
                    # Slot was not assigned - hide the NPC with default sprite
                    if not isinstance(
                        self.prize, self._originally_held  # pyright: ignore
                    ):
                        removed_ctr += 1
                        rm = world.rooms._rooms[room_id]
                        assert rm is not None
                        rm.get_npc_by_target_id(npc_id).set_visible(False)
                        world.event_scripts.delete_command_by_identifier(
                            f"forest_henchman_{npc_id}"
                        )
        if removed_ctr == 10:
            world.event_scripts.delete_command_by_identifier(
                "forest_henchmen_bounce_30"
            )

        # If any mook henchman slot received a new model, remove Aero's
        # bouncing animation mold commands (they reference Aero-specific
        # sprite sequences that won't exist for the replacement NPC).
        if self._mook_henchman_slots is not None:
            mook_slots_assigned = any(
                slot in assignment_map and assignment_map[slot].model is not None
                for slot in self._mook_henchman_slots
            )
            if mook_slots_assigned:
                for i in range(1, 8):
                    world.action_scripts.delete_command_by_identifier(f"aero_mold_{i}")


__all__ = ["ForestMazeBossFight"]
