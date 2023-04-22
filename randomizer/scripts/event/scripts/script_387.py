# pylint: disable=C0301

"""E0387_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_TOAD_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0658_WHAT_ARE_THOSE_THINGS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
