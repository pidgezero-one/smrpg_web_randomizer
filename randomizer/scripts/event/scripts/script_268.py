# pylint: disable=C0301

"""E0268_UNKNOWN"""

from randomizer.scripts.event.script_imports import *

script = EventScript([Inc(GAME_OVER_COUNTER_MAYBE), Return()])
