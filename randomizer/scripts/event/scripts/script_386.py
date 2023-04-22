# pylint: disable=C0301

"""E0386_MUSHROOM_KINGDOM_OCCUPIED_TOADSTOOLS_ROOM_TOAD_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0657_IM_SCARED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
