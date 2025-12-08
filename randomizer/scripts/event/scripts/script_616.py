# pylint: disable=C0301

"""E0616_MARRYMORE_INN_LOBBY_EXIT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7042_0, ["EVENT_616_jmp_if_bit_set_8"]),
        JmpIfBitSet(
            TEMP_704C_0, ["EVENT_256_ret_0"], identifier="EVENT_616_jmp_if_bit_set_1"
        ),
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_256_ret_0"]),
        JmpIfBitSet(MARRYMORE_LIBERATED, ["EVENT_616_enter_area_6"]),
        EnterArea(
            room_id=R005_MARRYMORE_OUTSIDE_DURING_BOOSTER,
            face_direction=SOUTHEAST,
            x=5,
            y=73,
            z=4,
            run_entrance_event=True),
        Return(),
        EnterArea(
            room_id=R064_MARRYMORE_OUTSIDE,
            face_direction=SOUTHEAST,
            x=5,
            y=73,
            z=4,
            run_entrance_event=True,
            identifier="EVENT_616_enter_area_6"),
        Return(),
        JmpIfBitSet(
            TEMP_7042_5,
            ["EVENT_616_jmp_if_bit_set_1"],
            identifier="EVENT_616_jmp_if_bit_set_8"),
        JmpIfBitSet(TEMP_7042_6, ["EVENT_616_jmp_if_bit_set_1"]),
        RunDialog(
            dialog_id=DI0997_CAPS_LOCK_HONORIFIC,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=0,
                    sprite_offset=3,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True),
                ASJumpToHeight(height=64, silent=True),
                ASPause(
                    1, identifier="EVENT_616_action_queue_async_11_SUBSCRIPT_pause_2"
                ),
                ASJmpIfMarioInAir(
                    ["EVENT_616_action_queue_async_11_SUBSCRIPT_pause_2"]
                ),
                ASPause(30),
                ASResetProperties(),
                ASWalkToXYCoords(x=6, y=62),
                ASFaceNorthwest(),
            ]),
        RunDialog(
            dialog_id=DI0968_DUPLICATE,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        JmpIfDialogOptionBSelected(["EVENT_616_set_action_script_sync_18"]),
        SetAsyncActionScript(MARIO, A0671_SHAKE_HEAD_NO),
        Pause(10),
        RunDialog(
            dialog_id=DI0974_ENJOY_YOUR_STAY,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Return(),
        SetSyncActionScript(
            MARIO, A0670_NOD_YES, identifier="EVENT_616_set_action_script_sync_18"
        ),
        Pause(10),
        RunDialog(
            dialog_id=DI0996_DROP_BY_AGAIN,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        Pause(10),
        UnsyncDialog(),
        ActionQueueAsync(target=MARIO, subscript=[ASWalk1StepSoutheast()]),
        Jmp(["EVENT_616_jmp_if_bit_set_1"]),
    ]
)
