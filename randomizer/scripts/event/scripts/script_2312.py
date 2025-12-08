# pylint: disable=C0301

"""E2312_BOOSTER_PASS_SPINY_COIN_BUTTON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(UNKNOWN_7047_6, ["EVENT_2312_ret_78"]),
        DisableObjectTrigger(NPC_5),
        SetBit(UNKNOWN_7047_6),
        RemoveObjectFromSpecificLevel(NPC_0, R101_BOOSTER_PASS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_1, R101_BOOSTER_PASS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_2, R101_BOOSTER_PASS_AREA_02),
        RemoveObjectFromSpecificLevel(NPC_3, R101_BOOSTER_PASS_AREA_02),
        Store01To0248(),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=3, y=94)]),
        Pause(8),
        JmpIfObjectInCurrentLevel(NPC_0, ["EVENT_2312_apply_tile_mod_18"]),
        Pause(1, identifier="EVENT_2312_pause_12"),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_2312_pause_12"]),
        SetBit(TEMP_7042_0),
        RemoveObjectFromCurrentLevel(NPC_0),
        AddCoins(10),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=7, y=115, z=8, direction=EAST),
                ASVisibilityOn(),
                ASPlaySound(sound=SO013_COIN, channel=6),
                ASSetPriority(3),
                ASJumpToHeight(128),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R101_BOOSTER_PASS_AREA_02,
            mod_id=4,
            identifier="EVENT_2312_apply_tile_mod_18"),
        JmpIfBitSet(TEMP_7042_0, ["EVENT_2312_set_action_script_sync_21"]),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetSyncActionScript(
            SCREEN_FOCUS,
            A0391_CAMERA_SHAKE,
            identifier="EVENT_2312_set_action_script_sync_21"),
        Pause(8),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=0
        ),
        Pause(48),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=4, y=85)]),
        Pause(8),
        JmpIfObjectInCurrentLevel(NPC_1, ["EVENT_2312_apply_tile_mod_34"]),
        Pause(1, identifier="EVENT_2312_pause_28"),
        JmpIfBitSet(TEMP_7043_1, ["EVENT_2312_pause_28"]),
        SetBit(TEMP_7042_1),
        RemoveObjectFromCurrentLevel(NPC_1),
        AddCoins(10),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=8, y=109, z=8, direction=EAST),
                ASVisibilityOn(),
                ASPlaySound(sound=SO013_COIN, channel=6),
                ASJumpToHeight(128),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R101_BOOSTER_PASS_AREA_02,
            mod_id=5,
            identifier="EVENT_2312_apply_tile_mod_34"),
        JmpIfBitSet(TEMP_7042_1, ["EVENT_2312_set_action_script_sync_37"]),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetSyncActionScript(
            SCREEN_FOCUS,
            A0391_CAMERA_SHAKE,
            identifier="EVENT_2312_set_action_script_sync_37"),
        Pause(8),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=1
        ),
        Pause(48),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=8, y=85)]),
        Pause(8),
        JmpIfObjectInCurrentLevel(NPC_2, ["EVENT_2312_apply_tile_mod_50"]),
        Pause(1, identifier="EVENT_2312_pause_44"),
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2312_pause_44"]),
        SetBit(TEMP_7042_2),
        RemoveObjectFromCurrentLevel(NPC_2),
        AddCoins(10),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASFloatingOff(),
                ASTransferToXYZF(x=12, y=109, z=8, direction=EAST),
                ASVisibilityOn(),
                ASPlaySound(sound=SO013_COIN, channel=6),
                ASJumpToHeight(128),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R101_BOOSTER_PASS_AREA_02,
            mod_id=6,
            identifier="EVENT_2312_apply_tile_mod_50"),
        JmpIfBitSet(TEMP_7042_2, ["EVENT_2312_set_action_script_sync_53"]),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetSyncActionScript(
            SCREEN_FOCUS,
            A0391_CAMERA_SHAKE,
            identifier="EVENT_2312_set_action_script_sync_53"),
        Pause(8),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=2
        ),
        Pause(48),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=8, y=73)]),
        Pause(8),
        JmpIfObjectInCurrentLevel(NPC_3, ["EVENT_2312_apply_tile_mod_65"]),
        Pause(1, identifier="EVENT_2312_pause_60"),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2312_pause_60"]),
        RemoveObjectFromCurrentLevel(NPC_3),
        AddCoins(10),
        ActionQueueSync(
            target=NPC_4,
            subscript=[
                ASSetBit(TEMP_7042_3),
                ASFloatingOff(),
                ASTransferToXYZF(x=11, y=97, z=12, direction=EAST),
                ASVisibilityOn(),
                ASPlaySound(sound=SO013_COIN, channel=6),
                ASJumpToHeight(128),
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASPause(32),
                ASVisibilityOff(),
            ]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R101_BOOSTER_PASS_AREA_02,
            mod_id=7,
            identifier="EVENT_2312_apply_tile_mod_65"),
        JmpIfBitSet(TEMP_7042_3, ["EVENT_2312_set_action_script_sync_68"]),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetSyncActionScript(
            SCREEN_FOCUS,
            A0391_CAMERA_SHAKE,
            identifier="EVENT_2312_set_action_script_sync_68"),
        Pause(8),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=3
        ),
        Pause(48),
        ApplySolidityModToLevel(
            permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=1
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=2
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R101_BOOSTER_PASS_AREA_02, mod_id=3
        ),
        Store00To0248(),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[ASSetWalkingSpeed(FAST), ASWalkToXYCoords(x=6, y=95)]),
        Return(identifier="EVENT_2312_ret_78"),
    ]
)
