# pylint: disable=C0301

"""E3898_BOOSTER_PASS_STAR_PIECE_SIGNAL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(SIGNAL_RING_BIT),
        Return(),
        PlaySound(sound=SO149_CASINO_SECRET_PASSAGE, channel=6),
        ClearBit(SIGNAL_RING_BIT),
        Return(),
    ]
)
