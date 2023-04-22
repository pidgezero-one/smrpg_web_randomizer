# pylint: disable=C0301

"""E1545_SAND_WHIRLPOOL"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Db(bytearray(b"\xc7\x90")),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FASTEST),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFixedFCoordOff(),
                ASDb(bytearray(b"\x98")),
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(NORMAL),
            ],
        ),
        PixelateLayers(layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=9, duration=0),
        FadeInFromBlack(sync=True, duration=40),
        PixelateLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3], pixel_size=0, duration=70
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASPause(30),
                ASResetProperties(),
                ASVisibilityOn(),
                ASJumpToHeight(108),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASWalk1StepFDirection(),
            ],
        ),
        SetBit(TEMP_7044_6),
        Return(),
    ]
)
