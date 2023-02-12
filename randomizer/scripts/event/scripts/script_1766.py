# E1766_TEMPLE_ELEVATOR_ROOM_LOADER

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMPLE_ELEVATOR_DIRECTION, ["EVENT_1766_action_queue_async_4"]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=20, y=23, z=0, direction=EAST),
                ASSetWalkingSpeed(FASTEST),
                ASShiftEastPixels(14),
                ASFaceSoutheast(),
            ],
        ),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=20, y=55, z=0, direction=EAST),
                ASSetWalkingSpeed(FASTEST),
                ASShiftEastPixels(14),
                ASFaceSoutheast(),
            ],
            identifier="EVENT_1766_action_queue_async_4",
        ),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
