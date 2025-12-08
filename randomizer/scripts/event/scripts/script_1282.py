# pylint: disable=C0301

"""E1282_TOWER_BALCONY_LOADER_AFTER_MARRYMORE"""

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
            target=NPC_3,
            subscript=[
                ASSetPriority(3),
                ASWalkNortheastPixels(10),
                ASWalkNorthPixels(2),
                ASWalkWestPixels(2),
                ASFaceSouthwest(),
            ]),
        JmpIfBitSet(NIMBUS_LAND_LIBERATED, ["EVENT_1282_jmp_to_event_17"]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=5, y=16, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=6, y=18, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=7, y=20, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceSouthwest(),
                ASSequenceLoopingOn(),
            ]),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetPriority(3),
                ASTransferToXYZF(x=4, y=21, z=0, direction=EAST),
                ASVisibilityOn(),
                ASFaceSouthwest(),
                ASSetSpriteSequence(index=6, is_mold=True, looping=True),
            ]),
        RunEventAsSubroutine(E0794_TOWER_BALCONY_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        JmpToEvent(E1927_TOWER_BALCONY_JUMP_OFF),
        JmpToEvent(
            E2278_BALCONY_LOADER_AFTER_NIMBUS_CASTLE,
            identifier="EVENT_1282_jmp_to_event_17"),
        Return(),
    ]
)
