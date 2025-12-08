# pylint: disable=C0301

"""E1638_MOLEVILLE_LIBERATED_NPC_AT_MTN_BASE_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RunDialog(
            dialog_id=DI1253_GOOD_LUCK_ON_STAR_PIECE_QUEST,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
    ]
)
