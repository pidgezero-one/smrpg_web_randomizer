# pylint: disable=C0301

"""E2064_DOJO_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkEastSteps(2),
                ASShiftNorthSteps(1),
                ASWalkNorthPixels(8),
            ],
        ),
        JmpIfBitSet(DOJO_BOSS_4_DEFEATED, ["EVENT_2064_action_queue_sync_15"]),
        JmpIfBitSet(DOJO_BOSS_3_DEFEATED, ["EVENT_2064_action_queue_sync___11"]),
        JmpIfBitSet(DOJO_BOSS_2_DEFEATED, ["EVENT_2064_action_queue_sync__11"]),
        JmpIfBitSet(DOJO_BOSS_1_DEFEATED, ["EVENT_2064_action_queue_sync_11"]),
        JmpIfBitSet(
            INITIAL_DOJO_CUTSCENE_COMPLETED, ["EVENT_2064_action_queue_async_8"]
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=6, y=13),
                ASFaceNortheast(),
                ASVisibilityOn(),
            ],
        ),
        RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_2065_pause_0"]),
        Return(),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASTransferToXYZF(x=5, y=15, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
            identifier="EVENT_2064_action_queue_async_8",
        ),
        RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=5, y=9),
                ASFaceSoutheast(),
                ASVisibilityOn(),
            ],
            identifier="EVENT_2064_action_queue_sync_11",
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=5, y=15, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=5, y=9),
                ASFaceSoutheast(),
                ASVisibilityOn(),
            ],
            identifier="EVENT_2064_action_queue_sync__11",
        ),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASTransferToXYZF(x=5, y=15, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=5, y=9),
                ASFaceSoutheast(),
                ASVisibilityOn(),
            ],
            identifier="EVENT_2064_action_queue_sync___11",
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=5, y=15, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
            ],
        ),
        RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=5, y=14),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
            ],
            identifier="EVENT_2064_action_queue_sync_15",
        ),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferToXYZF(x=6, y=16, z=0, direction=EAST),
                ASFaceSouthwest(),
                ASVisibilityOn(),
                ASShadowOn(),
                ASObjectMemoryClearBit(arg_1=0x08, bits=[3, 4]),
            ],
        ),
        SetSyncActionScript(NPC_3, A1006_DOJO_PERMA_JUMP),
        SetSyncActionScript(NPC_1, A1006_DOJO_PERMA_JUMP),
        RunEventAsSubroutine(E0815_DOJO_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
