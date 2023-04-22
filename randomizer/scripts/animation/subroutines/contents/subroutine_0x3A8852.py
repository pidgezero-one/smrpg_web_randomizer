# pylint: disable=C0301,C0103

"""referenced by """

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=64,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=256,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
        ),
        NewSpriteAtCoords(
            sprite_id=SPR0792_BLACK_ROCK,
            sequence=3,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            overwrite_palette=True,
            overlap_all_sprites=True,
        ),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        ClearAMEM8Bit(0x60),
        SetAMEM16BitToConst(0x60, 2),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A88DF),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A88DF),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x3A88DF),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3A88DF),
        Pause1Frame(identifier="command_0x3a8881"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 4, ["command_0x3a8881"]),
        IncAMEM8BitByConst(0x68, 1),
        SetOMEMMainToAMEM8Bit(omem=0x68, amem=0x68),
        RemoveObject(),
        ReturnObjectQueue(),
    ],
)
