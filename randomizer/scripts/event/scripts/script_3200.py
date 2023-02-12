# E3200_MINES_TRAMPOLINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7043_1),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AA),
        ActionQueueSync(
            target=MEM_70AA,
            subscript=[
                ASSequencePlaybackOn(),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=False),
                ASSetSequenceSpeed(NORMAL),
                ASPause(36),
                ASSetSequenceSpeed(FAST),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=6),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOff(),
                ASSetVRAMPriority(PRIORITY_3),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASFloatingOff(),
                ASSetWalkingSpeed(SLOW),
                ASShiftZDownPixels(3),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZDownPixels(1),
                ASSetWalkingSpeed(SLOW),
                ASShiftZDownPixels(4),
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftZDownPixels(2),
                ASPause(2),
                ASSetWalkingSpeed(SLOW),
                ASShiftZDownPixels(1),
                ASPause(9),
                ASSetWalkingSpeed(NORMAL),
                ASSequencePlaybackOn(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x10\x80\xff")),
                ASFloatingOn(),
                ASPause(12),
                ASBPL262728(),
                ASFloatingOff(),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetSpriteSequence(
                    index=5, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASWalkToXYCoords(x=7, y=49),
            ],
        ),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        StartAsyncEmbeddedActionScript(
            target=SCREEN_FOCUS,
            prefix=0xF1,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASStartLoopNTimes(2),
                ASShiftWestPixels(2),
                ASShiftNorthPixels(4),
                ASShiftEastPixels(2),
                ASShiftSouthPixels(1),
                ASShiftWestPixels(1),
                ASShiftSouthPixels(5),
                ASShiftEastPixels(1),
                ASShiftNorthPixels(2),
                ASEndLoop(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=MEM_70AA,
            prefix=0xF1,
            subscript=[
                ASPause(
                    1,
                    identifier="EVENT_3200_start_embedded_action_script_sync_F1_7_SUBSCRIPT_pause_0",
                ),
                ASJmpIfBitClear(
                    TEMP_7043_1,
                    [
                        "EVENT_3200_start_embedded_action_script_sync_F1_7_SUBSCRIPT_pause_0"
                    ],
                ),
                ASClearBit(TEMP_7043_1),
                ASSequenceLoopingOn(),
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=1, looping=False),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=6),
                ASPause(24),
                ASSetSequenceSpeed(NORMAL),
                ASResetProperties(),
                ASSequenceLoopingOff(),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASJumpToHeight(height=0, silent=True),
                ASResetProperties(),
                ASFaceNortheast(),
                ASPause(
                    1, identifier="EVENT_3200_action_queue_async_8_SUBSCRIPT_pause_3"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3200_action_queue_async_8_SUBSCRIPT_pause_3"]
                ),
                ASSetBit(TEMP_7043_1),
                ASSetWalkingSpeed(FAST),
                ASClearSolidityBits(cant_pass_npcs=True),
                ASFloatingOff(),
                ASShiftZDownPixels(8),
                ASPause(2),
                ASSetWalkingSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=7, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=108, silent=True),
                ASFloatingOn(),
                ASWalk1StepSouth(),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASSetSolidityBits(cant_pass_npcs=True),
            ],
        ),
        Pause(48),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=False
                ),
                ASPause(128),
                ASSetSequenceSpeed(VERY_FAST),
                ASSetSpriteSequence(
                    index=9, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPlaySound(sound=SO056_SHAKE_HEAD, channel=4),
                ASPause(24),
                ASSetSequenceSpeed(NORMAL),
                ASResetProperties(),
                ASFloatingOn(),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASClearBit(TEMP_7043_1),
            ],
        ),
        Return(),
    ]
)
