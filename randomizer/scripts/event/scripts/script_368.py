# pylint: disable=C0301

"""E0368_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set0158Bit7Offset(0x015C),
        Set0158Bit7Offset(0x015E),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShadowOff(),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthPixels(6),
                ASWalkNorthwestPixels(2),
            ]),
        ActionQueueSync(target=NPC_4, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_5, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_7, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_6, subscript=[ASSetPriority(2)]),
        ActionQueueSync(target=NPC_3, subscript=[ASSetPriority(3)]),
        ActionQueueSync(target=NPC_10, subscript=[ASSetPriority(2)]),
        ActionQueueAsync(
            target=NPC_2,
            subscript=[
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASVisibilityOff(),
            ]),
        FreezeCamera(),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASBounceToXYWithHeight(x=10, y=19, height=6),
                ASTransferXYZFPixels(x=0, y=252, z=0, direction=EAST),
            ]),
        RunEventAsSubroutine(
            E0761_MUSHROOM_KINGDOM_OCCUPIED_THRONE_ROOM_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        FadeInFromBlack(sync=False),
        SetBit(TEMP_7043_5),
        Pause(30),
        ClearBit(TEMP_7043_5),
        ActionQueueAsync(target=NPC_6, subscript=[ASSetSolidityBits(bit_4=True)]),
        ActionQueueAsync(target=NPC_7, subscript=[ASSetSolidityBits(bit_4=True)]),
        SetBit(TEMP_7043_6),
        SetSyncActionScript(NPC_4, A0101_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_5, A0102_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_8, A0101_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_9, A0102_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_6, A0101_MK_THRONE_HENCHMAN_BOUNCE),
        SetSyncActionScript(NPC_7, A0102_MK_THRONE_HENCHMAN_BOUNCE),
        Pause(60),
        SetBit(TEMP_7049_2),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        UnfreezeCamera(),
        Return(),
    ]
)
