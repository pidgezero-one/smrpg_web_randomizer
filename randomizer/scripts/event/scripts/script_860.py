# E0860_MINES_BOSS_SHOVE_SUBROUTINE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(34),
                ASSetSpriteSequence(
                    index=13, is_mold=True, is_sequence=True, looping=True
                ),
            ],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(32),
                ASSetSpriteSequence(
                    index=7,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASSetWalkingSpeed(VERY_FAST),
                ASPlaySound(sound=SO019_LONG_FALL, channel=6),
                ASShiftSouthwestSteps(10),
            ],
        ),
        Pause(30),
        Return(),
    ]
)
