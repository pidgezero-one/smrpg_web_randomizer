# pylint: disable=C0301

"""E0291_MUSHROOM_KINGDOM_OUTER_CASTLE_GUARDS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2230_TOAD_GUARD,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
