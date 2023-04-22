# pylint: disable=C0301

"""E3919_BOOSTER_PASS_BACK_ENTRANCE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunEventAsSubroutine(E0015_STANDARD_ROOM_LOADER),
        JmpIfBitClear(SIGNAL_RING_DIRECTIONAL_BIT, ["EVENT_3919_ret_26"]),
        RunEventAsSubroutine(E3588_SIGNAL_RING_ACTIVATOR),
        JmpIfBitClear(SIGNAL_RING_BIT, ["EVENT_3919_ret_26"]),
        RunEventAsSubroutine(E3898_BOOSTER_PASS_STAR_PIECE_SIGNAL),
        Return(identifier="EVENT_3919_ret_26"),
    ]
)
