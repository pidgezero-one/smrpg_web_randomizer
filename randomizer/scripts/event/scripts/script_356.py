# pylint: disable=C0301

"""E0356_BOSS_HUNT_BIT_SETTER_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Set7000ToCurrentLevel(), JmpToEvent(E0355_BOSS_HUNT_BIT_SETTER)])
