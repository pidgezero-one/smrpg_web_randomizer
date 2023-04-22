# pylint: disable=C0301

"""E3344_VOLCANO_FINAL_TRAMPOLINE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            VOLCANO_TRAMPOLINE_ROOM_ANIMATION_COMPLETED, ["EVENT_3344_jmp_to_event_13"]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASVisibilityOff(),
                ASWalk1StepNortheast(),
            ],
        ),
        RunEventAsSubroutine(E0844_VOLCANO_EXIT_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftXYPixels(x=252, y=254),
                ASVisibilityOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(3),
                ASJumpToHeight(108),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASPause(8),
                ASWalk1StepSouthwest(),
                ASPause(
                    1, identifier="EVENT_3344_action_queue_sync_4_SUBSCRIPT_pause_9"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_3344_action_queue_sync_4_SUBSCRIPT_pause_9"]
                ),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASFloatingOff(),
                ASSetBit(TEMP_7043_0),
                ASSetWalkingSpeed(FAST),
                ASShiftZDownPixels(8),
                ASJumpToHeight(256),
                ASPause(10),
                ASFloatingOff(),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASShiftXYPixels(x=252, y=254),
                ASPause(30),
                ASVisibilityOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(3),
                ASJumpToHeight(108),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASPause(8),
                ASWalk1StepSouthwest(),
                ASPause(
                    1, identifier="EVENT_3344_action_queue_sync_5_SUBSCRIPT_pause_10"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_3344_action_queue_sync_5_SUBSCRIPT_pause_10"]
                ),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASFloatingOff(),
                ASSetBit(TEMP_7043_0),
                ASSetWalkingSpeed(FAST),
                ASShiftZDownPixels(8),
                ASJumpToHeight(256),
                ASPause(10),
                ASFloatingOff(),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASShiftXYPixels(x=252, y=254),
                ASPause(60),
                ASVisibilityOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(3),
                ASJumpToHeight(108),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASPause(8),
                ASWalk1StepSouthwest(),
                ASPause(
                    1, identifier="EVENT_3344_action_queue_sync_6_SUBSCRIPT_pause_10"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_3344_action_queue_sync_6_SUBSCRIPT_pause_10"]
                ),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASFloatingOff(),
                ASSetBit(TEMP_7043_0),
                ASSetWalkingSpeed(FAST),
                ASShiftZDownPixels(8),
                ASJumpToHeight(256),
                ASPause(10),
                ASFloatingOff(),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASShiftXYPixels(x=252, y=254),
                ASPause(90),
                ASVisibilityOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(3),
                ASJumpToHeight(108),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASPause(8),
                ASWalk1StepSouthwest(),
                ASPause(
                    1, identifier="EVENT_3344_action_queue_sync_7_SUBSCRIPT_pause_10"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_3344_action_queue_sync_7_SUBSCRIPT_pause_10"]
                ),
                ASSetBit(TEMP_7043_0),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASFloatingOff(),
                ASSetWalkingSpeed(FAST),
                ASShiftZDownPixels(8),
                ASJumpToHeight(256),
                ASPause(10),
                ASFloatingOff(),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASShiftXYPixels(x=252, y=254),
                ASPause(120),
                ASVisibilityOn(),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthwestSteps(3),
                ASJumpToHeight(108),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASSetSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASPause(8),
                ASWalk1StepSouthwest(),
                ASPause(
                    1, identifier="EVENT_3344_action_queue_sync_8_SUBSCRIPT_pause_10"
                ),
                ASJmpIfObjectInAir(
                    DUMMY_0X07, ["EVENT_3344_action_queue_sync_8_SUBSCRIPT_pause_10"]
                ),
                ASClearSolidityBits(cant_pass_npcs=True, bit_7=True),
                ASFloatingOff(),
                ASSetBit(TEMP_7043_0),
                ASSetWalkingSpeed(FAST),
                ASShiftZDownPixels(8),
                ASJumpToHeight(256),
                ASPause(10),
                ASFloatingOff(),
                ASVisibilityOff(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(4),
                ASPause(
                    1, identifier="EVENT_3344_action_queue_async_9_SUBSCRIPT_pause_1"
                ),
                ASJmpIfBitClear(
                    TEMP_7043_0, ["EVENT_3344_action_queue_async_9_SUBSCRIPT_pause_1"]
                ),
                ASSetSequenceSpeed(FASTEST),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASSetSpriteSequence(index=0, looping=False),
                ASPause(4),
                ASClearBit(TEMP_7043_0),
                ASEndLoop(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASVisibilityOn(),
                ASWalk1StepSouthwest(),
            ],
        ),
        SetBit(VOLCANO_TRAMPOLINE_ROOM_ANIMATION_COMPLETED),
        Return(),
        JmpToEvent(E0015_STANDARD_ROOM_LOADER, identifier="EVENT_3344_jmp_to_event_13"),
    ]
)
