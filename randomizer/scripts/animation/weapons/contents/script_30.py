"""DrillClaw animation"""

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        ClearAMEM16Bit(0x60),
        JmpIfAMEM8BitEqualsConst(0x62, 1, ["command_0x35f074"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0016_BOWSER_CLAW_ATTACK, sequence=0, store_to_vram=True
        ),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35F49E),
        ReturnSubroutine(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0016_BOWSER_CLAW_ATTACK,
            sequence=2,
            store_to_vram=True,
            identifier="command_0x35f074",
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        PlaySound(sound=S0042_BLADE),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        PlaySound(sound=S0042_BLADE),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        PlaySound(sound=S0042_BLADE),
        PauseScriptUntilSpriteSequenceDone(),
        ReturnSubroutine(),
    ]
)
