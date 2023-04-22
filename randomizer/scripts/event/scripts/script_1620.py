# pylint: disable=C0301

"""E1620_OCCUPIED_MOLEVILLE_EXTERIOR_NPC_AT_MTN_BASE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1096_MOLEVILLE_BOMB_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
