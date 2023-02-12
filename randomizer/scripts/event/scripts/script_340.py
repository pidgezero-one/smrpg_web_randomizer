# E0340_MUSHROOM_KINGDOM_OCCUPIED_RAZ_RAINI_HOUSE_SHAKE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Pause(60, identifier="EVENT_340_pause_0"),
        PlaySound(sound=SO022_CLOSE_DOOR, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASShiftNorthwestPixels(4),
                ASShiftSoutheastPixels(8),
                ASShiftNorthwestPixels(6),
                ASShiftSoutheastPixels(4),
                ASShiftNorthwestPixels(3),
                ASShiftSoutheastPixels(1),
            ],
        ),
        Jmp(["EVENT_340_pause_0"]),
    ]
)
