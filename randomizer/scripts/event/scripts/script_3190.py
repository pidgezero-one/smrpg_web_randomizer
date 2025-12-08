# pylint: disable=C0301

"""E3190_ACTIVATE_POST_MINES_BOSS_FIRST_MINECART_SESSION_CONTINUED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(identifier="EVENT_3190_stop_all_background_events_0"),
        SetBit(MINECART_CLEARED),
        ClearBit(TOADOFSKY_REMOVED),
        ActionQueueSync(target=NPC_0, subscript=[ASSetVRAMPriority(NORMAL_PRIORITY)]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASClearSolidityBits(
                    cant_pass_walls=True, cant_pass_npcs=True, bit_7=True
                ),
                ASWalkToXYCoords(x=11, y=61),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFaceSoutheast(),
                ASFloatingOn(),
            ]),
        SetAsyncActionScript(NPC_1, A0015_DO_NOTHING),
        ActionQueueAsync(
            target=NPC_1, subscript=[ASWalkToXYCoords(x=12, y=61), ASFaceNorthwest()]
        ),
        SetVarToConst(TEMP_70AE, 21),
        SetTempAsyncActionScript(MARIO, A0670_NOD_YES),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASJumpToHeight(54),
                ASPause(20),
                ASJumpToHeight(54),
                ASPause(30),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASResetProperties(),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASWalk1StepNortheast(),
                ASFixedFCoordOff(),
                ASPause(
                    1, identifier="EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_5"
                ),
                ASJmpIfBitClear(
                    TEMP_7044_6, ["EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_5"]
                ),
                ASSetWalkingSpeed(FAST),
                ASSequenceLoopingOff(),
                ASSequencePlaybackOff(),
                ASWalkSoutheastPixels(3),
                ASWalkSouthPixels(6),
                ASWalkSouthwestPixels(12),
                ASWalkWestPixels(8),
                ASShiftZUpPixels(20),
                ASPause(16),
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASShadowOff(),
                ASBounceToXYWithHeight(x=12, y=62, height=2),
                ASWalkSouthwestPixels(4),
                ASWalkNortheastPixels(0),
                ASShiftZDownPixels(3),
                ASFixedFCoordOff(),
                ASClearSolidityBits(bit_4=True, cant_walk_through=True),
                ASFloatingOff(),
                ASPause(
                    1, identifier="EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_25"
                ),
                ASJmpIfBitClear(
                    TEMP_7044_5, ["EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_25"]
                ),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0]),
                ASSetVRAMPriority(PRIORITY_3),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(108),
                ASWalkToXYCoords(x=12, y=61),
                ASPause(20),
                ASFaceNortheast(),
                ASPause(20),
                ASSetBit(TEMP_7044_6),
                ASFaceEast(),
                ASPause(6),
                ASFaceSoutheast(),
                ASPause(6),
                ASFaceSouth(),
                ASPause(8),
                ASSetSpriteSequence(index=5, is_sequence=True, looping=True),
                ASPause(16),
                ASSetSpriteSequence(
                    index=9, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASPause(20),
                ASResetProperties(),
                ASFaceSouthwest(),
                ASPause(16),
                ASFaceNortheast(),
                ASWalk1StepNortheast(),
                ASSetBit(TEMP_7044_2),
                ASPause(
                    1, identifier="EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_22"
                ),
                ASJmpIfBitClear(
                    TEMP_7044_1, ["EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_22"]
                ),
                ASFaceSouthwest(),
                ASWalk1StepSouthwest(),
                ASPause(16),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASJumpToHeight(108),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(SLOW),
                ASWalkSouthwestPixels(9),
                ASShadowOff(),
                ASPause(8),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASFloatingOff(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=5, sprite_offset=6, is_sequence=True, looping=True
                ),
                ASSetBit(TEMP_7044_5),
            ]),
        Pause(1, identifier="EVENT_3190_pause_12"),
        JmpIfBitClear(TEMP_7044_2, ["EVENT_3190_pause_12"]),
        SetBit(TEMP_7044_1),
        Pause(1, identifier="EVENT_3190_pause_15"),
        RunEventAsSubroutine(E0186_PARTY_JOIN_LOGIC),
        JmpIfBitClear(TEMP_7044_5, ["EVENT_3190_pause_15"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=7, is_sequence=True, looping=True),
                ASPause(8),
                ASDb(bytearray(b" \x03")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASPlaySound(sound=SO048_MINECART_START, channel=4),
                ASPause(200),
            ]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(8),
                ASDb(bytearray(b" \x07")),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"&\x00\x00\xfe\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"'\x00\x00\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"
                    )
                ),
                ASEmbeddedAnimationRoutine(
                    bytearray(
                        b"(\x00\x00\x00\x00\x00\x00\x10\x00\x00\x01\x00\x00\x00\x04\x80"
                    )
                ),
                ASPause(200),
                ASSetBit(TEMP_7043_0),
            ]),
        Pause(1, identifier="EVENT_3190_pause_19"),
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3190_pause_19"]),
        CloseDialog(),
        FadeOutToBlack(sync=False),
        RemoveObjectFromSpecificLevel(
            NPC_1, R284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM
        ),
        Set7000ToMinecartTimer(),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_702E),
        JmpIfBitClear(
            SKIP_MANDATORY_MINECART, ["EVENT_3190_run_moleville_mountain_sequence_42"]
        ),
        JmpIfBitClear(OPTIONAL_MINECART_CLEARED, ["EVENT_3190_enter_area_43"]),
        RunMolevilleMountainSequence(
            identifier="EVENT_3190_run_moleville_mountain_sequence_42"
        ),
        EnterArea(
            room_id=R108_MOLEVILLE_OUTSIDE,
            face_direction=SOUTH,
            x=0,
            y=0,
            z=0,
            identifier="EVENT_3190_enter_area_43"),
        RunEventAsSubroutine(E1394_FOUR_DIGIT_COIN_VALUE_HANDLER),
        SetBit(TEMP_7044_6),
        JmpToEvent(E1648_MINECART_ENDING),
    ]
)
