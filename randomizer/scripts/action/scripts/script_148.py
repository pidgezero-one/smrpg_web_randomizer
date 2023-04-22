"""A0148_SONG_SCROLL"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ResetProperties(identifier="ACTION_148_reset_properties_0"),
        Pause(1),
        Jmp(["ACTION_148_reset_properties_0"]),
        Return(),
    ]
)
