"""BE0052_INTRO_SCENE_DOMINO_CLOAKER_S_INTRODUCTION"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    script=[
        RunSubroutine(["command_0x3a69a6"]),
        RunSubroutine(["command_0x3a7531"]),
        Db(bytearray(b"\xba\x03(\x00")),
        NewSpriteAtCoords(
            sprite_id=SPR1023_EMPTY,
            sequence=13,
            priority=1,
            vram_address=0x8000,
            palette_row=8,
            looping=True,
            param_2_and_0x10=True,
            overwrite_palette=True,
        ),
        Jmp(["command_0x3a7550"]),
    ]
)
