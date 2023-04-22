# pylint: disable=C0301

"""E3792_FACTORY_FINAL_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7043_1),
        SetBit(TEMP_7043_5),
        ActionQueueSync(
            target=NPC_4,
            subscript=[ASTransferXYZFPixels(x=0, y=4, z=0, direction=EAST)],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASTransferXYZFPixels(x=246, y=2, z=30, direction=NORTHEAST),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_7,
            subscript=[ASSetSpriteSequence(index=1, is_sequence=True, looping=True)],
        ),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=3, y=23, z=0, direction=SOUTHEAST),
                ASFloatingOff(),
            ],
        ),
        FreezeCamera(),
        RememberLastObject(),
        ActionQueueSync(
            target=NPC_5, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[0])]
        ),
        ActionQueueSync(
            target=NPC_9, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 2])]
        ),
        ActionQueueSync(
            target=NPC_8, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[2])]
        ),
        ActionQueueSync(
            target=NPC_7, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[0, 1])]
        ),
        ActionQueueSync(
            target=NPC_6, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[1])]
        ),
        RememberLastObject(),
        ActionQueueAsync(
            target=NPC_4, subscript=[ASSetWalkingSpeed(FASTEST), ASWalk1StepSouthwest()]
        ),
        ActionQueueSync(
            target=NPC_9, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[])]
        ),
        ActionQueueSync(
            target=NPC_8, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[])]
        ),
        ActionQueueSync(
            target=NPC_7, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[])]
        ),
        ActionQueueSync(
            target=NPC_6, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[])]
        ),
        ActionQueueSync(
            target=NPC_5, subscript=[ASSetObjectMemoryBits(arg_1=0x0E, bits=[])]
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASSetPriority(3),
                ASTransferXYZFPixels(x=0, y=8, z=0, direction=EAST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
            ],
        ),
        ActionQueueSync(
            target=NPC_11,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASTransferXYZFPixels(x=0, y=8, z=0, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASTransferXYZFPixels(x=0, y=24, z=0, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(index=3, is_sequence=True, looping=True),
                ASTransferXYZFPixels(x=0, y=24, z=0, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_14,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASTransferXYZFPixels(x=234, y=19, z=0, direction=EAST),
                ASSetVRAMPriority(OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES),
            ],
        ),
        RememberLastObject(),
        UnsyncActionScript(NPC_4),
        UnsyncActionScript(NPC_9),
        UnsyncActionScript(NPC_8),
        ClearBit(TEMP_7043_1),
        ClearBit(TEMP_7043_5),
        RunEventAsSubroutine(
            E0859_INNER_FACTORY_1ST_ROOM_POST_FIGHT_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        RunEventAtReturn(E3794_FACTORY_FINAL_BOSS_FIGHT),
        Return(),
    ]
)
