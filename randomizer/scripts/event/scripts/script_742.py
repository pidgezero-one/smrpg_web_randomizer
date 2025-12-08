# pylint: disable=C0301

"""E0742_NIMBUS_LAND_LIBERATED_CASTLE_MAIN_HALLWAY_WOMAN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0036_NIMBUS_NPC_FERTILIZER_LOCATION_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
