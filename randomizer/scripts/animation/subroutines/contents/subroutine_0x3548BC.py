# referenced by monster_attacks ScrowBell

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=56,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=-16,
            y=-8,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3548bc",
        ),
        NewSpriteAtCoords(
            sprite_id=SPR0792_BLACK_ROCK,
            sequence=2,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            looping=True,
            overwrite_palette=True,
            overlap_all_sprites=True,
        ),
        RunSubroutine(["command_0x357fcc"]),
        RemoveObject(),
        PlaySound(sound=S0152_HIT),
        ClearAMEM8Bit(0x68),
        SetAMEM16BitToConst(0x60, 7),
        ObjectQueueAtOffsetAndIndex(index=0, target_address=0x35624B),
        MoveObject(
            speed=1,
            start_position=-129,
            end_position=0,
            apply_to_x=True,
            should_set_speed=True,
        ),
        MoveObject(
            speed=1,
            start_position=256,
            end_position=0,
            apply_to_y=True,
            should_set_speed=True,
        ),
        RunSubroutine(["command_0x352552"]),
        ResetObjectMappingMemory(),
        Jmp(["command_0x35252f"]),
    ],
)
