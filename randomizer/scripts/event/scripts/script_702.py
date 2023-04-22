# pylint: disable=C0301

"""E0702_MARRYMORE_TAKE_PHOTO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_5, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7044_5),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFloatingOff(),
                ASWalkToXYCoords(x=22, y=68),
                ASSetSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASFaceSoutheast(),
            ],
        ),
        Pause(30),
        RunDialog(
            dialog_id=DI2164_MARRYMORE_PHOTO,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Pause(10),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
                ASJumpToHeight(height=108, silent=True),
                ASPause(
                    1, identifier="EVENT_702_action_queue_async_6_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(["EVENT_702_action_queue_async_6_SUBSCRIPT_pause_2"]),
                ASResetProperties(),
            ],
        ),
        RunDialog(
            dialog_id=DI2165_MARRYMORE_PHOTO,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Pause(10),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPause(10),
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True,
                ),
            ],
        ),
        Pause(10),
        RunDialog(
            dialog_id=DI2202_MARRYMORE_PHOTO,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        CircleMaskShrinkToObject(target=NPC_3, width=0, speed=10, static=True),
        PauseScriptUntilEffectDone(),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        CircleMaskShrinkToObject(target=NPC_3, width=255, speed=10, static=True),
        PauseScriptUntilEffectDone(),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Return(),
    ]
)
