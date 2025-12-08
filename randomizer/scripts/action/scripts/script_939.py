"""A0939_EMPTY"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOn(),
        JmpIfVarEqualsConst(TEMP_70AF, 0, ["ACTION_939_set_sprite_sequence_6"]),
        JmpIfVarEqualsConst(TEMP_70AF, 1, ["ACTION_939_set_sprite_sequence_44"]),
        JmpIfVarEqualsConst(TEMP_70AF, 2, ["ACTION_939_set_sprite_sequence_57"]),
        JmpIfVarEqualsConst(TEMP_70AF, 3, ["ACTION_939_inc_palette_row_by_70"]),
        JmpIfVarEqualsConst(TEMP_70AF, 4, ["ACTION_939_inc_palette_row_by_86"]),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_6"),
        Pause(1, identifier="ACTION_939_pause_7"),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 0, ["ACTION_939_set_sprite_sequence_6"]
        ),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 1, ["ACTION_939_set_sprite_sequence_12"]
        ),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 2, ["ACTION_939_set_sprite_sequence_14"]
        ),
        Jmp(["ACTION_939_pause_7"]),
        SetSpriteSequence(
            index=5,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_12"),
        Jmp(["ACTION_939_pause_7"]),
        SetSpriteSequence(
            index=0,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_14"),
        PlaySound(sound=SO004_JUMP, channel=4, identifier="ACTION_939_play_sound_15"),
        JumpToHeight(96),
        Pause(15),
        FloatingOff(),
        SetWalkingSpeed(VERY_SLOW),
        WalkSouthPixels(5),
        PlaySound(sound=SO058_INSERT, channel=4),
        Set700CToPressedButton(),
        AddConstToVar(PRIMARY_TEMP_700C, 65515),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_939_set_object_memory_bits_29"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 2, ["ACTION_939_set_object_memory_bits_31"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 3, ["ACTION_939_set_object_memory_bits_33"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 4, ["ACTION_939_set_object_memory_bits_35"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 5, ["ACTION_939_set_object_memory_bits_37"]
        ),
        SetObjectMemoryBits(
            arg_1=0x0E, bits=[0], identifier="ACTION_939_set_object_memory_bits_29"
        ),
        Jmp(["ACTION_939_pause_39"]),
        SetObjectMemoryBits(
            arg_1=0x0E, bits=[1], identifier="ACTION_939_set_object_memory_bits_31"
        ),
        Jmp(["ACTION_939_pause_39"]),
        SetObjectMemoryBits(
            arg_1=0x0E, bits=[0, 1], identifier="ACTION_939_set_object_memory_bits_33"
        ),
        Jmp(["ACTION_939_pause_39"]),
        SetObjectMemoryBits(
            arg_1=0x0E, bits=[2], identifier="ACTION_939_set_object_memory_bits_35"
        ),
        Jmp(["ACTION_939_pause_39"]),
        SetObjectMemoryBits(
            arg_1=0x0E, bits=[0, 2], identifier="ACTION_939_set_object_memory_bits_37"
        ),
        Jmp(["ACTION_939_pause_39"]),
        Pause(1, identifier="ACTION_939_pause_39"),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 2, ["ACTION_939_pause_39"]),
        VisibilityOff(),
        Pause(2),
        Return(),
        SetSpriteSequence(
            index=1,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_44"),
        ShiftXYPixels(x=244, y=3),
        Pause(1, identifier="ACTION_939_pause_46"),
        JmpIfVarEqualsConst(TEMP_7026, 0, ["ACTION_939_set_sprite_sequence_51"]),
        JmpIfVarEqualsConst(TEMP_7026, 1, ["ACTION_939_set_sprite_sequence_53"]),
        JmpIfVarEqualsConst(TEMP_7026, 2, ["ACTION_939_set_sprite_sequence_55"]),
        Jmp(["ACTION_939_pause_46"]),
        SetSpriteSequence(
            index=1,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_51"),
        Jmp(["ACTION_939_pause_46"]),
        SetSpriteSequence(
            index=6,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_53"),
        Jmp(["ACTION_939_pause_46"]),
        SetSpriteSequence(
            index=1,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_55"),
        Jmp(["ACTION_939_play_sound_15"]),
        SetSpriteSequence(
            index=2,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_57"),
        ShiftXYPixels(x=232, y=8),
        Pause(1, identifier="ACTION_939_pause_59"),
        JmpIfVarEqualsConst(TEMP_7028, 0, ["ACTION_939_set_sprite_sequence_64"]),
        JmpIfVarEqualsConst(TEMP_7028, 1, ["ACTION_939_set_sprite_sequence_66"]),
        JmpIfVarEqualsConst(TEMP_7028, 2, ["ACTION_939_set_sprite_sequence_68"]),
        Jmp(["ACTION_939_pause_59"]),
        SetSpriteSequence(
            index=2,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_64"),
        Jmp(["ACTION_939_pause_59"]),
        SetSpriteSequence(
            index=7,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_66"),
        Jmp(["ACTION_939_pause_59"]),
        SetSpriteSequence(
            index=2,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_68"),
        Jmp(["ACTION_939_play_sound_15"]),
        IncPaletteRowBy(1, identifier="ACTION_939_inc_palette_row_by_70"),
        SetSpriteSequence(index=3, is_sequence=True, looping=True),
        ShiftXYPixels(x=12, y=3),
        Pause(1, identifier="ACTION_939_pause_73"),
        JmpIfVarEqualsConst(TEMP_702A, 0, ["ACTION_939_set_sprite_sequence_78"]),
        JmpIfVarEqualsConst(TEMP_702A, 1, ["ACTION_939_set_sprite_sequence_80"]),
        JmpIfVarEqualsConst(TEMP_702A, 2, ["ACTION_939_set_sprite_sequence_82"]),
        Jmp(["ACTION_939_pause_73"]),
        SetSpriteSequence(
            index=3,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_78"),
        Jmp(["ACTION_939_pause_73"]),
        SetSpriteSequence(
            index=8,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_80"),
        Jmp(["ACTION_939_pause_73"]),
        SetSpriteSequence(
            index=3,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_82"),
        JmpToSubroutine(["ACTION_939_play_sound_15"]),
        IncPaletteRowBy(15),
        Return(),
        IncPaletteRowBy(1, identifier="ACTION_939_inc_palette_row_by_86"),
        SetSpriteSequence(index=4, is_sequence=True, looping=True),
        ShiftXYPixels(x=24, y=8),
        Pause(1, identifier="ACTION_939_pause_89"),
        JmpIfVarEqualsConst(TEMP_702C, 0, ["ACTION_939_set_sprite_sequence_94"]),
        JmpIfVarEqualsConst(TEMP_702C, 1, ["ACTION_939_set_sprite_sequence_96"]),
        JmpIfVarEqualsConst(TEMP_702C, 2, ["ACTION_939_set_sprite_sequence_98"]),
        Jmp(["ACTION_939_pause_89"]),
        SetSpriteSequence(
            index=4,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_94"),
        Jmp(["ACTION_939_pause_89"]),
        SetSpriteSequence(
            index=9,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_96"),
        Jmp(["ACTION_939_pause_89"]),
        SetSpriteSequence(
            index=4,
            is_sequence=True,
            looping=True,
            identifier="ACTION_939_set_sprite_sequence_98"),
        JmpToSubroutine(["ACTION_939_play_sound_15"]),
        IncPaletteRowBy(15),
        Return(),
    ]
)
