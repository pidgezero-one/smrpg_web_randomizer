# pylint: disable=C0301

"""E0296_MUSHROOM_KINGDOM_GRANDMA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0533_MUSHROOM_KINGDOM_NPC,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
