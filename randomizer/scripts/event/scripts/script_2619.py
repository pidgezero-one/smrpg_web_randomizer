# pylint: disable=C0301

"""E2619_ENDING_CREDITS_SUNSET"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkToXYCoords(x=0, y=3),
                ASShiftNorthSteps(8),
            ]),
        RunEventAsSubroutine(E1191_ENDING_CREDITS_CLIFF_SHUFFLED_NPC_ANIMATION_LOADER),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[ASSetSpriteSequence(index=11, is_sequence=True, looping=True)]),
        RemoveObjectFromCurrentLevel(MARIO),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(SLOW),
                ASShiftSouthSteps(4),
                ASWalkSouthPixels(8),
            ]),
        StarMaskExpandFromScreenCenter(),
        Pause(384),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(NORMAL), ASShiftSouthSteps(4)]),
        StarMaskShrinkToScreenCenter(),
        PauseScriptUntilEffectDone(),
        StopEmbeddedActionScript(SCREEN_FOCUS),
        JmpToEvent(E3799_ENDING_CREDITS_PURPLE_STAR),
        Return(),
    ]
)
