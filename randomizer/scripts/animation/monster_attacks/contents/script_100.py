"""LocoExpress animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x35788e"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0016_BOWSER_CLAW_ATTACK,
            sequence=3,
            store_to_vram=True,
            store_palette=True),
        PauseScriptUntilSpriteSequenceDone(),
        RunSubroutine(["command_0x352f2f"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0013_BOWSER_WALKING_DOWN_LEFT,
            sequence=0,
            store_to_vram=True,
            store_palette=True),
        ResetSpriteSequence(),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
