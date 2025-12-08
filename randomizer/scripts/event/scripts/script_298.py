# pylint: disable=C0301

"""E0298_MUSHROOM_KINGDOM_PINK_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0580_SUPER_JUMP_TIMING_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_298_run_dialog_16"),
        Return(),
    ]
)
