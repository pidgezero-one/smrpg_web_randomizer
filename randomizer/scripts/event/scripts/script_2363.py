# pylint: disable=C0301

"""E2363_ABYSS_1ST_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        FreezeCamera(),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetPriority(3),
                ASWalkNorthPixels(4),
                ASWalkNorthwestPixels(1),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASWalkWestPixels(11),
                ASWalkSouthPixels(2),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetPriority(3),
                ASWalkWestPixels(4),
                ASWalkSouthPixels(2),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetWalkingSpeed(FASTEST), ASShiftZUpSteps(16)]
        ),
        RunEventAsSubroutine(E0854_ABYSS_1ST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0, sprite_offset=1, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=0, silent=True),
                ASPause(
                    1, identifier="EVENT_2363_action_queue_async_7_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_2363_action_queue_async_7_SUBSCRIPT_pause_2"]
                ),
                ASPlaySound(sound=SO058_INSERT, channel=4),
            ],
        ),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
    ]
)
