# pylint: disable=C0301

"""E3077_SHIP_PUZZLE_MUSHROOM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        MoveScriptToBackgroundThread2(),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        RunEventAsSubroutine(E0241_FREESTANDING_1_GRANT),
        MoveScriptToMainThread(),
        Return(),
    ]
)
