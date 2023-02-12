# Space

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35ed56"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F92C),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0028_GENO_ELBOW_SHOT, sequence=0, store_to_vram=True
        ),
        ReturnSubroutine(),
        ReturnSubroutine(identifier="command_0x35ed56"),
    ]
)
