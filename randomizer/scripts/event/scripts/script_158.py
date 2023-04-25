# pylint: disable=C0301

"""E0158_NPC_QUEST_GRANT_MULTI_FROG_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO094_FROG_COIN, channel=6),
        AddFrogCoins(PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1310_RECEIVED_X_FROG_COINS,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
    ]
)
