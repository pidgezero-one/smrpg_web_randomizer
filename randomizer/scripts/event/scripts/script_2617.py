# pylint: disable=C0301

"""E2617_FACTORY_2ND_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(INNER_FACTORY_ROOM_3_COMPLETED, ["EVENT_2617_sequence_setter"]),
        ActionQueueSync(
            target=NPC_12,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetPriority(3),
                ASWalkNorthwestPixels(8),
                ASWalkNortheastPixels(8),
                ASFaceSoutheast(),
            ]),
        ActionQueueSync(
            target=NPC_13,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetPriority(3),
                ASWalkNorthwestPixels(8),
                ASWalkNortheastPixels(4),
                ASFaceSoutheast(),
            ]),
        ActionQueueSync(
            target=NPC_14,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASSetPriority(3),
                ASWalkNorthwestPixels(8),
                ASFaceSoutheast(),
            ]),
        ActionQueueAsync(target=NPC_15, subscript=[ASSetPriority(3)]),
        RunEventAsSubroutine(
            E0856_INNER_FACTORY_2ND_ROOM_SHUFFLED_NPC_ANIMATION_LOADER,
            identifier="EVENT_2617_sequence_setter"),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
