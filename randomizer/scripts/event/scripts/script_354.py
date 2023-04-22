# pylint: disable=C0301

"""E0354_BOSS_BATTLE_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0353_BOSS_BATTLE)])
