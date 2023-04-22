"""A0313_SHIP_TROOPA_PUZZLE_BUTTON"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        ShadowOn(identifier="ACTION_313_shadow_on_0"),
        SetPriority(3),
        Pause(1),
        JmpIfBitClear(TEMP_7043_0, ["ACTION_313_shadow_on_0"]),
        SetSpriteSequence(index=1, is_sequence=True, looping=False),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=4),
        Return(),
    ]
)
