# pylint: disable=C0301

"""E1639_MOLEVILLE_LIBERATED_NPC_AT_MTN_BASE_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(BOOSTER_HILL_CLEARED, ["EVENT_1639_run_dialog_3"]),
        RunDialog(
            dialog_id=DI1139_FIREWORKS_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI1254_FIREWORKS_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1639_run_dialog_3",
        ),
        Return(),
    ]
)
