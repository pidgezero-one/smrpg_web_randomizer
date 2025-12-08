# pylint: disable=C0301

"""E2278_BALCONY_LOADER_AFTER_NIMBUS_CASTLE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=7, y=14, z=0, direction=EAST),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=4, y=23, z=0, direction=EAST),
                ASVisibilityOn(),
                ASWalkSouthwestPixels(8),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=5, y=22, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=5, y=21, z=0, direction=EAST),
                ASVisibilityOn(),
                ASWalkNortheastPixels(8),
                ASFaceNorthwest(),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=5, y=17, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceSouthwest(),
                ASResetProperties(),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASShiftToXYCoords(x=4, y=20),
                ASFaceSoutheast(),
                ASSequenceLoopingOn(),
                ASVisibilityOn(),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFaceSoutheast(),
                ASSetSequenceSpeed(FAST),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASFaceSoutheast(),
                ASSetSequenceSpeed(FAST),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASFaceSoutheast(),
                ASSetSequenceSpeed(FAST),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=4, y=16, z=0, direction=EAST),
                ASFaceNorthwest(),
                ASResetProperties(),
            ]),
        ActionQueueAsync(
            target=NPC_4,
            subscript=[
                ASTransferToXYZF(x=3, y=17, z=0, direction=EAST),
                ASFaceNorthwest(),
                ASResetProperties(),
                ASSequenceLoopingOff(),
            ]),
        RunEventAsSubroutine(E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        JmpToEvent(E1927_TOWER_BALCONY_JUMP_OFF),
    ]
)
