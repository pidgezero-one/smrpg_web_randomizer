# TroopaShell

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ef00"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F263),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0004_MARIO_ATTACK_UP_RIGHT, sequence=4, store_to_vram=True
        ),
        ReturnSubroutine(),
        ReturnSubroutine(identifier="command_0x35ef00"),
    ]
)
