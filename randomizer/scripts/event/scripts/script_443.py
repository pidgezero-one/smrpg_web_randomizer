# E0443_PIPE_VAULT_CHOMPWEED_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_707C_0),
        SetVarToConst(CURRENT_OVERWORLD_MARKER_ID, 20),
        RunEventAsSubroutine(E0281_CLEAR_EXP_STAR_BITS),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_2, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_3, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_4, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_6, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_7, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_8, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_9, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_10, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_11, subscript=[ASSetPriority(3)]),
        RememberLastObject(),
        Return(),
    ]
)
