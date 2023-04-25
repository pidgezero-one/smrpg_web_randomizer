# pylint: disable=C0301

"""E3290_SHIP_COLLECT_3D_MAZE_PRIZE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_MAZE_PRIZE, ["EVENT_3290_ret_10"]),
        SetBit(SHIP_MAZE_PRIZE),
        StopAllBackgroundEvents(),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        Pause(120),
        RunBackgroundEvent(
            event_id=E3212_SHIP_3D_MAZE_FORFEIT_LISTENER, return_on_level_exit=True
        ),
        RunDialog(
            dialog_id=DI1657_3D_MAZE_OVERLAY,
            above_object=BOWSER,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
        ),
        Return(identifier="EVENT_3290_ret_10"),
    ]
)
