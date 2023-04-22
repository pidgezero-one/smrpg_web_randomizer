# pylint: disable=C0301

"""E2818_ASYNC_NO_ANIMATION_10_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO013_COIN, channel=6),
        SetVarToConst(PRIMARY_TEMP_7000, 10),
        AddCoins(PRIMARY_TEMP_7000),
        Return(),
    ]
)
