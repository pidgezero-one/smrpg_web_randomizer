# E1913_ABYSS_MACHINE_ARROW_ANIMATE

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_1, ["EVENT_1913_ret_25"]),
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1913_ret_25"]),
        SetBit(TEMP_7043_0),
        ClearBit(TEMP_7043_2),
        Set7016701BToObjectXYZ(MARIO),
        AddConstToVar(Z_COORD_2, 2048),
        Set7000ToPressedButton(),
        JmpIf7000AllBitsClear(destinations=["EVENT_1913_action_queue_sync_24"]),
        Set7000ToPressedButton(),
        JmpIf7000AnyBitsSet(destinations=["EVENT_1913_set_7000_to_object_coord_11"]),
        SetBit(TEMP_7043_2),
        Set7000ToObjectCoord(
            object=MARIO,
            coord=COORD_F,
            pixel=True,
            identifier="EVENT_1913_set_7000_to_object_coord_11",
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 6, ["EVENT_1913_add_short_18"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 7, ["EVENT_1913_add_short_20"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_1913_add_short_23"]),
        AddConstToVar(X_COORD_2, 65344),
        AddConstToVar(Y_COORD_2, 192),
        Jmp(["EVENT_1913_action_queue_sync_24"]),
        AddConstToVar(Y_COORD_2, 65152, identifier="EVENT_1913_add_short_18"),
        Jmp(["EVENT_1913_action_queue_sync_24"]),
        AddConstToVar(X_COORD_2, 384, identifier="EVENT_1913_add_short_20"),
        AddConstToVar(Y_COORD_2, 65344),
        Jmp(["EVENT_1913_action_queue_sync_24"]),
        AddConstToVar(X_COORD_2, 384, identifier="EVENT_1913_add_short_23"),
        ActionQueueSync(
            target=NPC_8,
            subscript=[
                ASJmpIfBitClear(
                    TEMP_7043_2, ["EVENT_1913_action_queue_sync_24_SUBSCRIPT_db_2"]
                ),
                ASPause(4),
                ASDb(
                    bytearray(b"\x99"),
                    identifier="EVENT_1913_action_queue_sync_24_SUBSCRIPT_db_2",
                ),
                ASObjectMemoryClearBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO078_CLICK, channel=4),
                ASVisibilityOn(),
                ASFloatingOff(),
                ASSetWalkingSpeed(FASTEST),
                ASShiftZDownSteps(8),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASStartLoopNTimes(7),
                ASVisibilityOn(),
                ASPause(1),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
                ASClearBit(TEMP_7043_0),
            ],
            identifier="EVENT_1913_action_queue_sync_24",
        ),
        Return(identifier="EVENT_1913_ret_25"),
    ]
)
