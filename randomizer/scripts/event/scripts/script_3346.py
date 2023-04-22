# pylint: disable=C0301

"""E3346_VOLCANO_1ST_BOSS_SCREEN_TINT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=128,
            green=32,
            blue=32,
            speed=4,
            bit_15=True,
            identifier="EVENT_3346_tint_layers_0",
        ),
        Pause(8),
        TintLayers(
            layers=[LAYER_L1, LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=0,
            green=0,
            blue=0,
            speed=4,
            bit_15=True,
        ),
        Pause(8),
        ResetPrioritySet(),
        Jmp(["EVENT_3346_tint_layers_0"]),
    ]
)
