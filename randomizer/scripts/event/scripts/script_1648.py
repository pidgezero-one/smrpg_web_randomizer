# pylint: disable=C0301

"""E1648_MINECART_ENDING"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, OW24_MOLEVILLE),
        JmpIfBitSet(TEMP_7044_6, ["EVENT_1648_set_bit_15"]),
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1648_fade_in_from_black_sync_9"]),
        FadeInFromBlack(sync=False),
        StartLoopNTimes(249),
        PlaySound(sound=SO001_MENU_SELECT, channel=6),
        Pause(4),
        EndLoop(),
        Return(),
        FadeInFromBlack(sync=True, identifier="EVENT_1648_fade_in_from_black_sync_9"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASJumpToHeight(height=192, silent=True),
                ASWalk1StepSouth(),
                ASFloatingOn(),
            ]),
        Pause(1, identifier="EVENT_1648_pause_11"),
        JmpIfMarioInAir(["EVENT_1648_pause_11"]),
        PlaySound(sound=SO058_INSERT, channel=6),
        Return(),
        SetBit(MINECART_CRASH_CUTSCENE_CLEARED, identifier="EVENT_1648_set_bit_15"),
        JmpIfBitSet(OPTIONAL_MINECART_CLEARED, ["EVENT_1648_clear_bit_18"]),
        JmpToEvent(E1651_MARIO_CRASH_THRU_MOLEVILLE_ROOF),
        ClearBit(PAID_FOR_MINECART, identifier="EVENT_1648_clear_bit_18"),
        EnterArea(
            room_id=R108_MOLEVILLE_OUTSIDE,
            face_direction=SOUTHWEST,
            x=28,
            y=39,
            z=4,
            run_entrance_event=True),
        Return(),
    ]
)
