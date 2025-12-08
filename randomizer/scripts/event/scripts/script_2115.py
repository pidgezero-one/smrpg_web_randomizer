# pylint: disable=C0301

"""E2115_STATUE_1_SHAKE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASFixedFCoordOn(),
                ASSequencePlaybackOff(),
                ASSetAllSpeeds(FAST),
                ASWalkSouthwestPixels(5),
                ASWalkNortheastPixels(5),
                ASWalkSouthwestPixels(3),
                ASWalkNortheastPixels(3),
                ASResetProperties(),
                ASFixedFCoordOff(),
            ]),
        Return(),
    ]
)
