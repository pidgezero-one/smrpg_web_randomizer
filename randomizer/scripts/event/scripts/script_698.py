# pylint: disable=C0301

"""E0698_MARRYMORE_PHOTOGRAPHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2163_MARRYMORE_PHOTO_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
