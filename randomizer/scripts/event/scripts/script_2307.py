# pylint: disable=C0301

"""E2307_TOWER_BUTTON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(NPC_0),
        JmpIfBitSet(BOOSTER_PASS_SECRET_OPEN, ["EVENT_2307_ret_12"]),
        SetBit(BOOSTER_PASS_SECRET_OPEN),
        SetVarToConst(APPRENTICE_LOSS_COUNTER, 4),
        PlaySound(sound=SO009_GREEN_SWITCH, channel=6),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSpriteSequence(
                    index=1, is_mold=True, is_sequence=True, looping=True
                ),
                ASSetVRAMPriority(MARIO_OVERLAPS_ON_ALL_SIDES),
                ASOverwriteSolidity(),
            ]),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=1
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R100_BOOSTER_PASS_AREA_01, mod_id=0
        ),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetAsyncActionScript(SCREEN_FOCUS, A0391_CAMERA_SHAKE),
        RunDialog(
            dialog_id=DI3154_BOOSTER_PASS_OPENED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(identifier="EVENT_2307_ret_12"),
    ]
)
