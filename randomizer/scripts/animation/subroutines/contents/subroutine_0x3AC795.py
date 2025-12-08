# pylint: disable=C0301,C0103

"""referenced by battle_events BE0028_BEAT_TENTACLES_MOVE_ON_TO_KING_CALAMARI"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=29,
    script=[
        RunSubroutine(["command_0x3a7729"], identifier="queuestart_0x3ac795"),
        RemoveObject(),
        SetAMEM32ToXYZCoords(
            origin=ABSOLUTE_POSITION,
            x=104,
            y=121,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        NewSpriteAtCoords(
            sprite_id=SPR0473_TENTACLES_LEFT,
            sequence=5,
            priority=2,
            vram_address=0x7200,
            palette_row=10,
            overwrite_vram=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True),
        SummonMonster(monster=TentaclesLeft, position=1, bit_7=True),
        RunSubroutine(["command_0x3a7544"]),
        ReturnSpriteQueue(),
    ])
