# E1386_VISTA_HILL_LOADER_CONTINUED

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        FreezeCamera(),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASBounceToXYWithHeight(x=0, y=2, height=0),
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetPriority(3),
                ASClearSolidityBits(cant_pass_walls=True),
                ASTransferToXYZF(x=4, y=26, z=0, direction=EAST),
                ASShiftNortheastPixels(1),
                ASFaceNorthwest(),
                ASSequencePlaybackOff(),
            ],
        ),
        FadeInFromBlack(sync=True, duration=130),
        ActionQueueSync(
            target=LAYER_1,
            subscript=[ASSetWalkingSpeed(VERY_SLOW), ASShiftEastSteps(1)],
        ),
        ActionQueueSync(
            target=LAYER_2,
            subscript=[ASSetWalkingSpeed(VERY_SLOW), ASShiftWestSteps(1)],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFixedFCoordOn(),
                ASSetWalkingSpeed(VERY_SLOW),
                ASShiftEastSteps(1),
            ],
        ),
        Pause(50),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSequencePlaybackOn(),
                ASJumpToHeight(108),
                ASPause(40),
                ASFixedFCoordOff(),
                ASSetSequenceSpeed(FAST),
                ASSetWalkingSpeed(NORMAL),
                ASShiftSoutheastSteps(1),
                ASSetWalkingSpeed(FAST),
                ASShiftSoutheastSteps(6),
                ASVisibilityOff(),
                ASPause(20),
            ],
        ),
        FadeOutToBlack(sync=False, duration=70),
        ExitToWorldMap(area=OW03_VISTA_HILL, bit_6=True, bit_7=True),
        Return(),
    ]
)
