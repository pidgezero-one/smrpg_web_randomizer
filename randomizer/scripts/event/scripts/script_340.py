# pylint: disable=C0301

"""E0340_MUSHROOM_KINGDOM_OCCUPIED_RAZ_RAINI_HOUSE_SHAKE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(60, identifier="EVENT_340_pause_0"),
        PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthwestPixels(4),
                ASWalkSoutheastPixels(8),
                ASWalkNorthwestPixels(6),
                ASWalkSoutheastPixels(4),
                ASWalkNorthwestPixels(3),
                ASWalkSoutheastPixels(1),
            ],
        ),
        Jmp(["EVENT_340_pause_0"]),
    ]
)
