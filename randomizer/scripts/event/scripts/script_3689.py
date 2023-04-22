# pylint: disable=C0301

"""E3689_LINK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO156_LINK_FANFARE, channel=6),
        RunDialog(
            dialog_id=DI3846_LINK,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
