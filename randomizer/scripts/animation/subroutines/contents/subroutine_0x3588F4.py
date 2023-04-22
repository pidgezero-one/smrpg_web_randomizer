# pylint: disable=C0301,C0103

"""referenced by items Mushroom"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=34,
    script=[
        MoveObject(
            speed=25,
            start_position=-513,
            end_position=0,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
            identifier="command_0x3588f4",
        ),
        PlaySound(sound=S0061_ITEM_USE),
        Db(bytearray(b"\x12\x81")),
        ResetObjectMappingMemory(),
        RemoveObject(),
        NewSpriteAtCoords(
            sprite_id=SPR0518_SMALL_WHITE_CLOUD,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            overwrite_palette=True,
            overlap_all_sprites=True,
        ),
        PauseScriptUntilSpriteSequenceDone(),
        RemoveObject(),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        ReturnSubroutine(),
    ],
)
