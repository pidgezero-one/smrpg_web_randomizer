# pylint: disable=C0301,C0103

"""referenced by battle_events BE0044_CZAR_DRAGON_DIES"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=75,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=256,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3a8894"),
        NewSpriteAtCoords(
            sprite_id=SPR0776_BLAST_ORANGE_GAS_CLOUD,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        ClearAMEM8Bit(0x64),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 0),
        ObjectQueueAtOffsetAndIndex(
            index=0, target_address=0x3A88DF, identifier="command_0x3a88b1"
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=4),
        IncAMEM8Bit(0x64),
        JmpIfAMEM8BitNotEqualsConst(0x64, 20, ["command_0x3a88b1"]),
        Pause1Frame(identifier="command_0x3a88c1"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 20, ["command_0x3a88c1"]),
        IncAMEM8BitByConst(0x68, 1),
        SetOMEMMainToAMEM8Bit(omem=0x68, amem=0x68),
        RemoveObject(),
        ReturnObjectQueue(),
        SetAMEM8BitToOMEMMain(amem=0x69, omem=0x69),
        IncAMEM8Bit(0x69),
        SetOMEMMainToAMEM8Bit(omem=0x69, amem=0x69),
        RemoveObject(),
        ResetObjectMappingMemory(),
        ReturnObjectQueue(),
    ])
