# pylint: disable=C0301

"""E0408_MUSHROOM_KINGDOM_OCCUPIED_OLDER_BROTHER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectNotInSpecificLevel(
            NPC_1,
            R481_MUSHROOM_KINGDOM_DURING_MACK_JUMPING_KIDS_HOUSE_2F,
            ["EVENT_408_run_dialog_3"],
        ),
        RunDialog(
            dialog_id=DI0697_WORRIED_ABOUT_BROTHER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI0727_THANKS_FOR_SAVING_BROTHER,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_408_run_dialog_3",
        ),
        Return(),
    ]
)
