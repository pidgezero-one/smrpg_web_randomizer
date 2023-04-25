# pylint: disable=C0301

"""E0159_NPC_QUEST_GRANT_COINS"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO013_COIN, channel=6),
        AddCoins(PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI0515_GOT_X_COINS,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
    ]
)
