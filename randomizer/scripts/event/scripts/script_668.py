# pylint: disable=C0301

"""E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM"""

from randomizer.scripts.event.script_imports import *
from randomizer.entities.items.items import Ring, Shoes, Crown, Brooch

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_7063_5, ["EVENT_256_ret_0"]),
        JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7044_5),
        StopBackgroundEvent(TIMER_701C),
        StopBackgroundEvent(TIMER_701E),
        Pause(10),
        ActionQueueSync(target=MARIO, subscript=[ASFaceSouthwest()]),
        ActionQueueSync(
            target=NPC_8,
            subscript=[ASFixedFCoordOff(), ASResetProperties(), ASFaceSouthwest()],
        ),
        ActionQueueSync(
            target=NPC_11,
            subscript=[
                ASTransferToXYZF(x=9, y=97, z=0, direction=EAST),
                ASTransferXYZFPixels(x=16, y=8, z=0, direction=EAST),
            ],
        ),
        ActionQueueSync(
            target=NPC_9,
            subscript=[
                ASTransferToXYZF(x=9, y=98, z=0, direction=EAST),
                ASTransferXYZFPixels(x=8, y=4, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_10,
            subscript=[
                ASTransferToXYZF(x=10, y=95, z=0, direction=EAST),
                ASTransferXYZFPixels(x=254, y=4, z=0, direction=EAST),
                ASFaceNortheast(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=5, y=85)],
        ),
        RememberLastObject(),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Pause(30),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitSet(GAME_OVER, ["EVENT_287_reset_and_choose_game_0"]),
        RestoreAllHP(),
        RestoreAllFP(),
        RunEventAsSubroutine(E0276_REFOCUS_CAMERA_ON_SELF),
        RememberLastObject(),
        RemoveObjectFromCurrentLevel(NPC_0),
        RemoveObjectFromCurrentLevel(NPC_1),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromCurrentLevel(NPC_8),
        RemoveObjectFromCurrentLevel(NPC_9),
        RemoveObjectFromCurrentLevel(NPC_10),
        RemoveObjectFromCurrentLevel(NPC_11),
        RemoveObjectFromSpecificLevel(
            NPC_0, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_1, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_2, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_7, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_8, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_9, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_10, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RemoveObjectFromSpecificLevel(
            NPC_11, R154_MARRYMORE_CHAPEL_SANCTUARY_DURING_BOOSTER
        ),
        RunEventAsSubroutine(E0200_UNLOCK_FOREST_IF_GATED_BY_MARRYMORE_CHARACTER),
        FadeInFromBlack(sync=False),
        ClearBit(TEMP_704C_0),
        SetBit(MARRYMORE_LIBERATED),
        SetBit(MAP_STAR_HILL),
        SetBit(TEMP_7042_1),
        ClearBit(TEMP_7042_0),
        ClearBit(TEMP_7042_2),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=1
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=2
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=3
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=4
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=5
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=6
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R065_MARRYMORE_CHAPEL_SANCTUARY, mod_id=7
        ),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        RunEventAsSubroutine(E0186_PARTY_JOIN_LOGIC),
        RemoveOneOfItemFromInventory(Shoes),
        RemoveOneOfItemFromInventory(Brooch),
        RemoveOneOfItemFromInventory(Ring),
        RemoveOneOfItemFromInventory(Crown),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(),
    ]
)
