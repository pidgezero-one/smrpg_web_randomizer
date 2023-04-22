# pylint: disable=C0301

"""E0680_MARRYMORE_LIBERATED_EXTERIOR_PATHWAY_YELLOW_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_0),
        RunDialog(
            dialog_id=DI2196_HOTEL_TIP_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ResumeActionScript(NPC_0),
        Return(),
    ]
)
