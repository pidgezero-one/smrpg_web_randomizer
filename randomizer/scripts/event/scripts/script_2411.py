# pylint: disable=C0301

"""E2411_FOREST_UNDERGROUND_2_EXIT_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript([SetBit(DIRECTIONAL_7045_4), Jmp(["EVENT_2416_set_bit_0"])])
