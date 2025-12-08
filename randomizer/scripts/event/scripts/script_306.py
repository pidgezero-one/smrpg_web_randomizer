# pylint: disable=C0301

"""E0306_MUSHROOM_KINGDOM_BROTHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0547_SUPER_JUMP_TIMING_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
