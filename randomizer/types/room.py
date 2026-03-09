"""Room type extension with extra sprite actions support."""
from __future__ import annotations

from typing import TYPE_CHECKING

from ..data.rooms.npcs import ALLY_CLONE_NPC

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld
from smrpgpatchbuilder.datatypes.levels.classes import (
    GLOWING_SAVE_POINT_NPC_BYTES,
    GLOWING_SAVE_POINT_NPC_INDEX,
    Room as RoomBase,
)
from .ally import SpriteAnimationState
from .physical_objects import NPC

# Backwards compatibility alias - deprecated, use SpriteAnimationState directly
ExtraSpriteActions = SpriteAnimationState

class AllyContainerNPC(NPC):
    """Mario character NPC wrapper for recruitment prizes."""

    _base = ALLY_CLONE_NPC


class Room(RoomBase):
    """Extended Room class with extra_sprite_actions and adjacent_rooms support."""

    extra_sprite_actions: list[SpriteAnimationState]
    adjacent_rooms: list[int]  # List of adjacent room indices for EXP star buffer propagation

    def __init__(
        self,
        *args,
        extra_sprite_actions: list[SpriteAnimationState] | None = None,
        adjacent_rooms: list[int] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.extra_sprite_actions = extra_sprite_actions or []
        self.adjacent_rooms = adjacent_rooms or []

    def update_partition_by_protagonist(self, world: GameWorld) -> None:
        if self.partition is None:
            return
        if self.partition.ally_sprite_buffer_size == 0:
            return

        old_buffer_size = self.partition.ally_sprite_buffer_size

        ally = world.overworld_character.ally
        m = world.overworld_character.character_model if ally.index == 0 else AllyContainerNPC()

        # Base animation sequences to always check
        vram_values = [
            m.min_vram_from_sequence(world, a[0], a[1])
            for a in [
                (0, 0),
                (1, 0),
                (0, 1),
                (1, 1),
                (2, 1),
                (3, 1),
                (4, 1),
                (5, 1),
                (6, 1),
                (7, 1),
                (8, 1),
                (9, 1),
            ]
        ]

        # Check extra sprite actions required by this room
        for state in self.extra_sprite_actions:
            if state not in ally._sprites_primary:
                continue
            tup = ally._sprites_primary[state]
            # Validate the sprite reference before using it
            sprite = world.get_sprite(m.base.sprite_id + tup[1])
            props = sprite.animation.properties
            if tup[2]:  # is_mold
                if tup[0] < len(props.molds):
                    vram_values.append(m.min_vram_from_mold(world, tup[0], tup[1]))
            else:
                if tup[0] < len(props.sequences):
                    vram_values.append(m.min_vram_from_sequence(world, tup[0], tup[1]))

        min_vram = max(vram_values) + 1
        self.partition.set_ally_sprite_buffer_size(max(min_vram, self.partition.ally_sprite_buffer_size))

        # Shift glowing save point NPC index if buffer size increased
        buffer_increase = self.partition.ally_sprite_buffer_size - old_buffer_size
        if buffer_increase > 0 and self.effects_npc in GLOWING_SAVE_POINT_NPC_INDEX:
            old_npc_index = GLOWING_SAVE_POINT_NPC_INDEX[self.effects_npc]
            new_npc_index = old_npc_index + buffer_increase
            if new_npc_index in GLOWING_SAVE_POINT_NPC_BYTES:
                self.set_effects_npc(GLOWING_SAVE_POINT_NPC_BYTES[new_npc_index])


    def update_partition_by_prize(self) -> None:
        """Update the room's partition based on its prize type."""
        pass
