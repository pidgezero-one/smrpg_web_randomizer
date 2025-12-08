# pylint: disable=C0301

"""E0752_VINE_FIELD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfMarioInAir(["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_256_ret_0"]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASJumpToHeight(108),
                ASPause(10),
                ASSetSolidityBits(cant_pass_walls=True),
                ASWalkSoutheastPixels(6),
            ]),
        Pause(1),
        JmpIfMarioInAir(["EVENT_749_pause_3"]),
        ClearBit(TEMP_7043_1),
        Return(),
    ]
)
