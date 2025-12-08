# pylint: disable=C0301

"""E2524_STAR_HILL_2ND_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ActionQueueSync(target=NPC_16, subscript=[ASWalkEastPixels(7)]),
        ActionQueueSync(target=NPC_17, subscript=[ASWalkEastPixels(6)]),
        ActionQueueSync(target=NPC_18, subscript=[ASWalkWestPixels(9)]),
        ActionQueueSync(target=NPC_19, subscript=[ASWalkWestPixels(8)]),
        ActionQueueSync(target=NPC_20, subscript=[ASWalkWestPixels(10)]),
        FreezeCamera(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShiftToXYCoords(x=14, y=22),
                ASOverwriteSolidity(),
                ASFloatingOff(),
                ASShadowOff(),
            ]),
        FadeInFromBlack(sync=False),
        Pause(16),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=0
        ),
        PlaySound(sound=SO126_EMERGE_DEEP_WATER, channel=6),
        Pause(16),
        ActionQueueAsync(
            target=MARIO, subscript=[ASSetSequenceSpeed(FAST), ASWalkSouthwestSteps(2)]
        ),
        Pause(16),
        Db(bytearray(b"\xfd\x8d")),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R157_STAR_HILL_AREA_03, mod_id=13
        ),
        PlaySound(sound=SO125_ENTER_DEEP_WATER, channel=6),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnfreezeCamera(),
        Return(),
    ]
)
