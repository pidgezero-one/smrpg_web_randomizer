# pylint: disable=C0301

"""E3372_KEEP_GET_CRUSHED_BY_HUGE_THWOMP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToBackgroundThread2(),
        JmpIfMarioOnAnObjectOrNot(["EVENT_3372_ret_29", "EVENT_3372_set_bit_7"]),
        SetBit(TEMP_7044_7),
        ResumeActionScript(MEM_70A8),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xfd\x9ci")),
                ASSet700CToObjectCoord(
                    target_npc=DUMMY_0X07, coord=COORD_F, pixel=True
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    7,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_10"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_10"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_12"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    2,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_12"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    3,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_14"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    4,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_14"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_16"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    6,
                    [
                        "EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_16"
                    ]),
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_10"),
                ASJmp(
                    ["EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18"]
                ),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_12"),
                ASJmp(
                    ["EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18"]
                ),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_14"),
                ASJmp(
                    ["EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18"]
                ),
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3372_action_queue_async_4_SUBSCRIPT_set_sprite_sequence_16"),
                ASJmp(
                    ["EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18"]
                ),
                ASFixedFCoordOn(
                    identifier="EVENT_3372_action_queue_async_4_SUBSCRIPT_fixed_f_coord_on_18"
                ),
                ASSetWalkingSpeed(FAST),
                ASTurnClockwise45DegreesNTimes(4),
                ASWalkFDirectionSteps(2),
                ASTurnClockwise45DegreesNTimes(4),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
                ASResetProperties(),
            ]),
        ClearBit(TEMP_7044_7),
        Return(),
        SetBit(TEMP_7044_7, identifier="EVENT_3372_set_bit_7"),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AB),
        ActionQueueSync(
            target=MEM_70AB,
            subscript=[
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZDownSteps(4),
                ASSetWalkingSpeed(FAST),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[1]),
                ASSetSolidityBits(bit_4=True, cant_walk_through=True),
            ]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASSetObjectMemoryBits(arg_1=0x0B, bits=[0, 1]),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZDownSteps(4),
                ASSet700CToObjectCoord(
                    target_npc=DUMMY_0X07, coord=COORD_F, pixel=True
                ),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    7,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_14"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    0,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_14"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    1,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_20"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    2,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_20"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    3,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_18"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    4,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_18"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    5,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_16"
                    ]),
                ASJmpIfVarEqualsConst(
                    PRIMARY_TEMP_700C,
                    6,
                    [
                        "EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_16"
                    ]),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_14"),
                ASJmp(["EVENT_3372_resume_action_script_12"]),
                ASSetSpriteSequence(
                    index=8,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_16"),
                ASJmp(["EVENT_3372_resume_action_script_12"]),
                ASSetSpriteSequence(
                    index=1,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    identifier="EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_18"),
                ASJmp(["EVENT_3372_resume_action_script_12"]),
                ASSetSpriteSequence(
                    index=1,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                    identifier="EVENT_3372_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_20"),
                ASJmp(["EVENT_3372_resume_action_script_12"]),
            ]),
        ResumeActionScript(MEM_70AB, identifier="EVENT_3372_resume_action_script_12"),
        SetVarToConst(SECONDARY_TEMP_7024, 0),
        Pause(1, identifier="EVENT_3372_pause_14"),
        Set7000ToTappedButton(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_3372_inc_short_19"]),
        Inc(SECONDARY_TEMP_7024),
        JmpIfVarEqualsConst(
            SECONDARY_TEMP_7024, 0, ["EVENT_3372_action_queue_async_23"]
        ),
        Inc(SECONDARY_TEMP_7024, identifier="EVENT_3372_inc_short_19"),
        Inc(SECONDARY_TEMP_7024),
        CompareVarToConst(SECONDARY_TEMP_7024, 120),
        JmpIfComparisonResultIsLesser(["EVENT_3372_pause_14"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSetWalkingSpeed(VERY_FAST),
                ASResetProperties(),
                ASFixedFCoordOn(),
                ASTurnClockwise45DegreesNTimes(4),
                ASWalk1StepFDirection(),
                ASTurnClockwise45DegreesNTimes(4),
                ASFixedFCoordOff(),
                ASSetWalkingSpeed(NORMAL),
            ],
            identifier="EVENT_3372_action_queue_async_23"),
        CopyVarToVar(from_var=TEMP_70AB, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetSolidityBits(cant_pass_npcs=True, bit_7=True)]
        ),
        ClearBit(TEMP_7044_7),
        Return(identifier="EVENT_3372_ret_29"),
    ]
)
