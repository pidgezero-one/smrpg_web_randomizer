# pylint: disable=C0301

"""E0157_NPC_QUEST_GRANT_1_FROG_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        AddFrogCoins(1),
        RunDialog(
            dialog_id=DI2243_EMPTY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        Return(),
    ]
)
