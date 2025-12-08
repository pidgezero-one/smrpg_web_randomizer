# pylint: disable=C0301

"""E1343_PORTRAIT_GAME_INSTRUCTIONS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(PORTRAIT_GAME_COMPLETED, ["EVENT_1343_run_dialog_3"]),
        RunDialog(
            dialog_id=DI2821_PORTRAIT_GAME_INSTRUCTION,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
        RunDialog(
            dialog_id=DI2822_PORTRAIT_GAME_COMPLETE,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_1343_run_dialog_3"),
        Return(),
    ]
)
