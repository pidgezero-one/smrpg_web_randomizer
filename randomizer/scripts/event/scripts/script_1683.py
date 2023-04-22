# pylint: disable=C0301

"""E1683_TEMPLE_EXIT_WARP_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(
            TRAMPOLINE_SHAMAN_PAID, ["EVENT_1682_set_7000_to_70A0_short_mem_0"]
        ),
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1583_action_queue_sync_6"]),
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R319_LANDS_END_DESERT_AREA_06, face_direction=NORTH, x=7, y=118, z=0
        ),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOff(),
                ASJumpToHeight(height=144, silent=True),
                ASWalk1StepNorth(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_1683_action_queue_sync_5_SUBSCRIPT_pause_6"
                ),
                ASJmpIfMarioInAir(["EVENT_1683_action_queue_sync_5_SUBSCRIPT_pause_6"]),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        SetBit(TEMP_7044_6),
        JmpToEvent(E1783_LANDS_END_FINAL_WHIRLPOOL_ROOM_LOADER),
    ]
)
