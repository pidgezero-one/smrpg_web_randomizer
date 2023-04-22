# pylint: disable=C0301

"""E0316_MUSHROOM_KINGDOM_OCCUPIED_DAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectInSpecificLevel(
            NPC_3,
            R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            ["EVENT_316_run_dialog_9"],
        ),
        JmpIfObjectInSpecificLevel(
            NPC_4,
            R480_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_1F,
            ["EVENT_316_run_dialog_9"],
        ),
        RunDialog(
            dialog_id=DI0692_THANKS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI0634_SCARY_THINGS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_316_run_dialog_9",
        ),
        Return(),
    ]
)
