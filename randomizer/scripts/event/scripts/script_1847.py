# pylint: disable=C0301

"""E1847_CANNONBALL_ROOM_BOMB_1"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIf316DIs3(["EVENT_1847_enable_controls_11"]),
        FreezeAllNPCsUntilReturn(),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASPlaySound(sound=SO089_LIT_FUSE, channel=4),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASPause(30),
            ]),
        Pause(1, identifier="EVENT_1847_pause_5"),
        CreatePacketAtObjectCoords(
            packet=P024_REGULAR_SOUND_EXPLOSION,
            target_npc=NPC_1,
            destinations=["EVENT_1847_pause_5"]),
        PlaySound(sound=SO060_DYNAMITE_BOMB_EXPLOSION, channel=6),
        RemoveObjectFromCurrentLevel(NPC_1),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASTurnClockwise45DegreesNTimes(4),
                ASJumpToHeight(height=144, silent=True),
                ASSetSpriteSequence(
                    index=6, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASWalk1StepFDirection(),
                ASPause(
                    1, identifier="EVENT_1847_action_queue_async_9_SUBSCRIPT_pause_5"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_1847_action_queue_async_9_SUBSCRIPT_pause_5"]
                ),
            ],
            identifier="EVENT_1847_action_queue_async_9"),
        Jmp(["EVENT_1830_store_coin_amount_7000_10"]),
        EnableControls([], identifier="EVENT_1847_enable_controls_11"),
        RunBackgroundEvent(
            event_id=E1849_CANNONBALL_ROOM_BOMB_1_CONTD, return_on_level_exit=True
        ),
        Return(),
    ]
)
