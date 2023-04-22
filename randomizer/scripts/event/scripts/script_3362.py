# pylint: disable=C0301

"""E3362_KEEP_BUTTON_GAME_PRESS_BUTTON"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        DisableObjectTrigger(MEM_70A8),
        CopyVarToVar(from_var=ROSE_WAY_703E, to_var=ROSE_WAY_703C),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 21, ["EVENT_3362_set_7000_to_7000_short_mem_18"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 22, ["EVENT_3362_set_7000_to_7000_short_mem_22"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 23, ["EVENT_3362_set_7000_to_7000_short_mem_26"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 24, ["EVENT_3362_set_7000_to_7000_short_mem_30"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 25, ["EVENT_3362_set_7000_to_7000_short_mem_34"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 26, ["EVENT_3362_set_7000_to_7000_short_mem_38"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 27, ["EVENT_3362_set_7000_to_7000_short_mem_42"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 28, ["EVENT_3362_set_7000_to_7000_short_mem_46"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 29, ["EVENT_3362_set_7000_to_7000_short_mem_50"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 30, ["EVENT_3362_set_7000_to_7000_short_mem_54"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 31, ["EVENT_3362_set_7000_to_7000_short_mem_58"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 32, ["EVENT_3362_set_7000_to_7000_short_mem_62"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 33, ["EVENT_3362_set_7000_to_7000_short_mem_66"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 34, ["EVENT_3362_set_7000_to_7000_short_mem_70"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 35, ["EVENT_3362_set_7000_to_7000_short_mem_74"]
        ),
        JmpIfVarEqualsConst(
            ACTIVE_NPC, 36, ["EVENT_3362_set_7000_to_7000_short_mem_78"]
        ),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_18",
        ),
        Mem7000XorConst(0x0013),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_22",
        ),
        Mem7000XorConst(0x0027),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_26",
        ),
        Mem7000XorConst(0x004E),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_30",
        ),
        Mem7000XorConst(0x008C),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_34",
        ),
        Mem7000XorConst(0x0131),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_38",
        ),
        Mem7000XorConst(0x0272),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_42",
        ),
        Mem7000XorConst(0x04E4),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_46",
        ),
        Mem7000XorConst(0x08C8),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_50",
        ),
        Mem7000XorConst(0x1310),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_54",
        ),
        Mem7000XorConst(0x2720),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_58",
        ),
        Mem7000XorConst(0x4E40),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_62",
        ),
        Mem7000XorConst(0x8C80),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_66",
        ),
        Mem7000XorConst(0x3100),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_70",
        ),
        Mem7000XorConst(0x7200),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_74",
        ),
        Mem7000XorConst(0xE400),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        CopyVarToVar(
            from_var=ROSE_WAY_703E,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_3362_set_7000_to_7000_short_mem_78",
        ),
        Mem7000XorConst(0xC800),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=ROSE_WAY_703E),
        Jmp(["EVENT_3362_set_82"]),
        SetVarToConst(TEMP_70A9, 21, identifier="EVENT_3362_set_82"),
        StartLoopNTimes(15),
        SetSyncActionScript(MEM_70A9, A0281_KEEP_TOPPER_GAME_SET_BUTTON_OR_BALL_STATE),
        Inc(TEMP_70A9),
        EndLoop(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASShiftZDownPixels(8),
                ASJumpToHeight(height=0, silent=True),
                ASResetProperties(),
                ASPause(1),
            ],
        ),
        JmpIfVarNotEqualsConst(ROSE_WAY_703E, 65535, ["EVENT_3362_ret_102"]),
        Pause(8),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOn(),
                ASPause(2),
                ASVisibilityOff(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOn(),
            ],
        ),
        ClearBit(TEMP_7044_7),
        SetSyncActionScript(
            NPC_0, A0059_SEWER_STAIR_UPPER_RIGHT_RAT_PACING_AND_BOWSERS_KEEP_GAME_MOLDS
        ),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=4),
        Pause(16),
        PlayMusicAtDefaultVolume(M09_VICTORY),
        SetBit(TEMP_7044_7),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES,
            mod_id=0,
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R465_BOWSERS_KEEP_6DOOR_PUZZLE_ROOM_2B_GREEN_SWITCHES,
            mod_id=0,
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASStartLoopNTimes(3),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASVisibilityOff(),
            ],
        ),
        Return(identifier="EVENT_3362_ret_102"),
    ]
)
