# pylint: disable=C0301

"""E1108_FROGFUCIUS_SCROLL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2718_SONG_1_SCROLL_HINT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
    ]
)
