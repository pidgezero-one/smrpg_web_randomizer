"""StickyGlove animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35f00a"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0022_MALLOW_PUNCH, sequence=3, store_to_vram=True
        ),
        ReturnSubroutine(),
        PlaySound(sound=S0152_HIT, identifier="command_0x35f00a"),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0022_MALLOW_PUNCH, sequence=4, store_to_vram=True
        ),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0195_EXPLOSIVE_HIT),
        ReturnSubroutine(),
    ]
)
