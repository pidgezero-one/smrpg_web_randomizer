# pylint: disable=C0301

"""E0313_MUSHROOM_KINGDOM_OCCUPIED_GRANDMA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0676_GRANDMA_DURING_MK_INVASION,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
