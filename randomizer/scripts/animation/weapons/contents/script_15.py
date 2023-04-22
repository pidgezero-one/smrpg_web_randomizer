"""HandGun animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35eeb4"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35FC89),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0029_GENO_FINGER_SHOT, sequence=1, store_to_vram=True
        ),
        ReturnSubroutine(),
        ReturnSubroutine(identifier="command_0x35eeb4"),
    ]
)
