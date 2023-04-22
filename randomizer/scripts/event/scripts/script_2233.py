# pylint: disable=C0301

"""E2233_KEEP_1ST_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FadeInFromBlack(sync=False),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_2233_ret_8"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_2233_ret_8"]),
        RunEventAsSubroutine(E3914_KEEP_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_2233_ret_8"),
    ]
)
