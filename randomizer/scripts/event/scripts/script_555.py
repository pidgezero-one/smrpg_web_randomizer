# pylint: disable=C0301

"""E0555_ROSE_TOWN_INN_TOAD_ITEM_GRANT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        RememberLastObject(),
        SetBit(ROSE_TOWN_INN_TOAD_ITEM_RECEIVED),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        SetAsyncActionScript(MEM_70A8, A0636_54_VELOCITY_SINGLE_JUMP),
        Pause(10),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOn(),
                ASWalkSoutheastSteps(4),
            ]),
        RemoveObjectFromCurrentLevel(MEM_70A8),
        RemoveObjectFromSpecificLevel(NPC_0, R095_ROSE_TOWN_DURING_BOWYER_INN_2F),
        RemoveObjectFromSpecificLevel(NPC_2, R096_ROSE_TOWN_INN_2F),
        Return(),
    ]
)
