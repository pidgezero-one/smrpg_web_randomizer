"""A0397_PLAYER_TUMBLES_DOWN_BOOSTER_PASS"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        FloatingOff(),
        OverwriteSolidity(),
        ShadowOff(),
        SetWalkingSpeed(FASTER),
        SetSpriteSequence(index=6, sprite_offset=3, is_sequence=True, looping=True),
        VisibilityOn(),
        PlaySound(sound=SO048_MINECART_START, channel=4),
        WalkSouthwestSteps(3),
        OverwriteSolidity(
            cant_pass_walls=True,
            bit_4=True,
            cant_pass_npcs=True,
            cant_walk_through=True,
            bit_7=True,
        ),
        FloatingOn(),
        ShadowOn(),
        WalkSouthwestSteps(18),
        SetWalkingSpeed(FASTEST),
        WalkSouthPixels(8),
        SetSpriteSequence(
            index=1, sprite_offset=3, is_mold=True, is_sequence=True, looping=True
        ),
        PlaySound(sound=SO022_CLOSE_DOOR, channel=4),
        ClearBit(DISABLE_BOOSTER_PASS_EXIT_WHILE_FALLING),
        SetBit(TEMP_7043_0),
        Return(),
    ]
)
