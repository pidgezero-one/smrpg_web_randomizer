# E2115_STATUE_1_SHAKE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
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
