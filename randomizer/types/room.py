"""Room type extension with extra sprite actions support."""

from enum import Enum
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
    """Extended Room class with extra_sprite_actions support."""

    extra_sprite_actions: list[ExtraSpriteActions]

    def __init__(
        self,
        *args,
        extra_sprite_actions: list[ExtraSpriteActions] | None = None,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self.extra_sprite_actions = extra_sprite_actions or []
