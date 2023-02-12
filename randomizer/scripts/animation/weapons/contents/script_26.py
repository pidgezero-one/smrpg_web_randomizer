# HandCannon

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35effc"]),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35FD48),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0029_GENO_FINGER_SHOT, sequence=2, store_to_vram=True
        ),
        ReturnSubroutine(),
        ReturnSubroutine(identifier="command_0x35effc"),
    ]
)
