# pylint: disable=C0301

"""E2210_KEEP_1ST_BOSS_HEALS_YOU"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO071_MUSHROOM_CURE, channel=6),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=64,
            green=160,
            blue=64,
            speed=3,
            bit_15=True,
        ),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=0,
            green=0,
            blue=0,
            speed=3,
            bit_15=True,
        ),
        ResetPrioritySet(),
        RestoreAllHP(),
        RestoreAllFP(),
        Return(),
    ]
)
