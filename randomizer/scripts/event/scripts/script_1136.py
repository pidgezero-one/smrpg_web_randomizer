# pylint: disable=C0301

"""E1136_SEASIDE_OCCUPIED_MUSHROOM_BOY_SHOP_OCCUPANT_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI2838_OCCUPIED_SEASIDE_HENCHMAN_BOSS_NAME,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
    ]
)
