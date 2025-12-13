# pylint: disable=C0301

"""E3685_NIMBUS_GET_CROCOS_ITEM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RemoveObjectFromCurrentLevel(MEM_70A8),
        SetBit(UNUSED_704B_6),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        Return(),
    ]
)
