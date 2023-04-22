"""MegaGlove animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35efb3"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0004_MARIO_ATTACK_UP_RIGHT, sequence=5, store_to_vram=True
        ),
        ReturnSubroutine(),
        PlaySound(sound=S0084_WALLOP_4, identifier="command_0x35efb3"),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0004_MARIO_ATTACK_UP_RIGHT, sequence=6, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0085_WALLOP_5),
        ResetObjectMappingMemory(),
        ReturnSubroutine(),
    ]
)
