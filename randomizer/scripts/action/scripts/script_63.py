"""A0063_EXPLOSION_WITH_SOUND"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        Set700CToCurrentLevel(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C, 13, ["ACTION_63_sequence_looping_on_3"]
        ),
        SetVRAMPriority(PRIORITY_3),
        SequenceLoopingOn(identifier="ACTION_63_sequence_looping_on_3"),
        SequencePlaybackOn(),
        ClearSolidityBits(cant_pass_walls=True),
        SetSpriteSequence(index=0, looping=False),
        JmpIfBitSet(TEMP_7042_7, ["ACTION_63_play_sound_13"]),
        Set700CToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 457, ["ACTION_63_play_sound_11"]),
        JmpIfVarEqualsConst(
            CURRENT_OVERWORLD_MARKER_ID, 4, ["ACTION_63_play_sound_17"]
        ),
        PlaySound(
            sound=SO060_DYNAMITE_BOMB_EXPLOSION,
            channel=4,
            identifier="ACTION_63_play_sound_11",
        ),
        Jmp(["ACTION_63_shift_z_up_pixels_14"]),
        PlaySound(
            sound=SO113_OPEN_CHAMBER_DOOR,
            channel=4,
            identifier="ACTION_63_play_sound_13",
        ),
        ShiftZUpPixels(18, identifier="ACTION_63_shift_z_up_pixels_14"),
        VisibilityOff(),
        Return(),
        PlaySound(
            sound=SO052_DEEP_BOUNCE, channel=4, identifier="ACTION_63_play_sound_17"
        ),
        Jmp(["ACTION_63_shift_z_up_pixels_14"]),
    ]
)
