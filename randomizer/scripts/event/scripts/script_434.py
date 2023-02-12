# E0434_PIPE_VAULT_RED_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_707C_0),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(
            target=NPC_5,
            subscript=[
                ASSetPriority(3),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
            ],
        ),
        ActionQueueSync(target=NPC_2, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_3, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_0, subscript=[ASSetPriority(3), ASVisibilityOff()]),
        ActionQueueSync(target=NPC_1, subscript=[ASSetPriority(3), ASVisibilityOff()]),
        RememberLastObject(),
        Return(),
    ]
)
