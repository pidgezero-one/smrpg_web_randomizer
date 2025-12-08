# pylint: disable=C0301

"""E3478_MIDAS_RIVER_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7043_0, ["EVENT_3478_action_queue_sync_7"]),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        ClearBit(TEMP_7043_0),
        ClearBit(UNKNOWN_MIDAS_RIVER_7079_1),
        ClearBit(UNKNOWN_MIDAS_RIVER_704D_6),
        EnterArea(
            room_id=R069_MIDAS_RIVER_WATERFALL,
            face_direction=SOUTH,
            x=9,
            y=108,
            z=0,
            run_entrance_event=True),
        Return(),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(index=0, looping=False),
                ASSetSequenceSpeed(NORMAL),
                ASPause(36),
                ASSetSequenceSpeed(FAST),
                ASPlaySound(sound=SO010_TRAMPOLINE, channel=4),
                ASPause(5),
                ASSequenceLoopingOff(),
            ],
            identifier="EVENT_3478_action_queue_sync_7"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOff(),
                ASSetVRAMPriority(PRIORITY_3),
                ASClearSolidityBits(cant_pass_npcs=True),
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
                ASJumpToHeight(height=96, silent=True),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASWalkToXYCoords(x=21, y=35),
                ASJmpIfBitSet(BUCKET_WARP_BIT, ["EVENT_3478_jmp_if_bit_set_9"]),
                ASFaceWest(),
            ]),
        JmpIfBitSet(
            BUCKET_WARP_BIT,
            ["EVENT_3478_ret_14"],
            identifier="EVENT_3478_jmp_if_bit_set_9"),
        Pause(20),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASFaceSoutheast(),
                ASSetAllSpeeds(FAST),
                ASStartLoopNTimes(2),
                ASShiftZUpPixels(4),
                ASShiftZDownPixels(4),
                ASEndLoop(),
                ASWalkSoutheastSteps(2),
                ASWalkEastPixels(16),
                ASFaceSoutheast(),
                ASSetAllSpeeds(NORMAL),
            ]),
        RunEventAsSubroutine(E3479_MIDAS_RIVER_SCORE_SUBMISSION),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkWestPixels(16),
                ASWalkNorthwestSteps(2),
                ASFaceSoutheast(),
                ASSetAllSpeeds(NORMAL),
            ]),
        Return(identifier="EVENT_3478_ret_14"),
    ]
)
