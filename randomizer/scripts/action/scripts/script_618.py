"""A0618_MINES_RIGHT_CROOK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpIfBitSet(MINES_HENCHMAN_RIGHT_DEFEATED, ["ACTION_617_visibility_off_10"]),
        JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["ACTION_617_visibility_off_10"]),
        Return(),
        ShiftToXYCoords(x=4, y=24),
        VisibilityOn(),
        FaceMario(),
        SequenceLoopingOn(),
        SequencePlaybackOn(),
        Return(),
    ]
)
