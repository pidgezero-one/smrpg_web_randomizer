# pylint: disable=C0301

"""E3918_FOREST_MAZE_ENTRANCE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3918_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3918_ret_26"]),
        RunEventAsSubroutine(E3896_FOREST_MAZE_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3918_ret_26"),
    ]
)
