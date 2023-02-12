# E1134_FAKE_ELDER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2830_SEASIDE_BOSS_WELCOMES_YOU,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
