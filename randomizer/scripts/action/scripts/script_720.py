"""A0720_WATER_SPLASH_DROPS_SFX"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        SetSpriteSequence(index=0, looping=False),
        PlaySound(sound=SO050_WATER_DROPLET, channel=4),
        Pause(15),
        SetVarToConst(TEMP_70AF, 0),
        VisibilityOff(),
        Return(),
    ]
)
