# pylint: disable=C0301

"""E1583_LANDS_END_UNDERGROUND_TRAMPOLINE_TO_DESERT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1583_action_queue_sync_6"]),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R319_LANDS_END_DESERT_AREA_06, face_direction=SOUTH, x=8, y=110, z=0
        ),
        SetVarToConst(ACTIVE_NPC, 20),
        RunEventAsSubroutine(E1545_SAND_WHIRLPOOL),
        JmpToEvent(E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER),
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
            identifier="EVENT_1583_action_queue_sync_6"),
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
                ASJumpToHeight(height=108, silent=True),
                ASSetSolidityBits(cant_pass_npcs=True),
                ASSetVRAMPriority(NORMAL_PRIORITY),
                ASWalk1StepSouth(),
                ASPause(
                    1, identifier="EVENT_1583_action_queue_async_7_SUBSCRIPT_pause_21"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1583_action_queue_async_7_SUBSCRIPT_pause_21"]
                ),
            ]),
        Return(),
    ]
)
