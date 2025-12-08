# pylint: disable=C0301

"""E2116_STATUE_2_SHAKE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueAsync(
            target=NPC_1,
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
