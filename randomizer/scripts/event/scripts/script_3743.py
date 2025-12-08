# pylint: disable=C0301

"""E3743_NIMBUS_CASTLE_RIGHT_SHAMAN_HALLWAY_LIBERATED_NPC"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3594_REFILLED_NIMBUS_CHEST_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
