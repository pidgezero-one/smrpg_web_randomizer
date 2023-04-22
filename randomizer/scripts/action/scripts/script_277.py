"""A0277_VOLCANO_HOMING_FIREBALL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        VisibilityOff(identifier="ACTION_277_visibility_off_0"),
        Set700CToCurrentLevel(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_700C, 389, ["ACTION_277_clear_solidity_bits_4"]
        ),
        SetPriority(2),
        ClearSolidityBits(
            bit_4=True,
            cant_walk_through=True,
            identifier="ACTION_277_clear_solidity_bits_4",
        ),
        ObjectMemorySetBit(arg_1=0x30, bits=[4]),
        SequenceLoopingOn(),
        SetWalkingSpeed(NORMAL),
        JmpIfBitSet(TEMP_7044_3, ["ACTION_277_set_700C_to_pressed_button_10"]),
        JmpIfObjectWithinRangeSameZ(
            comparing_npc=MARIO,
            usually=0,
            tiles=5,
            destinations=["ACTION_277_reset_properties_59"],
        ),
        Set700CToPressedButton(identifier="ACTION_277_set_700C_to_pressed_button_10"),
        Mem700CAndConst(0x0007),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 7, ["ACTION_277_pause_26"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 6, ["ACTION_277_pause_25"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 5, ["ACTION_277_pause_24"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 4, ["ACTION_277_pause_23"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 3, ["ACTION_277_pause_22"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 2, ["ACTION_277_pause_21"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_700C, 1, ["ACTION_277_pause_20"]),
        Pause(5),
        Pause(9, identifier="ACTION_277_pause_20"),
        Pause(13, identifier="ACTION_277_pause_21"),
        Pause(19, identifier="ACTION_277_pause_22"),
        Pause(23, identifier="ACTION_277_pause_23"),
        Pause(17, identifier="ACTION_277_pause_24"),
        Pause(11, identifier="ACTION_277_pause_25"),
        Pause(7, identifier="ACTION_277_pause_26"),
        VisibilityOn(),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        PlaySound(sound=SO084_SMOKED, channel=4),
        FaceMario(),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 7, ["ACTION_277_set_sprite_sequence_37"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_277_set_sprite_sequence_37"]
        ),
        SetSpriteSequence(index=8, is_sequence=True, looping=True),
        Jmp(["ACTION_277_pause_38"]),
        SetSpriteSequence(
            index=8,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_277_set_sprite_sequence_37",
        ),
        Pause(8, identifier="ACTION_277_pause_38"),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 7, ["ACTION_277_set_sprite_sequence_44"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_277_set_sprite_sequence_44"]
        ),
        SetSpriteSequence(index=9, is_sequence=True, looping=True),
        Jmp(["ACTION_277_jump_to_height_silent_45"]),
        SetSpriteSequence(
            index=9,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_277_set_sprite_sequence_44",
        ),
        JumpToHeight(
            height=180, silent=True, identifier="ACTION_277_jump_to_height_silent_45"
        ),
        Pause(28),
        ResetProperties(),
        SequenceLoopingOn(),
        Pause(2, identifier="ACTION_277_pause_49"),
        JmpIfObjectInAir(DUMMY_0X07, ["ACTION_277_pause_49"]),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 7, ["ACTION_277_set_sprite_sequence_56"]
        ),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_700C, 1, ["ACTION_277_set_sprite_sequence_56"]
        ),
        SetSpriteSequence(index=8, is_sequence=True, looping=True),
        Jmp(["ACTION_277_pause_57"]),
        SetSpriteSequence(
            index=8,
            is_sequence=True,
            looping=True,
            mirror_sprite=True,
            identifier="ACTION_277_set_sprite_sequence_56",
        ),
        Pause(4, identifier="ACTION_277_pause_57"),
        Jmp(["ACTION_277_visibility_off_0"]),
        ResetProperties(identifier="ACTION_277_reset_properties_59"),
        VisibilityOn(),
        SetSolidityBits(bit_4=True, cant_walk_through=True),
        ObjectMemoryClearBit(arg_1=0x30, bits=[4]),
        Db(bytearray(b" \x07")),
        EmbeddedAnimationRoutine(
            bytearray(b"(\x00\x00\x00\x00\x00\x00\x00\x14\x00\x01\x00\x00\x80\x03\x80")
        ),
        Db(bytearray(b"/\x00\x08\x80\x00\x01\x00")),
        FaceMario(identifier="ACTION_277_face_mario_66"),
        Set700CToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True),
        AddConstToVar(PRIMARY_TEMP_700C, 256),
        CopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=TEMP_7028),
        Set700CToObjectCoord(target_npc=DUMMY_0X07, coord=COORD_Z, pixel=True),
        Compare700CToVar(TEMP_7028),
        JmpIfLoadedMemoryIs0(["ACTION_277_pause_75"]),
        JmpIfLoadedMemoryIsBelow0(["ACTION_277_shift_z_down_pixels_77"]),
        JmpIfLoadedMemoryIsAboveOrEqual0(["ACTION_277_shift_z_up_pixels_79"]),
        Pause(1, identifier="ACTION_277_pause_75"),
        Jmp(["ACTION_277_face_mario_66"]),
        ShiftZDownPixels(1, identifier="ACTION_277_shift_z_down_pixels_77"),
        Jmp(["ACTION_277_face_mario_66"]),
        ShiftZUpPixels(1, identifier="ACTION_277_shift_z_up_pixels_79"),
        Jmp(["ACTION_277_face_mario_66"]),
    ]
)
