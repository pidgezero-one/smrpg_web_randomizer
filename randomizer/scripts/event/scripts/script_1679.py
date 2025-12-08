# pylint: disable=C0301

"""E1679_LANDS_END_TRAMPOLINE_IN_LOWER_UNDERGROUND_GECKO_ROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0065_TRAMPOLINE_SUBROUTINE),
        EnterArea(
            room_id=R265_LANDS_END_UNDERGROUND_AREA_03,
            face_direction=SOUTH,
            x=22,
            y=93,
            z=4),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASJumpToHeight(height=144, silent=True),
                ASWalk1StepSouth(),
                ASFloatingOn(),
                ASPause(
                    1, identifier="EVENT_1679_action_queue_async_3_SUBSCRIPT_pause_4"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1679_action_queue_async_3_SUBSCRIPT_pause_4"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ]),
        Return(),
    ]
)
