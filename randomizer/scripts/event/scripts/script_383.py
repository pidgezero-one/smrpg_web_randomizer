# pylint: disable=C0301

"""E0383_TOAD_WISHES_YOU_WELL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0702_GIVE_EM_HECK,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
