import enum
from json import JSONEncoder


class StringEnum(str, enum.Enum):
    pass


class ExtraSpriteActions(StringEnum):
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
