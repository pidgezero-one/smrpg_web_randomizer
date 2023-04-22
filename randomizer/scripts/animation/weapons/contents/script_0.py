"""Weapon animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ecf7"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0004_MARIO_ATTACK_UP_RIGHT, sequence=0, store_to_vram=True
        ),
        ReturnSubroutine(),
        PlaySound(sound=S0080_WALLOP_1, identifier="command_0x35ecf7"),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0004_MARIO_ATTACK_UP_RIGHT, sequence=1, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0081_WALLOP_2),
        ReturnSubroutine(),
    ]
)
