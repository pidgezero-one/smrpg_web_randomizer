# pylint: disable=C0301,C0103

"""referenced by monster_attacks Thornet"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=21,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x356061"),
        NewSpriteAtCoords(
            sprite_id=SPR0518_SMALL_WHITE_CLOUD,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        PauseScriptUntilSpriteSequenceDone(),
        RunSubroutine(["command_0x35252f"]),
    ])
