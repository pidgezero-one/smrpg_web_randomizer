# pylint: disable=C0301

"""E2633_CASINO_INTERIOR_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(CASINO_WARP_ENABLED, ["EVENT_2633_set_bit_0"]),
        RunEventAsSubroutine(E2645_CASINO_SUBROUTINE),
        SetBit(DIRECTIONAL_7046_1, identifier="EVENT_2633_set_bit_0"),
        ActionQueueSync(
            target=NPC_1, subscript=[ASSetWalkingSpeed(FASTEST), ASWalkWestPixels(5)]
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthPixels(8),
                ASSetSpriteSequence(
                    index=10, is_mold=True, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkWestPixels(16),
                ASSetSpriteSequence(
                    index=10,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
            ]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASSetWalkingSpeed(FASTEST), ASWalkSouthwestPixels(3)]),
        ActionQueueAsync(
            target=NPC_9,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthwestPixels(8),
                ASWalkSouthwestPixels(3),
            ]),
        ActionQueueAsync(target=NPC_4, subscript=[ASVisibilityOn()]),
        ActionQueueAsync(target=NPC_5, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_6, subscript=[ASVisibilityOff()]),
        ActionQueueAsync(target=NPC_7, subscript=[ASVisibilityOff()]),
        FadeInFromBlack(sync=False),
        JmpIfBitClear(GAMEBOY_KID_PURCHASE_COMPLETE, ["EVENT_2633_ret_7"]),
        SetVarToConst(PRIMARY_TEMP_7000, 523),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Return(identifier="EVENT_2633_ret_7"),
    ]
)
