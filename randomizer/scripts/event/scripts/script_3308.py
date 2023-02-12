# E3308_SHIP_BOSS_ROOM_DRINK

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1782_SHIP_BOSS_DRINK,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=False,
            use_background=True,
        ),
        Return(),
    ]
)
