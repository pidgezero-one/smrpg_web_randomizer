# pylint: disable=C0301

"""E3745_NIMBUS_BACK_EXIT_INITIATE_FALLING_SEQUENCE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PlaySound(sound=SO019_LONG_FALL, channel=6),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=27, y=29, z=16, direction=SOUTHEAST),
                ASSetSpriteSequence(
                    index=9, sprite_offset=2, is_sequence=True, looping=True
                ),
                ASVisibilityOn(),
                ASFloatingOn(),
                ASShadowOff(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        FadeInFromBlack(sync=True),
        Pause(50),
        PauseScriptUntilEffectDone(),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R372_NIMBUS_LAND_FALL_FROM_PLATFORM_2ND,
            face_direction=SOUTHEAST,
            x=19,
            y=95,
            z=10,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=19, y=95, z=27, direction=SOUTHEAST),
                ASSetSpriteSequence(
                    index=10, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASShadowOff(),
                ASVisibilityOn(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x00\x08\x00")),
            ],
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3745_action_queue_async_9_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3745_action_queue_async_9_SUBSCRIPT_pause_0"]
                ),
                ASBPL262728(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
            ],
        ),
        SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
        Pause(8),
        PauseScriptUntilEffectDone(),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R373_NIMBUS_LAND_FALL_FROM_PLATFORM_3RD,
            face_direction=SOUTHEAST,
            x=27,
            y=91,
            z=6,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=27, y=91, z=16, direction=SOUTHEAST),
                ASSetSpriteSequence(
                    index=30,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASVisibilityOn(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x00\x0c\x00")),
            ],
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3745_action_queue_async_17_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3745_action_queue_async_17_SUBSCRIPT_pause_0"]
                ),
                ASBPL262728(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASShadowOff(),
            ],
        ),
        SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
        Pause(15),
        PauseScriptUntilEffectDone(),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R374_NIMBUS_LAND_FALL_FROM_PLATFORM_4TH,
            face_direction=SOUTHEAST,
            x=27,
            y=115,
            z=6,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=27, y=115, z=16, direction=SOUTHEAST),
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASVisibilityOn(),
                ASShadowOff(),
                ASDb(bytearray(b" \x04")),
                ASDb(bytearray(b"%\x00\x00\x0e\x00")),
            ],
        ),
        FadeInFromBlack(sync=True),
        Pause(50),
        PauseScriptUntilEffectDone(),
        FadeOutToBlack(sync=False),
        SetBit(TEMP_704A_2),
        EnterArea(
            room_id=R370_NIMBUS_LAND_ENTRANCE_TO_HOT_SPRINGS,
            face_direction=SOUTHEAST,
            x=20,
            y=50,
            z=0,
            run_entrance_event=True,
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASVisibilityOff(),
                ASTransferToXYZF(x=20, y=50, z=0, direction=SOUTHEAST),
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_mold=True,
                    is_sequence=True,
                    looping=True,
                ),
                ASVisibilityOn(),
                ASFloatingOn(),
            ],
        ),
        FadeInFromBlack(sync=True),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(
                    1, identifier="EVENT_3745_action_queue_async_32_SUBSCRIPT_pause_0"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_3745_action_queue_async_32_SUBSCRIPT_pause_0"]
                ),
                ASStopSound(),
                ASBPL262728(),
                ASJumpToHeight(height=108, silent=True),
            ],
        ),
        SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkSouthwestSteps(2),
                ASWalkSouthwestPixels(8),
            ],
        ),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
