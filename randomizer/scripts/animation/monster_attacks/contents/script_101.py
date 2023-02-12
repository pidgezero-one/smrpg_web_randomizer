# PhysicalAttack115

from randomizer.scripts.animation.script_imports import *

script = AnimationScript(
    [
        RunSubroutine(["command_0x357b83"]),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0014_BOWSER_WALKING_UP_RIGHT,
            sequence=2,
            store_to_vram=True,
            looping=True,
            store_palette=True,
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        SpriteSequence(sequence=1, looping_on=True, mirror=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        SpriteSequence(sequence=0, looping_on=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        PlaySound(sound=S0009_ARROW_SLING),
        SetAMEM16BitToConst(0x60, 1),
        RunSubroutine(["command_0x3524b1"]),
        SpriteSequence(sequence=1, looping_on=True, mirror=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        SpriteSequence(sequence=2),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0013_BOWSER_WALKING_DOWN_LEFT,
            sequence=0,
            store_to_vram=True,
            store_palette=True,
        ),
        ResetSpriteSequence(),
        PlaySound(sound=S0015_SPIKE_STING),
        RunSubroutine(["command_0x3523c4"]),
        RunSubroutine(["command_0x3577f2"]),
        ReturnSubroutine(),
    ]
)
