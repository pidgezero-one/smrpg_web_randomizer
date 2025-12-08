# pylint: disable=C0301

"""E1615_MOLEVILLE_SWAP_SHOP_TUTORIAL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1175_SWAP_SHOP_INSTRUCTIONS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
