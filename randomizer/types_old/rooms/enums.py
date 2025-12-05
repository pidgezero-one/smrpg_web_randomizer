"""Enums supporting development surrounding room contents."""

from enum import Enum, IntEnum


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


class ObjectType(IntEnum):
    """Enum of NPC subtypes that control what properties they should have
    in the ROM."""

    OBJECT = 0
    CHEST = 1
    BATTLE = 2


class EventInitiator(IntEnum):
    """Enum of the rules by which an NPC can have its interaction triggered."""

    NONE = 0x0
    PRESS_A_FROM_ANY_SIDE = 0x1
    PRESS_A_FROM_FRONT = 0x2
    ANYTHING_EXCEPT_TOUCH_SIDE = 0x3
    PRESS_A_OR_TOUCH_ANY_SIDE = 0x4
    PRESS_A_OR_TOUCH_FRONT = 0x5
    DO_ANYTHING = 0x6
    HIT_FROM_BELOW = 0x7
    JUMP_ON = 0x8
    JUMP_ON_OR_HIT_FROM_BELOW = 0x9
    TOUCH_ANY_SIDE = 0xA
    TOUCH_FROM_FRONT = 0xB
    ANYTHING_EXCEPT_PRESS_A = 0xC


class PostBattleBehaviour(IntEnum):
    """Enum of the ways NPCs should behave in the overworld after defeated in battle"""

    REMOVE_PERMANENTLY = 0x0
    REMOVE_UNTIL_RELOAD = 0x1
    DO_NOT_REMOVE = 0x2
    REMOVE_PERMANENTLY_NO_IFRAME_COLLISION = 0x3
    REMOVE_UNTIL_RELOAD_NO_IFRAME_COLLISION = 0x4
    UNKNOWN = 0x08


class EdgeDirection(IntEnum):
    """Enum of directions an event or exit tile can face"""

    SOUTHEAST = 0x00
    SOUTHWEST = 0x01


class ExitType(IntEnum):
    """Enum of room exit types"""

    ROOM = 0x00
    MAP_LOCATION = 0x01


class BufferType(IntEnum):
    """Enum of partition buffer types"""

    THREE_SPRITES_PER_ROW = 0x00
    FOUR_SPRITES_PER_ROW = 0x01
    TREASURE_CHEST = 0x02
    EMPTY_TREASURE_CHEST = 0x03
    COINS = 0x04
    EMPTY_1 = 0x05
    EMPTY_2 = 0x06
    EMPTY_3 = 0x07


class BufferSpace(IntEnum):
    """Enum of partition buffer sizes"""

    BYTES_0 = 0x00
    BYTES_256 = 0x01
    BYTES_512 = 0x02
    BYTES_768 = 0x03
    BYTES_1024 = 0x04
    BYTES_1280 = 0x05
    BYTES_1536 = 0x06
    BYTES_1792 = 0x07
