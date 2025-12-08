# pylint: disable=C0301

"""E3633_NIMBUS_EXTERIOR_WOMAN_NEAR_INN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2415_TALK_TO_CASTLE_NPCS_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
