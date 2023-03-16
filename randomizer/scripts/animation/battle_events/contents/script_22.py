"""BE0022_YARIDOVICH_MIRAGE_ATTACK"""

from randomizer.scripts.animation.script_imports import *

script = BattleAnimationScript(
    header=["command_0x3a6352"],
    script=[
        RunSubroutine(["command_0x3a7531"]),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ac3b2"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a7729"]),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=90),
        ClearAMEM8Bit(0x68),
        SetAMEMToRandom(amem=0x68, upper_bound=7),
        JmpIfAMEM8BitLessThanConst(0x68, 3, ["command_0x3a6352"]),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ac345"], bit_2=True, bit_4=True
        ),
        SpriteQueue(
            field_object=1, destinations=["queuestart_0x3ac35f"], bit_2=True, bit_4=True
        ),
        Jmp(["command_0x3a635c"]),
        SpriteQueue(
            field_object=1,
            destinations=["queuestart_0x3ac345"],
            bit_2=True,
            bit_4=True,
            identifier="command_0x3a6352",
        ),
        SpriteQueue(
            field_object=0, destinations=["queuestart_0x3ac35f"], bit_2=True, bit_4=True
        ),
        RunSubroutine(["command_0x3a771e"], identifier="command_0x3a635c"),
        Jmp(["command_0x3a7550"]),
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=183,
            y=127,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        NewSpriteAtCoords(
            sprite_id=SPR0482_YARIDOVICH,
            sequence=0,
            priority=2,
            vram_address=0x7800,
            palette_row=12,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True,
        ),
        RunSubroutine(["command_0x3a756c"]),
        SummonMonster(monster=Yaridovich, position=1, bit_6=True, bit_7=True),
    ],
)
