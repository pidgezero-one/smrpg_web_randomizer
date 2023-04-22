"""A0459_FACTORY_SWITCH_ROOM_AMEBOID"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetWalkingSpeed(SLOW),
        ShadowOff(),
        SequenceLoopingOn(),
        WalkSouthwestSteps(4),
        WalkSouthwestPixels(10),
        SetSpriteSequence(index=9, is_sequence=True, looping=True),
        FloatingOn(),
        JumpToHeight(0),
        ShadowOn(),
        Pause(24),
        SetWalkingSpeed(NORMAL),
        ResetProperties(),
        WalkToXYCoords(x=22, y=85),
        SetSpriteSequence(index=9, is_sequence=True, looping=True, mirror_sprite=True),
        Db(bytearray(b" \x07")),
        Db(bytearray(b"$\x00\xff\xb0\x00"), identifier="ACTION_459_db_15"),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Pause(30),
        Db(bytearray(b"$\x80\xfe\x00\xff")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Pause(30),
        Db(bytearray(b"$\x80\x01\x00\x01")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Pause(30),
        Db(bytearray(b"$\x00\x01P\xff")),
        Db(bytearray(b"%\xc0\x06\x80\xff")),
        Pause(30),
        Jmp(["ACTION_459_db_15"]),
    ]
)
