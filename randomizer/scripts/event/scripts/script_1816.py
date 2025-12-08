# pylint: disable=C0301

"""E1816_TROOPA_CLIFF_FINISH"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_7, ["EVENT_1816_ret_82"]),
        JmpIfBitSet(TEMP_7044_2, ["EVENT_1816_ret_82"]),
        SetBit(TEMP_7044_2),
        StopAllBackgroundEvents(),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7044_1),
        StopSound(),
        Pause(1),
        PlaySound(sound=SO143_METRONOME_UPBEAT_DING, channel=6),
        FadeOutMusicToVolume(duration=2, volume=127),
        SetVarToConst(TEMP_70AB, 21),
        RunEventAsSubroutine(E1739_REFOCUS_CAMERA),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=25, y=112),
                ASFaceNortheast(),
                ASSetAllSpeeds(NORMAL),
            ]),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetSpriteSequence(index=3, is_sequence=True, looping=False),
                ASPause(20),
                ASPlaySound(sound=SO133_CLOSE_HIT_DOOR, channel=4),
                ASPause(20),
            ]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI1263_TROOPA_CLIFF_TIME,
            above_object=MARIO,
            closable=False,
            sync=False,
            multiline=True,
            use_background=False),
        ActionQueueAsync(target=NPC_1, subscript=[ASResetProperties()]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 1800),
        JmpIfComparisonResultIsLesser(["EVENT_1816_mem_compare_val_22"]),
        Return(),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 840, identifier="EVENT_1816_mem_compare_val_22"
        ),
        JmpIfComparisonResultIsLesser(["EVENT_1816_mem_compare_val_26"]),
        Return(),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 720, identifier="EVENT_1816_mem_compare_val_26"
        ),
        JmpIfComparisonResultIsLesser(["EVENT_1816_mem_compare_val_32"]),
        JmpIfRandom2of3(["EVENT_1816_ret_82", "EVENT_1816_ret_82"]),
        SetVarToConst(TEMP_7028, 1),
        Jmp(["EVENT_1816_action_queue_sync_74"]),
        CompareVarToConst(
            PRIMARY_TEMP_7000, 660, identifier="EVENT_1816_mem_compare_val_32"
        ),
        JmpIfComparisonResultIsLesser(["EVENT_1816_jmp_if_bit_clear_71"]),
        JmpIfBitSet(UNKNOWN_LARGE_CONVEYOR_ROOM, ["EVENT_1816_set_short_64"]),
        SetBit(UNKNOWN_LARGE_CONVEYOR_ROOM, identifier="EVENT_1816_set_bit_36"),
        RunEventAsSubroutine(E0178_NPC_QUEST_1_CONTAINER),
        Return(),
        SetVarToConst(TEMP_7028, 1, identifier="EVENT_1816_set_short_64"),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        CompareVarToConst(PRIMARY_TEMP_7000, 690),
        JmpIfComparisonResultIsLesser(["EVENT_1816_jmp_69"]),
        JmpIfRandom1of2(["EVENT_1816_ret_82"]),
        Jmp(["EVENT_1816_action_queue_sync_74"], identifier="EVENT_1816_jmp_69"),
        JmpIfBitClear(
            UNKNOWN_LARGE_CONVEYOR_ROOM,
            ["EVENT_1816_set_bit_36"],
            identifier="EVENT_1816_jmp_if_bit_clear_71"),
        SetVarToConst(TEMP_7028, 5),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSpriteSequence(
                    index=9,
                    sprite_offset=2,
                    is_sequence=True,
                    looping=True,
                    mirror_sprite=True)
            ],
            identifier="EVENT_1816_action_queue_sync_74"),
        SetObjectMemoryToVar(TEMP_7028),
        ActionQueueAsync(
            target=NPC_10,
            subscript=[
                ASPlaySound(sound=SO094_FROG_COIN, channel=4),
                ASShadowOff(),
                ASSetVRAMPriority(PRIORITY_3),
                ASSetPriority(3),
                ASSetSpriteSequence(index=1, is_sequence=True, looping=True),
                ASDb(bytearray(b"\x97\x15")),
                ASSetAllSpeeds(FASTEST),
                ASShiftZUpPixels(16),
                ASSetAllSpeeds(NORMAL),
                ASVisibilityOn(),
                ASFloatingOff(),
                ASJumpToHeight(height=80, silent=True),
                ASWalk1StepSouthwest(),
                ASPause(6),
                ASVisibilityOff(),
            ]),
        SetVarToConst(PRIMARY_TEMP_7000, 1),
        AddFrogCoins(PRIMARY_TEMP_7000),
        EndLoop(),
        Pause(30),
        ActionQueueAsync(target=MARIO, subscript=[ASResetProperties()]),
        Return(identifier="EVENT_1816_ret_82"),
    ]
)
