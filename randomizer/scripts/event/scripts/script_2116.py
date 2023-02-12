# E2116_STATUE_2_SHAKE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFixedFCoordOn(),
                ASSequencePlaybackOff(),
                ASSetAllSpeeds(FAST),
                ASShiftSouthwestPixels(5),
                ASShiftNortheastPixels(5),
                ASShiftSouthwestPixels(3),
                ASShiftNortheastPixels(3),
                ASResetProperties(),
                ASFixedFCoordOff(),
            ],
        ),
        Return(),
    ]
)
