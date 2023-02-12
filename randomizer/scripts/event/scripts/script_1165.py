# E1165_SEASIDE_LIBERATED_BEACH_LETTER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1786_LETTER_FROM_SHIP_BOSS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
