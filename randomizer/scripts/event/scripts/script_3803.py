# pylint: disable=C0301

"""E3803_ENDING_CREDITS_GREEN_STAR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(8),
        RunEventSequence(scene=SC13_RUN_STAR_PIECE_END_SEQUENCE, value=1),
        Pause(8),
        JmpToEvent(E2629_ENDING_CREDITS_KEEP_OPENER),
    ]
)
