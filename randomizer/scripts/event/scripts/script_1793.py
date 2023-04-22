# pylint: disable=C0301

"""E1793_LANDS_END_PURCHASABLE_CHEST_1_SUBROUTINE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(LANDS_END_CHEST_1_USED),
        ClearBit(LANDS_END_CHEST_1_PAID),
        JmpToEvent(E0172_CHEST_1_CONTAINER),
    ]
)
