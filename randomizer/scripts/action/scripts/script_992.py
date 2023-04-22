"""A0992_DEFAULT_SEQUENCE_IN_CHEST"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOff(),
        VisibilityOff(),
        Pause(9),
        VisibilityOn(),
        Pause(24),
        VisibilityOff(),
        Return(),
    ]
)
