# pylint: disable=C0301

"""E2294_ENDING_CREDITS_WEDDING_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([RunEventAtReturn(E2295_ENDING_CREDITS_WEDDING_LOGIC), Return()])
