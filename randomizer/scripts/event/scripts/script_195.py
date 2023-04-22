# pylint: disable=C0301

"""E0195_GENO_JOINS_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1181_GENO_JOINS,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        JmpToEvent(E0189_GENO_JOINS),
    ]
)
