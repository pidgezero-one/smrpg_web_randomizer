# pylint: disable=C0301

"""E2822_CLONE_RESERVED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        PlaySound(sound=SO014_FLOWER, channel=6),
        MoveScriptToBackgroundThread2(),
        RestoreAllHP(),
        RestoreAllFP(),
        TintLayers(
            layers=[LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=64,
            green=160,
            blue=64,
            speed=3,
            bit_15=True),
        TintLayers(
            layers=[LAYER_L2, LAYER_L3, LAYER_L4, NPC_SPRITES, BACKGROUND],
            red=0,
            green=0,
            blue=0,
            speed=3,
            bit_15=True),
        ResetPrioritySet(),
        MoveScriptToMainThread(),
        Return(),
    ]
)
