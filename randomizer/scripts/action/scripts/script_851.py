"""A0851_BOOSTER_PASS_APPRENTICE_AFTER_FIGHT"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOff(),
        ShadowOff(),
        SetPriority(3),
        OverwriteSolidity(),
        FaceSoutheast(),
        SetSpriteSequence(index=0, is_sequence=True, looping=True, mirror_sprite=True),
        SetSequenceSpeed(VERY_FAST),
        PlaySound(sound=SO024_TAPPING_FEET, channel=4),
        Pause(80),
        PlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
        SetWalkingSpeed(FASTEST),
        WalkToXYCoords(x=23, y=76),
        VisibilityOff(),
        Return(),
    ]
)
