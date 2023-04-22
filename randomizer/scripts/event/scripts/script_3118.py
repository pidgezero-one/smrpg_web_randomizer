# pylint: disable=C0301

"""E3118_WATER_STATE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[ASObjectMemoryClearBit(arg_1=0x0C, bits=[3, 4, 5]), ASPause(1)],
        ),
        Return(),
    ]
)
