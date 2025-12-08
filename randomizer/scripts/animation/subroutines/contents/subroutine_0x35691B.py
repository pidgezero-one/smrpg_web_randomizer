# pylint: disable=C0301,C0103

"""referenced by monster_attacks PhysicalAttack32"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=78,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=248,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x35691b"),
        NewSpriteAtCoords(
            sprite_id=SPR0785_SPRITZ_BOMB,
            sequence=1,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True),
        PlaySound(sound=S0088_TICKING_BOMB),
        ClearAMEM8Bit(0x68),
        ClearAMEM8Bit(0x69),
        SetAMEM16BitToConst(0x60, 6),
        ObjectQueueAtOffsetAndIndex(index=4, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ObjectQueueAtOffsetAndIndex(index=10, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=8),
        ObjectQueueAtOffsetAndIndex(index=6, target_address=0x356B15),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        StopCurrentSoundEffect(),
        DrawSpriteAtAMEM32Coords(
            sprite_id=SPR0517_BOMB_EXPLOSION,
            sequence=0,
            store_to_vram=True,
            store_palette=True),
        PlaySound(sound=S0012_BOMB_EXPLOSION),
        Pause1Frame(identifier="command_0x35695f"),
        JmpIfAMEM8BitNotEqualsConst(0x69, 4, ["command_0x35695f"]),
        Jmp(["command_0x356b01"]),
    ])
