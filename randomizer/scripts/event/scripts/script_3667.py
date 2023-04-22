# pylint: disable=C0301

"""E3667_NIMBUS_CASTLE_ANTECHAMBER_LEFT_GUARD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI3597_VOLCANO_FIRST_ROOM_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
