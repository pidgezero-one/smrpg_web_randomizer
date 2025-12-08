# pylint: disable=C0301

"""E1567_LANDS_END_2_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7042_3),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASVisibilityOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASShiftZUpPixels(4),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASVisibilityOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASShiftZUpPixels(4),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
