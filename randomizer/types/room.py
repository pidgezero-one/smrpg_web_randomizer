"""Room type extension with extra sprite actions support."""
from __future__ import annotations

from enum import Enum
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from randomizer.types.gameworld import GameWorld
from smrpgpatchbuilder.datatypes.levels.classes import Room as RoomBase


class ExtraSpriteActions(str, Enum):
    """Enum of specific actions that a sprite (usually of a playable character)
    can be expected to perform in any given room."""

    SWIM = "swim"
    WHIRL = "whirl"
    RECOIL = "recoil"
    SURPRISE_FRAME = "surprise_frame"
    SURPRISE_FRAME_BACK = "surprise_frame_back"
    STANDING_SLEEP = "standing_sleep"
    LEAN_BACK = "lean_back"
    LEAN_BACK_2 = "lean_back_2"
    LEAN_FORWARD = "lean_forward"
    SALUTE = "salute"
    DOWN_PIPE = "down_pipe"
    PRAISE_FRONT = "praise_front"
    PRAISE_BACK = "praise_back"
    DISPLEASED_FRONT = "displeased_front"
    DISPLEASED_BACK = "displeased_back"
    TUMBLE_FRONT = "tumble_front"
    TUMBLE_BACK = "tumble_back"
    EXOR = "exor"
    CHALLENGE = "challenge"
    CHALLENGE_NIMBUS = "challenge_nimbus"
    CROUCH = "crouch"
    YOSHI = "yoshi"
    CLIMB = "climb"
    CLIMB_FRAME = "climb_frame"
    BLACKJACK = "blackjack"
    FLOP = "flop"
    DIZZY = "dizzy"
    WOBBLE = "wobble"
    SLEEP = "sleep"
    HOLD_STAR = "hold_star"
    LOOK_AT_DOLL = "look_at_doll"
    DEFEND = "defend"
    MUTE = "mute"


class Room(RoomBase):
    """Extended Room class with extra_sprite_actions and adjacent_rooms support."""

    extra_sprite_actions: list[ExtraSpriteActions]
    adjacent_rooms: list[int]  # List of adjacent room indices for EXP star buffer propagation

    def __init__(
        self,
        *args,
        extra_sprite_actions: list[ExtraSpriteActions] | None = None,
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

        # Lazy import to avoid circular dependency
        from ..logic.partition_calculator import EXTRA_ACTION_TO_ANIMATION_STATE

        m = world.overworld_character.character_model
        ally = world.overworld_character.ally

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
        for action in self.extra_sprite_actions:
            if action not in EXTRA_ACTION_TO_ANIMATION_STATE:
                continue
            for state in EXTRA_ACTION_TO_ANIMATION_STATE[action]:
                if state not in ally._sprites_primary:
                    continue
                tup = ally._sprites_primary[state]
                if tup[2]:  # is_mold
                    vram_values.append(m.min_vram_from_mold(world, tup[0], tup[1]))
                else:
                    vram_values.append(m.min_vram_from_sequence(world, tup[0], tup[1]))

        min_vram = max(vram_values) + 1
        self.partition.set_ally_sprite_buffer_size(min_vram)


    def update_partition_by_prize(self) -> None:
        """Update the room's partition based on its prize type."""
        pass
