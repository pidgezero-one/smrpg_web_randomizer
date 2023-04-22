# pylint: disable=C0301

"""E3287_SHIP_UPPER_HENCHMAN_ROOM_TALK_TO_GUARD_AFTER_WINNING"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(SHIP_LIBERATED, ["EVENT_3287_run_dialog_3_"]),
        RunDialog(
            dialog_id=DI1694_FINAL_SHIP_HENCHMEN_DEFEATED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI1695_FINAL_SHIP_HENCHMEN_AFTER_BOSS_DEFEATED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_3287_run_dialog_3_",
        ),
        Return(),
    ]
)
