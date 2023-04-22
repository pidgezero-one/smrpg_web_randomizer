"""A0518_TOWER_BOSS_1_HIDES_BEHIND_DOORWAY_IN_LOBBY_2"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FixedFCoordOn(),
        SetWalkingSpeed(FAST),
        WalkNortheastPixels(4),
        FixedFCoordOff(),
        FaceNortheast(),
        WalkNortheastPixels(6),
        VisibilityOff(),
        Return(),
    ]
)
