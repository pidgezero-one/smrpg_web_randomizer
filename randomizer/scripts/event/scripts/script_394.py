# pylint: disable=C0301

"""E0394_MUSHROOM_KINGDOM_OCCUPIED_EXTERIOR_PINK_TOAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_4,
            R190_MUSHROOM_KINGDOM_DURING_MACK_OUTSIDE,
            ["EVENT_298_run_dialog_16"],
        ),
        RunDialog(
            dialog_id=DI0674_OH_WOW,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
