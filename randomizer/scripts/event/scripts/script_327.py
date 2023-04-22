# pylint: disable=C0301

"""E0327_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2298_TOAD,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
