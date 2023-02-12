# PhysicalAttack107

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x3577e2"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0491_SHYPER, sequence=3, store_to_vram=True, store_palette=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0490_SMITHY_ST_FORM,
            sequence=0,
            store_to_vram=True,
            store_palette=True,
        ),
        ResetSpriteSequence(),
        PlaySound(sound=S0111_SLEDGE),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
