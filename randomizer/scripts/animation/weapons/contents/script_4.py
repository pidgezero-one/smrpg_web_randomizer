# Space

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ed64"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0022_MALLOW_PUNCH, sequence=0, store_to_vram=True
        ),
        ReturnSubroutine(),
        PlaySound(sound=S0010_MALLOW_PUNCH_1, identifier="command_0x35ed64"),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0022_MALLOW_PUNCH, sequence=1, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0048_MALLOW_PUNCH_2),
        ReturnSubroutine(),
    ]
)
