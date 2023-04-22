# pylint: disable=C0301

"""E2413_FOREST_UNDERGROUND_2_ENTRANCE_TRAMPOLINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript([SetBit(DIRECTIONAL_7045_2), Jmp(["EVENT_2416_set_bit_0"])])
