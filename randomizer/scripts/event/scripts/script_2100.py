# pylint: disable=C0301

"""E2100_HINOPIO"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_2, ["EVENT_2100_run_dialog_6"]),
        JmpIfBitSet(TEMP_7043_3, ["EVENT_2100_open_shop_49"]),
        JmpToEvent(E1183_VOLCANO_ITEM_SHOP),
        RunDialog(
            dialog_id=DI2576_VOLCANO_INN,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_2100_run_dialog_6"),
        JmpIfDialogOptionBSelected(["EVENT_2100_ret_45"]),
        StoreCoinCountTo7000(),
        CompareVarToConst(PRIMARY_TEMP_7000, 30),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_2100_set_13"]),
        RunDialog(
            dialog_id=DI2578_VOLCANO_INN_INSUFFICIENT_COINS,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True),
        Return(),
        SetVarToConst(PRIMARY_TEMP_7000, 30, identifier="EVENT_2100_set_13"),
        Dec7000FromCoins(),
        FadeOutMusicToVolume(duration=2, volume=0),
        CircleMaskShrinkToObject(target=MARIO, width=18, speed=3, static=True),
        Pause(10),
        PlaySound(sound=SO054_GOODNIGHT, channel=6),
        Pause(50),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=30,
                    sprite_offset=2,
                    is_mold=True,
                    is_sequence=True,
                    looping=True)
            ]),
        Pause(60),
        CircleMaskShrinkToObject(target=MARIO, width=0, speed=1, static=True),
        Pause(30),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASTransferToXYZF(x=8, y=56, z=2, direction=EAST),
                ASWalkSoutheastPixels(8),
                ASWalkSouthwestPixels(8),
                ASSetSpriteSequence(
                    index=8, sprite_offset=2, is_sequence=True, looping=True
                ),
            ]),
        ActionQueueSync(target=NPC_0, subscript=[ASFaceNortheast()]),
        ActionQueueAsync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASBounceToXYWithHeight(x=4, y=41, height=0),
            ]),
        Pause(30),
        CircleMaskShrinkToObject(target=MARIO, width=40, speed=3, static=True),
        Pause(10),
        FadeOutMusicToVolume(duration=6, volume=100),
        Pause(10),
        Set7000ToTappedButton(identifier="EVENT_2100_set_7000_to_tapped_button_33"),
        Pause(1),
        Mem7000AndConst(0x0080),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 128, ["EVENT_2100_circle_mask_static_38"]
        ),
        Jmp(["EVENT_2100_set_7000_to_tapped_button_33"]),
        CircleMaskShrinkToObject(
            target=MARIO,
            width=255,
            speed=5,
            static=True,
            identifier="EVENT_2100_circle_mask_static_38"),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASSetSequenceSpeed(NORMAL),
                ASJumpToHeight(120),
                ASPause(60),
                ASSetAllSpeeds(NORMAL),
            ]),
        ActionQueueAsync(target=NPC_0, subscript=[ASFaceSouthwest()]),
        Pause(20),
        RestoreAllHP(),
        RestoreAllFP(),
        Return(identifier="EVENT_2100_ret_45"),
        JmpToEvent(E1184_VOLCANO_ARMOR_SHOP, identifier="EVENT_2100_open_shop_49"),
    ]
)
