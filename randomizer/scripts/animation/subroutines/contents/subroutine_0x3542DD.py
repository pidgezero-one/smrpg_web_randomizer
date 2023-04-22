# pylint: disable=C0301,C0103

"""referenced by monster_spells WeirdMushroom"""

from randomizer.scripts.animation.script_imports import *

script = SubroutineOrBanklessScript(
    expected_size=35,
    script=[
        SetAMEM32ToXYZCoords(
            origin=CASTER_CURRENT_POSITION,
            x=0,
            y=0,
            z=0,
            set_x=True,
            set_y=True,
            set_z=True,
            identifier="queuestart_0x3542dd",
        ),
        NewSpriteAtCoords(
            sprite_id=SPR0566_GREEN_ITEM_COLLECTION,
            sequence=0,
            priority=3,
            vram_address=0x6200,
            palette_row=0,
            overwrite_vram=True,
            overwrite_palette=True,
            behind_all_sprites=True,
            overlap_all_sprites=True,
        ),
        ResetTargetMappingMemory(),
        ResetObjectMappingMemory(),
        MoveObject(
            speed=33,
            start_position=-1025,
            end_position=1024,
            apply_to_z=True,
            should_set_start_position=True,
            should_set_end_position=True,
            should_set_speed=True,
        ),
        PauseScriptUntil(condition=FRAMES_ELAPSED, frames=60),
        ResetObjectMappingMemory(),
        Jmp(["command_0x35252f"]),
    ],
)
