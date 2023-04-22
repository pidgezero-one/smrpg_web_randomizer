# pylint: disable=C0301

"""E1869_SKY_BRIDGE_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]), Return()])
