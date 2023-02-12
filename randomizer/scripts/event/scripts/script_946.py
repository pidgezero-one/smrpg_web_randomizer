# E0946_FINAL_BOSS_ANIMATION_SUBROUTINE_3

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASPause(20),
                ASResetProperties(),
                ASSetWalkingSpeed(FAST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
                ASJumpToHeight(152),
                ASShiftNortheastSteps(2),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASShiftNortheastSteps(2),
                ASFloatingOff(),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=1,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        Return(),
    ]
)
