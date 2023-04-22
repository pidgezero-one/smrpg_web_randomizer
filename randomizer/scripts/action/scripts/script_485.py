"""A0485_PLAYER_SHOCKED_WHEN_WIGGLER_WAKES_UP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
        SetSpriteSequence(
            index=0,
            sprite_offset=3,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
        ),
        ShiftToXYCoords(x=3, y=74),
        SetWalkingSpeed(FASTEST),
        WalkSoutheastPixels(4),
        WalkNorthPixels(8),
        SetSpriteSequence(
            index=0,
            sprite_offset=3,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_485_set_sprite_sequence_6",
        ),
        Pause(10),
        SetSpriteSequence(
            index=0,
            sprite_offset=3,
            is_mold=True,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
        ),
        Pause(10),
        JmpIfBitSet(TEMP_7043_0, ["ACTION_485_pause_12"]),
        Jmp(["ACTION_485_set_sprite_sequence_6"]),
        Pause(3, identifier="ACTION_485_pause_12"),
        WalkSoutheastPixels(4),
        Db(bytearray(b" \x04")),
        Db(bytearray(b"%\x00\x0f\x80\xff")),
        Pause(48),
        BPL262728(),
        Return(),
    ]
)
