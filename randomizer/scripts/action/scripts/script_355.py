"""A0355_PLAYER_IN_FOREST_1ST_TRUNK"""

from randomizer.scripts.action.script_imports import *

script = ActionScript(
    [
        JmpToSubroutine(["ACTION_355_shadow_off_3"]),
        WalkToXYCoords(x=16, y=24),
        Jmp(["ACTION_355_set_animation_speed_10"]),
        ShadowOff(identifier="ACTION_355_shadow_off_3"),
        FaceSouth(),
        FixedFCoordOn(),
        FloatingOff(),
        ClearSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
        SetWalkingSpeed(FAST),
        Return(),
        SetWalkingSpeed(NORMAL, identifier="ACTION_355_set_animation_speed_10"),
        SetSolidityBits(cant_pass_walls=True),
        PlaySound(sound=SO028_PIPE_ENTRANCE, channel=6),
        SetSpriteSequence(
            index=30, sprite_offset=2, is_mold=True, is_sequence=True, looping=True
        ),
        ClearSolidityBits(cant_pass_walls=True),
        DecZCoord1Step(),
        SetSolidityBits(cant_pass_walls=True, cant_pass_npcs=True),
        ResetProperties(),
        FixedFCoordOff(),
        Return(),
    ]
)
