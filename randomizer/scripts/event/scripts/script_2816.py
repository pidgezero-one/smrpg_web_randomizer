# pylint: disable=C0301

"""E2816_ASYNC_NO_ANIMATION_FROG_COIN"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [PlaySound(sound=SO094_FROG_COIN, channel=6), AddFrogCoins(1), Return()]
)
