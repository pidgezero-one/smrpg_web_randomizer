"""A0343_SHIP_1_CHEST_ROOM_RATS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSequenceSpeed(FAST, identifier="ACTION_343_set_animation_speed_0"),
        WalkFDirectionSteps(2),
        JmpIfRandom1of2(["ACTION_343_set_animation_speed_0"]),
        Pause(8),
        JmpIfRandom1of2(["ACTION_343_set_animation_speed_0"]),
        TurnRandomDirection(),
        Jmp(["ACTION_343_set_animation_speed_0"]),
    ]
)
