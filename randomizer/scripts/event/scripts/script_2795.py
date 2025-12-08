# pylint: disable=C0301

"""E2795_STAR_HILL_PROGRESS_SIGN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3324_TO_STAR_HILL,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpIfBitSet(UNKNOWN_7091_7, ["EVENT_2795_ret_4"]),
        SetBit(UNKNOWN_7091_7),
        RunDialog(
            dialog_id=DI3322_STAR_HILL_TUTORIAL,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        Return(identifier="EVENT_2795_ret_4"),
    ]
)
