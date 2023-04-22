# pylint: disable=C0301

"""E3133_PA_MOLE_IN_MINES"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1652_PA_MOLE_AFTER_MINES_CLEARED,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
    ]
)
