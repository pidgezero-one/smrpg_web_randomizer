# pylint: disable=C0301

"""E2405_STAR_HILL_FINAL_AREA_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SummonObjectToSpecificLevel(NPC_5, R158_STAR_HILL_AREA_02),
        SummonObjectToSpecificLevel(NPC_6, R158_STAR_HILL_AREA_02),
        SummonObjectToSpecificLevel(NPC_7, R158_STAR_HILL_AREA_02),
        SummonObjectToSpecificLevel(NPC_8, R158_STAR_HILL_AREA_02),
        SummonObjectToSpecificLevel(NPC_6, R157_STAR_HILL_AREA_03),
        SummonObjectToSpecificLevel(NPC_7, R157_STAR_HILL_AREA_03),
        SummonObjectToSpecificLevel(NPC_8, R157_STAR_HILL_AREA_03),
        SummonObjectToSpecificLevel(NPC_9, R157_STAR_HILL_AREA_03),
        SummonObjectToSpecificLevel(NPC_0, R159_STAR_HILL_AREA_04),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASSetWalkingSpeed(FASTEST),
                ASWalkNorthPixels(12),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASShadowOff(),
            ]),
        ActionQueueSync(target=NPC_12, subscript=[ASWalkWestPixels(7)]),
        ActionQueueSync(target=NPC_13, subscript=[ASWalkEastPixels(8)]),
        ActionQueueSync(target=NPC_14, subscript=[ASWalkWestPixels(8)]),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShiftToXYCoords(x=27, y=108),
                ASOverwriteSolidity(),
                ASFloatingOff(),
                ASShadowOff(),
            ]),
        FadeInFromBlack(sync=False),
        Pause(16),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=0
        ),
        PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
        Pause(16),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetSequenceSpeed(FAST), ASWalkSouthwestSteps(2)]
        ),
        Pause(16),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R159_STAR_HILL_AREA_04, mod_id=13
        ),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
    ]
)
