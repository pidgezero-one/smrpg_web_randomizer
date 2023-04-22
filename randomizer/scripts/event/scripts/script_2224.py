# pylint: disable=C0301

"""E2224_KEEP_FINAL_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(KEEP_BOSS_3_DEFEATED, ["EVENT_2224_action_queue_sync_6"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetSequenceSpeed(SLOW),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNortheastPixels(8),
                ASWalkNorthwestPixels(4),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
                ASSequenceLoopingOn(),
                ASSetPriority(3),
            ],
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNortheastPixels(19),
                ASWalkNorthPixels(3),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
                ASSequenceLoopingOn(),
                ASSetPriority(3),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNortheastPixels(23),
                ASWalkSoutheastPixels(12),
                ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 1, 3]),
                ASSequenceLoopingOn(),
                ASSetPriority(3),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=True),
            ],
        ),
        RunEventAsSubroutine(E0853_KEEP_FINAL_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueSync(
            target=NPC_3,
            subscript=[ASWalkSoutheastPixels(8)],
            identifier="EVENT_2224_action_queue_sync_6",
        ),
        ActionQueueAsync(target=NPC_4, subscript=[ASWalkSoutheastPixels(8)]),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R400_BOWSERS_KEEP_AREA_13_2ND_THRONE_ROOM_BOOMERS_ROOM,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        PrioritySet(mainscreen=[LAYER_L1, NPC_SPRITES], subscreen=[], colour_math=[]),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
