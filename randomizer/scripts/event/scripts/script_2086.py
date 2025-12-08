# pylint: disable=C0301

"""E2086_MONSTRO_PIRANHA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MONSTRO_MIDDLE_DOOR_COMPLETED, ["EVENT_2086_run_dialog_3"]),
        RunDialog(
            dialog_id=DI3338_MONSTRO_SUPERBOSS_HINT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
        RunDialog(
            dialog_id=DI3356_MONSTRO_PIRANHA_PLANT_AFTER_DEFEAT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_2086_run_dialog_3"),
        Return(),
    ]
)
