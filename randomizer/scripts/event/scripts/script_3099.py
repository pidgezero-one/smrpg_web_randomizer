# pylint: disable=C0301

"""E3099_SHUFFLE_FIREWORKS_CHEST_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [SetVarToConst(FIREWORKS_COUNTER, 5), JmpToEvent(E0883_CHEST_ITEM_BAG_PACKET)]
)
