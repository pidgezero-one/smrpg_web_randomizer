# E1592_BELOME_STATUE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StoreItemAmountTo7000(TempleKey),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            0,
            ["EVENT_1592_summon_to_current_level_at_marios_coords_254"],
        ),
        RunDialog(
            dialog_id=DI1235_BELOME_STATUE_KEY_HINT,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        Return(),
        SummonObjectToCurrentLevelAtMariosCoords(
            NPC_12, identifier="EVENT_1592_summon_to_current_level_at_marios_coords_254"
        ),
        ActionQueueAsync(
            target=NPC_12,
            subscript=[
                ASSetSpriteSequence(index=2, is_sequence=True, looping=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetPriority(3),
                ASSetVRAMPriority(PRIORITY_3),
                ASJumpToHeight(112),
                ASWalkToXYCoords(x=1, y=118),
                ASPause(
                    1, identifier="EVENT_1592_action_queue_async_255_SUBSCRIPT_pause_6"
                ),
                ASJmpIfObjectInAir(
                    NPC_12, ["EVENT_1592_action_queue_async_255_SUBSCRIPT_pause_6"]
                ),
                ASSetWalkingSpeed(VERY_FAST),
                ASShiftZUpPixels(8),
                ASSetWalkingSpeed(FAST),
                ASShiftZUpPixels(4),
                ASSetWalkingSpeed(NORMAL),
                ASShiftZUpPixels(2),
            ],
        ),
        ActionQueueAsync(
            target=NPC_16,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASSetSpriteSequence(index=4, is_sequence=True, looping=True),
                ASPause(50),
                ASResetProperties(),
                ASPause(10),
                ASSetSpriteSequence(index=3, looping=False),
            ],
        ),
        RemoveObjectFromCurrentLevel(NPC_12),
        Pause(60),
        PlaySound(sound=SO021_RUMBLING, channel=6),
        SetVarToConst(TEMP_7034, 1),
        Set70107015ToObjectXYZ(NPC_16),
        StartLoopNTimes(2),
        Pause(1, identifier="EVENT_1592_pause_263"),
        CreatePacketAt7010(
            packet=P032_BLUE_CLOUD, destinations=["EVENT_1592_pause_263"]
        ),
        Pause(4),
        AddConstToVar(TEMP_7034, 3),
        EndLoop(),
        ActionQueueAsync(
            target=NPC_16,
            subscript=[
                ASJumpToHeight(128),
                ASStartLoopNTimes(4),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
                ASDb(bytearray(b"\xfd\xf2")),
            ],
        ),
        RemoveOneOfItemFromInventory(TempleKey),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R422_BELOME_TEMPLE_AREA_09_BELOMES_TREASURE_ROOM,
            mod_id=0,
        ),
        SetBit(TEMPLE_KEY_USED),
        Return(),
    ]
)
