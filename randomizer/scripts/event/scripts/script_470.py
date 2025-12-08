# pylint: disable=C0301

"""E0470_GREEN_YOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
        JmpIfBitSet(UNKNOWN_MUSHROOM_DERBY_7085_4, ["EVENT_256_ret_0"]),
        JmpIfMarioOnAnObjectOrNot(
            ["EVENT_470_jmp_if_bit_set_32", "EVENT_470_jmp_if_bit_set_32"]
        ),
        JmpIfBitSet(TEMP_7044_4, ["EVENT_470_action_queue_async_28"]),
        Jmp(["EVENT_470_play_sound_10"]),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        PlaySound(
            sound=SO063_YOSHI_TALK, channel=6, identifier="EVENT_470_play_sound_10"
        ),
        UnsyncDialog(),
        CloseDialog(),
        RunEventAsSubroutine(E3587_SET_70AE_TO_70A8),
        Jmp(["EVENT_470_pause_action_script_18"]),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        PauseActionScript(NPC_9, identifier="EVENT_470_pause_action_script_18"),
        SetSyncActionScript(NPC_9, A0119_SLOW_SEQUENCE_LOOP),
        StartAsyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASSet700CToObjectCoord(target_npc=NPC_9, coord=COORD_F, pixel=True),
                ASAddConstToVar(PRIMARY_TEMP_700C, 4),
                ASMem700CAndConst(0x0007),
                ASFaceEast7C(),
                ASCopyVarToVar(from_var=PRIMARY_TEMP_700C, to_var=ROSE_WAY_703E),
                ASFixedFCoordOn(),
            ],
            identifier="EVENT_470_start_embedded_action_script_async_F1_20"),
        SetBit(TEMP_7044_4),
        Return(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        StopSound(),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[ASFixedFCoordOff(), ASFaceMario()],
            identifier="EVENT_470_action_queue_async_28"),
        PlaySound(sound=SO063_YOSHI_TALK, channel=6),
        RunDialog(
            dialog_id=DI0900_YOSHI_AFTER_YOU_ENABLE_HIM,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Jmp(["EVENT_470_start_embedded_action_script_async_F1_20"]),
        JmpIfBitSet(
            TEMP_7044_4,
            ["EVENT_470_pause_action_script_34"],
            identifier="EVENT_470_jmp_if_bit_set_32"),
        Return(),
        PauseActionScript(MARIO, identifier="EVENT_470_pause_action_script_34"),
        PauseActionScript(NPC_9),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
            ]),
        Db(bytearray(b"\xfdE")),
        FreezeCamera(),
        SetBit(TEMP_7044_5),
        SetBit(TEMP_7044_4),
        Db(bytearray(b"\xc7\x9d")),
        AddConstToVar(Z_COORD_2, 1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(FASTEST),
                ASFixedFCoordOn(),
                ASDb(bytearray(b"\x98")),
                ASVisibilityOff(),
                ASJmp(["EVENT_470_non_embedded_action_queue_46"]),
            ]),
        ActionQueueAsync(target=NPC_9, subscript=[ASFixedFCoordOff()]),
        Jmp(["EVENT_470_action_queue_async_47"]),
        NonEmbeddedActionQueue(
            subscript=[
                ASPlaySound(sound=SO063_YOSHI_TALK, channel=4),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    1,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_10"
                    ]),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    2,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_12"
                    ]),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    3,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_14"
                    ]),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    4,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_16"
                    ]),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    5,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_18"
                    ]),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    6,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_20"
                    ]),
                ASJmpIfVarEqualsConst(
                    ROSE_WAY_703E,
                    7,
                    [
                        "EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_22"
                    ]),
                ASSetSpriteSequence(
                    index=4,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_10"),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=2,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_12"),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_14"),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=4,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_16"),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_18"),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=3,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_20"),
                ASJmp(
                    ["EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"]
                ),
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=False,
                    mirror_sprite=True,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_sprite_sequence_22"),
                ASSetVarToConst(
                    Z_COORD_2,
                    0,
                    identifier="EVENT_470_non_embedded_action_queue_46_SUBSCRIPT_set_short_23"),
                ASDb(bytearray(b"\x9a")),
                ASVisibilityOn(),
                ASFixedFCoordOff(),
                ASSequencePlaybackOff(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASShadowOff(),
                ASReturn(),
            ],
            identifier="EVENT_470_non_embedded_action_queue_46"),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[ASTransferToObjectXY(MARIO), ASSequenceLoopingOff()],
            identifier="EVENT_470_action_queue_async_47"),
        RememberLastObject(),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=3),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=5),
        ApplySolidityModToLevel(permanent=True, room_id=R034_YOSTER_ISLE, mod_id=7),
        RunBackgroundEvent(
            event_id=E0469_YOSTER_ISLE_BACKGROUND, return_on_level_exit=True, bit_7=True
        ),
        Return(),
    ]
)
