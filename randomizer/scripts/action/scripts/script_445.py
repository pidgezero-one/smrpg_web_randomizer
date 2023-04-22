"""A0445_ROSE_WAY_STARSLAP"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetPriority(3, identifier="ACTION_445_set_priority_0"),
        Set700CToPressedButton(),
        CompareVarToConst(PRIMARY_TEMP_700C, 33),
        JmpIfComparisonResultIsGreaterOrEqual(["ACTION_445_set_object_memory_bits_51"]),
        Pause(91, identifier="ACTION_445_pause_4"),
        JmpIfRandom1of2(["ACTION_445_pause_4"]),
        Pause(55),
        JmpIfVarNotEqualsConst(TEMP_70AF, 0, ["ACTION_445_pause_4"]),
        Set700CToPressedButton(),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AF),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_445_set_short_15"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 31, ["ACTION_445_set_short_17"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 32, ["ACTION_445_set_short_19"]),
        SetVarToConst(ROSE_WAY_7038, 1),
        Jmp(["ACTION_445_pause_20"]),
        SetVarToConst(ROSE_WAY_703A, 1, identifier="ACTION_445_set_short_15"),
        Jmp(["ACTION_445_pause_20"]),
        SetVarToConst(ROSE_WAY_703C, 1, identifier="ACTION_445_set_short_17"),
        Jmp(["ACTION_445_pause_20"]),
        SetVarToConst(ROSE_WAY_703E, 1, identifier="ACTION_445_set_short_19"),
        Pause(328, identifier="ACTION_445_pause_20"),
        ShiftZUpSteps(3),
        Db(bytearray(b" \x03")),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00\x00\x00\x00\x00\x01 \x00\x00\x02\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00@\x00\x00\x00\x01 \x00\x00\x02\x80")
        ),
        Pause(512),
        EmbeddedAnimationRoutine(
            bytearray(b"&\x00\x00\x00\x00\x00\x00\x00@\x00\x01\xe0\xff\x00\x02\x80")
        ),
        EmbeddedAnimationRoutine(
            bytearray(b"'\x00\x00\x00\x00\x00@\x00@\x00\x01\xe0\xff\x00\x02\x80")
        ),
        Pause(512),
        BPL262728(),
        Set700CToPressedButton(),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_70AF),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 30, ["ACTION_445_set_short_39"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 31, ["ACTION_445_set_short_43"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 32, ["ACTION_445_set_short_47"]),
        SetVarToConst(ROSE_WAY_7038, 2),
        BounceToXYWithHeight(x=8, y=40, height=0),
        SetVarToConst(ROSE_WAY_7038, 0),
        Jmp(["ACTION_445_set_priority_0"]),
        SetVarToConst(ROSE_WAY_703A, 2, identifier="ACTION_445_set_short_39"),
        BounceToXYWithHeight(x=17, y=42, height=0),
        SetVarToConst(ROSE_WAY_703A, 0),
        Jmp(["ACTION_445_set_priority_0"]),
        SetVarToConst(ROSE_WAY_703C, 2, identifier="ACTION_445_set_short_43"),
        BounceToXYWithHeight(x=14, y=26, height=0),
        SetVarToConst(ROSE_WAY_703C, 0),
        Jmp(["ACTION_445_set_priority_0"]),
        SetVarToConst(ROSE_WAY_703E, 2, identifier="ACTION_445_set_short_47"),
        BounceToXYWithHeight(x=23, y=38, height=0),
        SetVarToConst(ROSE_WAY_703E, 0),
        Jmp(["ACTION_445_set_priority_0"]),
        SetObjectMemoryBits(
            arg_1=0x0E, bits=[2], identifier="ACTION_445_set_object_memory_bits_51"
        ),
        IncPaletteRowBy(1),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        SetPriority(2),
        Pause(55),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 34, ["ACTION_445_pause_63"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 35, ["ACTION_445_pause_66"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 36, ["ACTION_445_pause_69"]),
        Pause(1, identifier="ACTION_445_pause_60"),
        JmpIfVarNotEqualsConst(ROSE_WAY_7038, 1, ["ACTION_445_pause_60"]),
        Jmp(["ACTION_445_set_sprite_sequence_71"]),
        Pause(1, identifier="ACTION_445_pause_63"),
        JmpIfVarNotEqualsConst(ROSE_WAY_703A, 1, ["ACTION_445_pause_63"]),
        Jmp(["ACTION_445_set_sprite_sequence_71"]),
        Pause(1, identifier="ACTION_445_pause_66"),
        JmpIfVarNotEqualsConst(ROSE_WAY_703C, 1, ["ACTION_445_pause_66"]),
        Jmp(["ACTION_445_set_sprite_sequence_71"]),
        Pause(1, identifier="ACTION_445_pause_69"),
        JmpIfVarNotEqualsConst(ROSE_WAY_703E, 1, ["ACTION_445_pause_69"]),
        SetSpriteSequence(
            index=4,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_445_set_sprite_sequence_71",
        ),
        Pause(256),
        SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
        Pause(6),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        Pause(6),
        SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
        Pause(6),
        SetSpriteSequence(index=4, is_mold=True, is_sequence=True, looping=True),
        Pause(6),
        SetSpriteSequence(index=5, is_mold=True, is_sequence=True, looping=True),
        Pause(48),
        CreatePacketAtObjectCoords(
            packet=P030_WATER_SPLASH_DROPS_SFX,
            target_npc=DUMMY_0X07,
            destinations=["ACTION_445_set_sprite_sequence_84"],
        ),
        SetSpriteSequence(
            index=5,
            is_sequence=True,
            looping=True,
            identifier="ACTION_445_set_sprite_sequence_84",
        ),
        SetPriority(3),
        IncPaletteRowBy(15),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 34, ["ACTION_445_pause_94"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 35, ["ACTION_445_pause_97"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 36, ["ACTION_445_pause_100"]),
        Pause(1, identifier="ACTION_445_pause_91"),
        JmpIfVarNotEqualsConst(ROSE_WAY_7038, 2, ["ACTION_445_pause_91"]),
        Jmp(["ACTION_445_set_sprite_sequence_102"]),
        Pause(1, identifier="ACTION_445_pause_94"),
        JmpIfVarNotEqualsConst(ROSE_WAY_703A, 2, ["ACTION_445_pause_94"]),
        Jmp(["ACTION_445_set_sprite_sequence_102"]),
        Pause(1, identifier="ACTION_445_pause_97"),
        JmpIfVarNotEqualsConst(ROSE_WAY_703C, 2, ["ACTION_445_pause_97"]),
        Jmp(["ACTION_445_set_sprite_sequence_102"]),
        Pause(1, identifier="ACTION_445_pause_100"),
        JmpIfVarNotEqualsConst(ROSE_WAY_703E, 2, ["ACTION_445_pause_100"]),
        SetSpriteSequence(
            index=6,
            is_mold=True,
            is_sequence=True,
            looping=True,
            identifier="ACTION_445_set_sprite_sequence_102",
        ),
        SetObjectMemoryBits(arg_1=0x0E, bits=[]),
        Set700CToPressedButton(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 34, ["ACTION_445_bounce_to_xy_with_height_110"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 35, ["ACTION_445_bounce_to_xy_with_height_112"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 36, ["ACTION_445_bounce_to_xy_with_height_114"]
        ),
        BounceToXYWithHeight(x=8, y=40, height=0),
        Jmp(["ACTION_445_create_packet_at_npc_coords_115"]),
        BounceToXYWithHeight(
            x=17, y=42, height=0, identifier="ACTION_445_bounce_to_xy_with_height_110"
        ),
        Jmp(["ACTION_445_create_packet_at_npc_coords_115"]),
        BounceToXYWithHeight(
            x=14, y=26, height=0, identifier="ACTION_445_bounce_to_xy_with_height_112"
        ),
        Jmp(["ACTION_445_create_packet_at_npc_coords_115"]),
        BounceToXYWithHeight(
            x=23, y=38, height=0, identifier="ACTION_445_bounce_to_xy_with_height_114"
        ),
        CreatePacketAtObjectCoords(
            packet=P030_WATER_SPLASH_DROPS_SFX,
            target_npc=DUMMY_0X07,
            destinations=["ACTION_445_jmp_116"],
            identifier="ACTION_445_create_packet_at_npc_coords_115",
        ),
        Jmp(["ACTION_445_set_object_memory_bits_51"], identifier="ACTION_445_jmp_116"),
    ]
)
