# pylint: disable=C0301

"""E0032_NON_COIN_CHEST_CONTAINER"""

from randomizer.scripts.event.script_imports import *

script = EventScript([JmpToEvent(E3072_FLOWER_STAR_FC_OR_MUSHROOM_CHEST)])
