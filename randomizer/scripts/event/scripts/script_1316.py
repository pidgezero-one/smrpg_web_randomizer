# pylint: disable=C0301

"""E1316_LOBBY_PORTRAIT_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToBackgroundThread2(),
        RunDialog(
            dialog_id=DI2561_PORTRAIT_1,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        MoveScriptToMainThread(),
        Return(),
    ]
)
