# pylint: disable=C0301

"""E2622_ENDING_CREDITS_KEEP"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkToXYCoords(x=1, y=4),
                ASWalkWestPixels(8),
                ASWalk1StepNorth(),
            ],
        ),
        RunEventAsSubroutine(E1192_ENDING_CREDITS_KEEP_SHUFFLED_NPC_ANIMATION_LOADER),
        RemoveObjectFromCurrentLevel(MARIO),
        StarMaskExpandFromScreenCenter(),
        Pause(564),
        StarMaskShrinkToScreenCenter(),
        PauseScriptUntilEffectDone(),
        JmpToEvent(E3798_ENDING_CREDITS_ORANGE_STAR),
        Return(),
    ]
)
