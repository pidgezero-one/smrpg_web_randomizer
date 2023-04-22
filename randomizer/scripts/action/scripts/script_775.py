"""A0775_PLAYER_FALLS_IN_KEEP_LAVA"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 20, ["ACTION_775_set_short_11"]),
        PlaySound(sound=SO105_SURPRISE, channel=4),
        SetAllSpeeds(VERY_FAST),
        SetSpriteSequence(index=3, sprite_offset=2, is_sequence=True, looping=True),
        JumpToHeight(
            height=112, silent=True, identifier="ACTION_775_jump_to_height_silent_5"
        ),
        WalkSouthwestPixels(1),
        WalkWestPixels(4, identifier="ACTION_775_shift_west_pixels_7"),
        JmpIfMarioInAir(["ACTION_775_shift_west_pixels_7"]),
        PlaySound(sound=SO084_SMOKED, channel=4),
        Jmp(["ACTION_775_jump_to_height_silent_5"]),
        SetVarToConst(TEMP_7034, 65535, identifier="ACTION_775_set_short_11"),
        Db(bytearray(b"\xc7\x00")),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["ACTION_775_pause_14"]
        ),
        Pause(6, identifier="ACTION_775_pause_14"),
        Jmp(["ACTION_775_set_short_11"]),
    ]
)
