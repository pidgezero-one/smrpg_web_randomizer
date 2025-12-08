# pylint: disable=C0301

"""E2555_BEAN_VALLEY_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(DIRECTIONAL_7047_0),
        ActionQueueSync(
            target=NPC_0, subscript=[ASWalkSouthPixels(1), ASWalkSouthwestPixels(4)]
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASWalkSoutheastPixels(7),
                ASWalkSouthwestPixels(1),
                ASVisibilityOff(),
            ]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSequenceLoopingOn(),
                ASSetSpriteSequence(index=5, is_sequence=True, looping=True),
            ]),
        JmpIfBitSet(BEAN_VALLEY_BOSS_DEFEATED, ["EVENT_2555_action_queue_async_8"]),
        RunBackgroundEvent(
            event_id=E2557_BEAN_VALLEY_WATERS_BOSS, return_on_level_exit=True
        ),
        FadeInFromBlack(sync=False),
        RunEventAsSubroutine(E0817_BEAN_VALLEY_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        Return(),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASTransferToXYZF(x=26, y=60, z=0, direction=EAST),
                ASWalkNorthwestPixels(5),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
            ],
            identifier="EVENT_2555_action_queue_async_8"),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
