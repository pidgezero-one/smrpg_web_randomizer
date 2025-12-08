# pylint: disable=C0301

"""E3075_HEAL_FLASH"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=64,
            green=160,
            blue=64,
            speed=3,
            bit_15=True),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=0,
            green=0,
            blue=0,
            speed=3,
            bit_15=True),
        ResetPrioritySet(),
        Return(),
    ]
)
