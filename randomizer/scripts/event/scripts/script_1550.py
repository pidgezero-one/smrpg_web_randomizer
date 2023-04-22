# pylint: disable=C0301

"""E1550_CLEAR_BUCKET_WARP_BIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript([ClearBit(BUCKET_WARP_BIT), Return()])
