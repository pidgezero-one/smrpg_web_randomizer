# pylint: disable=C0301,C0103

"""referenced by ally_spells Thunderbolt"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=89,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=256,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3583e1"),
        NewSpriteAtCoords(
            sprite_id=SPR0528_VERY_SMALL_BLACK_DOT,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        ShineEffect(
            colour_count=6, starting_colour_index=1, glow_duration=1, east=True
        ),
        ClearAMEM16Bit(0x60),
        ClearAMEM8Bit(0x6E),
        ObjectQueueAtOffsetAndIndex(index=2, target_address=0x3583DB),
        RunSubroutine(["command_0x35862c"]),
        PauseScriptUntilAMEMBitsSet(0x6E, [0]),
        SetAMEM8BitToConst(0x6F, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6F, amem=0x6F),
        RemoveObject(),
        Db(bytearray(b"\x81")),
        ReturnObjectQueue(),
        PauseScriptUntil(
            condition=FRAMES_ELAPSED, frames=5, identifier="queuestart_0x35840f"
        ),
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=8,
            y=-266,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True),
        NewEffectObject(effect=EF0014_SPELL_CAST_CLUB, looping_on=True),
        PlaySound(sound=S0035_SPELL_POWER_UP),
        Db(bytearray(b"\x8a\x01")),
        Layer3On(prop=OVERLAP_ALL, bpp4=True),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=24),
        FadeOutObject(duration=1),
        PauseScriptUntil(condition=FADE_4BPP_COMPLETE),
        Layer3Off(prop=OVERLAP_ALL, bpp4=True),
        Pause2Frames(),
        ClearEffectIndex(),
        SetAMEM8BitToConst(0x6E, 1),
        SetOMEMMainToAMEM8Bit(omem=0x6E, amem=0x6E),
        ReturnObjectQueue(),
    ])
