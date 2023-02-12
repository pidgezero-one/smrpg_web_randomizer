from enum import Enum, IntEnum


class ExtraSpriteActions(str, Enum):
    Swim = "swim"
    Whirl = "whirl"
    Recoil = "recoil"
    SurpriseFrame = "surprise_frame"
    SurpriseFrameBack = "surprise_frame_back"
    StandingSleep = "standing_sleep"
    LeanBack = "lean_back"
    LeanBack2 = "lean_back_2"
    LeanForward = "lean_forward"
    Salute = "salute"
    DownPipe = "down_pipe"
    PraiseFront = "praise_front"
    PraiseBack = "praise_back"
    DispleasedFront = "displeased_front"
    DispleasedBack = "displeased_back"
    TumbleFront = "tumble_front"
    TumbleBack = "tumble_back"
    Exor = "exor"
    Challenge = "challenge"
    ChallengeNimbus = "challenge_nimbus"
    Crouch = "crouch"
    Yoshi = "yoshi"
    Climb = "climb"
    ClimbFrame = "climb_frame"
    Blackjack = "blackjack"
    Flop = "flop"
    Dizzy = "dizzy"
    Wobble = "wobble"
    Sleep = "sleep"
    HoldStar = "hold_star"
    LookAtDoll = "look_at_doll"
    Defend = "defend"
    Mute = "mute"


class ObjectType(IntEnum):
    OBJECT = 0
    CHEST = 1
    BATTLE = 2


class EventInitiator(IntEnum):
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
    REMOVE_PERMANENTLY = 0x0
    REMOVE_UNTIL_RELOAD = 0x1
    DO_NOT_REMOVE = 0x2
    REMOVE_PERMANENTLY_NO_IFRAME_COLLISION = 0x3
    REMOVE_UNTIL_RELOAD_NO_IFRAME_COLLISION = 0x4
    UNKNOWN = 0x08


class EdgeDirection(IntEnum):
    SOUTHEAST = 0x00
    SOUTHWEST = 0x01


class ExitType(IntEnum):
    ROOM = 0x00
    MAP_LOCATION = 0x01


class BufferType(IntEnum):
    _3_SPRITES_PER_ROW = 0x00
    _4_SPRITES_PER_ROW = 0x01
    TREASURE_CHEST = 0x02
    EMPTY_TREASURE_CHEST = 0x03
    COINS = 0x04
    EMPTY_1 = 0x05
    EMPTY_2 = 0x06
    EMPTY_3 = 0x07


class BufferSpace(IntEnum):
    _0_BYTES = 0x00
    _256_BYTES = 0x01
    _512_BYTES = 0x02
    _768_BYTES = 0x03
    _1024_BYTES = 0x04
    _1280_BYTES = 0x05
    _1536_BYTES = 0x06
    _1792_BYTES = 0x07
