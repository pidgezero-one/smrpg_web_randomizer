"""Room type extension with extra sprite actions support."""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..data.rooms.npcs import ALLY_CLONE_NPC

if TYPE_CHECKING:
    from collections.abc import Sequence
    from randomizer.types.gameworld import GameWorld
from smrpgpatchbuilder.datatypes.levels.classes import (BufferSpace, GLOWING_SAVE_POINT_NPC_BYTES, GLOWING_SAVE_POINT_NPC_INDEX, Room as RoomBase)
from .ally import SpriteAnimationState
from .physical_objects import NPC
from ..utils.npcs import (
            PROTAGONIST_BASE_SPRITE_ID,
            PROTAGONIST_SPRITE_RANGE,
            get_protagonist_sprite,
            min_vram_from_sequence_for_sprite,
            min_vram_from_mold_for_sprite,
        )

# Backwards compatibility alias - deprecated, use SpriteAnimationState directly
ExtraSpriteActions = SpriteAnimationState

class AllyContainerNPC(NPC):
    """Mario character NPC wrapper for recruitment prizes."""

    _base = ALLY_CLONE_NPC


class Room(RoomBase):
    """Extended Room class with extra_sprite_actions, adjacent_rooms, and npc_expected_animations support."""

    extra_sprite_actions: list[SpriteAnimationState]
    adjacent_rooms: list[int]  # List of adjacent room indices for EXP star buffer propagation
    # NPC obj index → list of expected animations. Each entry is one of:
    # - str: SpriteAnimationCollection attribute name (boss sprites)
    # - SpriteAnimationState: ally character animation state
    # - ("character", SpriteAnimationState): explicit ally form (legacy)
    npc_expected_animations: dict[int, Sequence[str | SpriteAnimationState | tuple[str, SpriteAnimationState]]]
    # Role → expected animations, for ending cutscene rooms where the NPC slot a
    # role lands on depends on per-seed recruit assignment. Apply-time code
    # resolves role → character → native NPC slot and writes the corresponding
    # entries into npc_expected_animations before the partition orchestrator runs.
    # Role keys: "marrymore", "mushroom_way", "forest_maze", "inner_mines", "protagonist".
    role_expected_animations: dict[str, Sequence[str | SpriteAnimationState | tuple[str, SpriteAnimationState]]]
    # If the NPC at obj_index still has its vanilla sprite after shuffling,
    # pin that sprite into (slot_index, main_buffer_space) with cannot_clone=False.
    # If the NPC's sprite was replaced, the pin is ignored and the partition
    # calculator proceeds normally.
    vanilla_sprite_buffer_pins: dict[int, tuple[int, BufferSpace]]

    # Opt in to palette-swap sprite merging for this room's henchman slots.
    # OFF by default and deliberately so: merging collapses two recoloured
    # sprites onto one clone buffer, but a merged object renders from the
    # canonical sprite's mold set, so any slot that plays an animation the
    # canonical lacks breaks (room 192's snifits corrupt on mold 6). Only rooms
    # crowded enough to actually need the buffer -- and whose henchmen stay on
    # simple poses -- should turn it on.
    allow_sprite_merging: bool

    def __init__(
        self,
        *args,
        extra_sprite_actions: list[SpriteAnimationState] | None = None,
        adjacent_rooms: list[int] | None = None,
        npc_expected_animations: dict[int, Sequence[str | SpriteAnimationState | tuple[str, SpriteAnimationState]]] | None = None,
        role_expected_animations: dict[str, Sequence[str | SpriteAnimationState | tuple[str, SpriteAnimationState]]] | None = None,
        vanilla_sprite_buffer_pins: dict[int, tuple[int, BufferSpace]] | None = None,
        allow_sprite_merging: bool = False,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.extra_sprite_actions = extra_sprite_actions or []
        self.adjacent_rooms = adjacent_rooms or []
        self.npc_expected_animations = npc_expected_animations or {}
        self.role_expected_animations = role_expected_animations or {}
        self.vanilla_sprite_buffer_pins = vanilla_sprite_buffer_pins or {}
        self.allow_sprite_merging = allow_sprite_merging

    def project_ally_sprite_buffer_size(
        self, world: GameWorld
    ) -> tuple[int, str] | None:
        """Compute what ally_sprite_buffer_size would become for this room
        given world.overworld_character, without mutating anything.

        Returns (new_buffer_size, worst_contributor_label), or None if the
        room has no ally buffer or the protagonist's sprite set isn't known.

        The result is max(min_vram_needed_for_protagonist_animations + 1,
        current ally_sprite_buffer_size). Callers that just want to know
        whether the buffer grows can compare against
        partition.ally_sprite_buffer_size.
        """
        if self.partition is None:
            return None
        if self.partition.ally_sprite_buffer_size == 0:
            return None

        ally = world.overworld_character.ally

        if ally.index not in PROTAGONIST_BASE_SPRITE_ID:
            return None
        protagonist_base = PROTAGONIST_BASE_SPRITE_ID[ally.index]

        # Base animation sequences to always check (offset, sequence_id, label).
        DEFAULT_CHECKS = [
            (0, 0, "base seq 0"),
            (0, 1, "base seq 1"),
            (1, 0, "+1 seq 0"),
            (1, 1, "+1 seq 1"),
            (1, 2, "+1 seq 2"),
            (1, 3, "+1 seq 3"),
            (1, 4, "+1 seq 4"),
            (1, 5, "+1 seq 5"),
            (1, 6, "+1 seq 6"),
            (1, 7, "+1 seq 7"),
            (1, 8, "+1 seq 8"),
            (1, 9, "+1 seq 9"),
        ]

        labelled_values: list[tuple[int, str]] = []
        for offset, seq_id, label in DEFAULT_CHECKS:
            sprite = get_protagonist_sprite(world, ally.index, offset)
            if sprite is None:
                continue
            sid = protagonist_base + offset
            try:
                v = min_vram_from_sequence_for_sprite(world, sid, seq_id, player_sprite=True)
            except (IndexError, AssertionError):
                continue
            labelled_values.append((v, f"default {label} (sprite {sid})"))

        for state in self.extra_sprite_actions:
            if state not in ally._sprites_primary:
                continue
            offset, prop_id, is_mold = ally._sprites_primary[state]
            if offset >= PROTAGONIST_SPRITE_RANGE:
                continue
            sprite = get_protagonist_sprite(world, ally.index, offset)
            if sprite is None:
                continue
            sid = protagonist_base + offset
            props = sprite.animation.properties
            if is_mold:
                if prop_id < len(props.molds):
                    v = min_vram_from_mold_for_sprite(world, sid, prop_id, player_sprite=True)
                    labelled_values.append((v, f"extra {state.name} mold {prop_id} sprite {sid}"))
            else:
                if prop_id < len(props.sequences):
                    v = min_vram_from_sequence_for_sprite(world, sid, prop_id, player_sprite=True)
                    labelled_values.append((v, f"extra {state.name} seq {prop_id} sprite {sid}"))

        if not labelled_values:
            return None
        max_v, max_label = max(labelled_values, key=lambda x: x[0])
        min_vram = max_v + 1
        new_buffer_size = max(min_vram, self.partition.ally_sprite_buffer_size)
        return (new_buffer_size, max_label)

    def update_partition_by_protagonist(self, world: GameWorld) -> None:
        if self.partition is None:
            return
        projection = self.project_ally_sprite_buffer_size(world)
        if projection is None:
            return
        new_buffer_size, max_label = projection
        new_buffer_size = min(3, new_buffer_size)
        self.partition.set_ally_sprite_buffer_size(new_buffer_size)

        # Shift glowing save point NPC index if buffer size increased from original
        buffer_increase = self.partition.ally_sprite_buffer_size - self.partition.original_ally_sprite_buffer_size
        if buffer_increase > 0 and self.effects_npc in GLOWING_SAVE_POINT_NPC_INDEX:
            old_npc_index = GLOWING_SAVE_POINT_NPC_INDEX[self.effects_npc]
            new_npc_index = old_npc_index + buffer_increase
            if new_npc_index in GLOWING_SAVE_POINT_NPC_BYTES:
                self.set_effects_npc(GLOWING_SAVE_POINT_NPC_BYTES[new_npc_index])


    def update_partition_by_prize(self) -> None:
        """Update the room's partition based on its prize type."""
        pass
