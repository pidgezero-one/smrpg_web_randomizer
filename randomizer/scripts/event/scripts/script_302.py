# pylint: disable=C0301

"""E0302_MUSHROOM_KINGDOM_DAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0540_KINGDOM_JUMP_SHOES_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
