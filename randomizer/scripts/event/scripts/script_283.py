# pylint: disable=C0301

"""E0283_GET_FROG_COIN_NO_DIALOG_POSSIBLY_UNUSED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [AddFrogCoins(1), PlaySound(sound=SO094_FROG_COIN, channel=6), Return()]
)
