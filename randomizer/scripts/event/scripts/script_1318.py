# pylint: disable=C0301

"""E1318_LOBBY_PORTRAIT_3"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToBackgroundThread2(),
        RunDialog(
            dialog_id=DI2563_PORTRAIT_3,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        MoveScriptToMainThread(),
        Return(),
    ]
)
