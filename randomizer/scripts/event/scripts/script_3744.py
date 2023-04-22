# pylint: disable=C0301

"""E3744_NIMBUS_EXTERIOR_SHY_AWAY"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetSpriteSequence(
                    index=6, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASPause(60),
                ASResetProperties(),
            ],
        ),
        Pause(20),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        ActionQueueSync(target=MARIO, subscript=[ASPause(30), ASFaceSoutheast()]),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[ASWalkSoutheastSteps(8), ASDb(bytearray(b"\xfd\xf2"))],
        ),
        RemoveObjectFromSpecificLevel(NPC_9, R438_NIMBUS_LAND_OUTSIDE_AFTER_VALENTINA),
        RemoveObjectFromCurrentLevel(NPC_9),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouth()]),
        Return(),
    ]
)
