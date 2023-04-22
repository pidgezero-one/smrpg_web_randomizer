# pylint: disable=C0301

"""E3218_SHIP_SUBMIT_PASSWORD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StopAllBackgroundEvents(),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3218_jmp_if_bit_set_53"]),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_3218_run_dialog_9"]),
        JmpIfBitSet(SHIP_MIDBOSS_COMPLETED, ["EVENT_3218_run_dialog_9"]),
        RunDialog(
            dialog_id=DI1659_SHIP_PASSWORD_INSTRUCTIONS,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        SetBit(TEMP_7044_0),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_3218_ret_8"]),
        RunBackgroundEvent(
            event_id=E3225_SHIP_PASSWORD_BOX_DIALOG, return_on_level_exit=True
        ),
        Return(identifier="EVENT_3218_ret_8"),
        RunDialog(
            dialog_id=DI1706_MY_PASSWORD_IS,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
            identifier="EVENT_3218_run_dialog_9",
        ),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1701),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1713),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        CopyVarToVar(from_var=TEMP_7028, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1725),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        CopyVarToVar(from_var=TEMP_702A, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1737),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        CopyVarToVar(from_var=TEMP_702C, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1749),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        CopyVarToVar(from_var=TEMP_702E, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 1761),
        RunDialog(
            dialog_id=PRIMARY_TEMP_7000,
            above_object=NPC_12,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        RunDialog(
            dialog_id=DI1707_EMPTY,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        SetVarToConst(TEMP_70AC, 0),
        SetBit(TEMP_7042_2),
        RunEventAsSubroutine(E3411_SHIP_PASSWORD_CORRECTNESS_CHECK),
        JmpIfVarNotEqualsConst(TEMP_70AC, 6, ["EVENT_3218_play_sound_56"]),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        JmpIfBitSet(SHIP_MIDBOSS_COMPLETED, ["EVENT_3218_jmp_if_bit_set_59"]),
        SetSyncActionScript(NPC_7, A0203_SHIP_PASSWORD_BOSS_REVEAL),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceNortheast(),
                ASFixedFCoordOn(),
                ASWalkSouthwestSteps(3),
                ASFixedFCoordOff(),
            ],
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplySolidityModToLevel(
            permanent=True, room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            mod_id=32,
        ),
        SetBit(TEMP_7043_0),
        SetBit(TEMP_7042_6),
        JmpIfBitSet(
            SHIP_MIDBOSS_COMPLETED,
            ["EVENT_3218_jmp_if_bit_set_59"],
            identifier="EVENT_3218_jmp_if_bit_set_53",
        ),
        RunDialog(
            dialog_id=DI1660_SHIP_PASSWORD_COMPLETE,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
        PlaySound(
            sound=SO088_WRONG_SIGNAL, channel=6, identifier="EVENT_3218_play_sound_56"
        ),
        RunBackgroundEvent(
            event_id=E3225_SHIP_PASSWORD_BOX_DIALOG, return_on_level_exit=True
        ),
        Return(),
        JmpIfBitSet(
            TEMP_7043_0,
            ["EVENT_3218_ret_65"],
            identifier="EVENT_3218_jmp_if_bit_set_59",
        ),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplySolidityModToLevel(
            permanent=True, room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM, mod_id=0
        ),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R177_SUNKEN_SHIP_AREA_09_PASSWORD_ROOM,
            mod_id=32,
        ),
        SetBit(TEMP_7043_0),
        SetBit(TEMP_7042_6),
        Return(identifier="EVENT_3218_ret_65"),
    ]
)
