# pylint: disable=C0301,C0103

"""referenced by behaviour_33_0x350C5B, behaviour_34_0x350C9E, behaviour_51_0x350F56, behaviour_24_0x350A9C, behaviour_8_0x3507A2, behaviour_41_0x350DAF, behaviour_16_0x350928, behaviour_32_0x350C14, behaviour_52_0x350F6B, behaviour_23_0x350A55, behaviour_9_0x3507E9, behaviour_42_0x350DED, weapons FroggieStick, behaviour_43_0x350E38"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=81,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35f732"),
        NewSpriteAtCoords(
            sprite_id=SPR0032_FROGGIE_STICK,
            sequence=0,
            priority=3,
            vram_address=0x6600,
            palette_row=8,
            overwrite_vram=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True),
        PauseScriptUntilSpriteSequenceDone(),
        Pause1Frame(identifier="command_0x35f744"),
        SetAMEM8BitToOMEMMain(amem=0x63, omem=0x63),
        JmpIfAMEM8BitNotEqualsConst(0x63, 1, ["command_0x35f744"]),
        RemoveObject(),
        SetOMEMMainToAMEM8Bit(omem=0x64, amem=0x63),
        ReturnObjectQueue(),
        PlaySound(sound=S0018_SUPER_JUMP_HIT_1, identifier="queuestart_0x35f755"),
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        Pause1Frame(identifier="command_0x35f75f"),
        SetAMEM8BitToOMEMMain(amem=0x64, omem=0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 1, ["command_0x35f75f"]),
        NewSpriteAtCoords(
            sprite_id=SPR0032_FROGGIE_STICK,
            sequence=1,
            priority=3,
            vram_address=0x6600,
            palette_row=8,
            overwrite_vram=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True),
        PauseScriptUntilSpriteSequenceDone(),
        PlaySound(sound=S0058_SUPER_JUMP_HIT_2),
        Pause1Frame(identifier="command_0x35f776"),
        SetAMEM8BitToOMEMMain(amem=0x65, omem=0x65),
        JmpIfAMEM8BitNotEqualsConst(0x65, 1, ["command_0x35f776"]),
        RemoveObject(),
        ReturnObjectQueue(),
    ])
