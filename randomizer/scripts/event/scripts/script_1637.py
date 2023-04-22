# pylint: disable=C0301

"""E1637_MOLEVILLE_SWAP_SHOP_GIRL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MINECART_CLEARED, ["EVENT_1637_run_dialog_3"]),
        RunDialog(
            dialog_id=DI1145_LANDS_END_SEWER_HINT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        RunDialog(
            dialog_id=DI1152_EMPTY,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1637_run_dialog_3",
        ),
        Return(),
    ]
)
