# pylint: disable=C0301

"""E0287_RESET_GAME"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [ResetAndChooseGame(identifier="EVENT_287_reset_and_choose_game_0"), Return()]
)
