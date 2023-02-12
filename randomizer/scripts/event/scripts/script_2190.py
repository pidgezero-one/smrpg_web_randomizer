# E2190_BATTLE_DOOR_MIMIC_BOSS_ANIMATION

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASPause(35),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZUpSteps(2),
                ASSetWalkingSpeed(FAST),
                ASShiftZDownPixels(6),
                ASShiftZUpPixels(6),
                ASShiftZDownPixels(4),
                ASShiftZUpPixels(4),
                ASShiftZDownPixels(2),
                ASShiftZUpPixels(2),
                ASPause(20),
            ],
        ),
        Return(),
    ]
)
