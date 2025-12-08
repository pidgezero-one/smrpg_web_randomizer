# pylint: disable=C0301

"""E0352_MUSHROOM_KINGDOM_OCCUPIED_SHOPKEEPER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI0687_HOW_CAN_YOU_SHOP_AT_A_TIME_LIKE_THIS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
