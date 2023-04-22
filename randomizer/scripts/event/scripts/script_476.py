# pylint: disable=C0301

"""E0476_INITIATE_MUSHROOM_DERBY_FROM_TALKING_TO_BOSHI"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CircleMaskShrinkToObject(target=MARIO, width=0, speed=3, static=True),
        PauseScriptUntilEffectDone(),
        PauseActionScript(NPC_0),
        PauseActionScript(NPC_2),
        PauseActionScript(NPC_1),
        PauseActionScript(NPC_3),
        PauseActionScript(NPC_5),
        PauseActionScript(NPC_9),
        PauseActionScript(NPC_10),
        StartSyncEmbeddedActionScript(
            target=NPC_0,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=16, y=77, z=0, direction=EAST),
                ASFaceNorthwest(),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_9,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=10, y=81, z=0, direction=EAST),
                ASFaceSoutheast(),
                ASSequenceLoopingOff(),
            ],
        ),
        ActionQueueSync(
            target=NPC_10,
            subscript=[
                ASTransferToXYZF(x=11, y=83, z=0, direction=EAST),
                ASFaceNortheast(),
                ASVisibilityOff(),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_2,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=11, y=75, z=0, direction=EAST),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASFaceSoutheast(),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=MARIO,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=10, y=81, z=0, direction=EAST),
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_1,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=20, y=69, z=0, direction=EAST),
                ASFaceNorthwest(),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_3,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=15, y=67, z=0, direction=EAST),
                ASFaceSoutheast(),
            ],
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_5,
            prefix=0xF1,
            subscript=[
                ASTransferToXYZF(x=19, y=60, z=0, direction=EAST),
                ASTransferXYZFPixels(x=8, y=252, z=0, direction=EAST),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASFaceSoutheast(),
            ],
        ),
        RememberLastObject(),
        RemoveObjectFromCurrentLevel(NPC_13),
        SetBit(TEMP_7049_6),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        JmpIfBitClear(MARRYMORE_LIBERATED, ["EVENT_476_action_queue_sync_191"]),
        SummonObjectToCurrentLevel(NPC_13),
        ActionQueueSync(
            target=NPC_10,
            subscript=[ASFaceNorthwest(), ASVisibilityOn()],
            identifier="EVENT_476_action_queue_sync_191",
        ),
        ActionQueueSync(
            target=NPC_9, subscript=[ASFaceSoutheast(), ASSetSequenceSpeed(SLOW)]
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=5,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        FadeInFromBlack(sync=True),
        PauseScriptUntilEffectDone(),
        Pause(30),
        PlaySound(sound=SO062_BIG_YOSHI_TALK, channel=6),
        Pause(10),
        ActionQueueSync(target=NPC_10, subscript=[ASFaceNortheast()]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=6,
                    sprite_offset=6,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                )
            ],
        ),
        ActionQueueAsync(target=NPC_9, subscript=[ASFaceNortheast()]),
        Pause(60),
        JmpToSubroutine(["EVENT_457_action_queue_sync_0"]),
        RunBackgroundEvent(
            event_id=E0465_MUSHROOM_DERBY_BUSINESS_LOGIC,
            return_on_level_exit=True,
            bit_7=True,
        ),
        EnableControls([]),
        Return(),
    ]
)
