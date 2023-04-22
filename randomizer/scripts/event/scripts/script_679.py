# pylint: disable=C0301

"""E0679_MARRYMORE_LIBERATED_EXTERIOR_PATHWAY_RED_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_1),
        RunDialog(
            dialog_id=DI2195_SUITE_PRIZE_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        ResumeActionScript(NPC_1),
        Return(),
    ]
)
