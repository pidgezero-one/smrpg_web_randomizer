# pylint: disable=C0301

"""E3212_SHIP_3D_MAZE_FORFEIT_LISTENER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_2, identifier="EVENT_3212_pause_action_script_0"),
        RemoveObjectFromCurrentLevel(NPC_2),
        EnableControlsUntilReturn([LEFT, RIGHT, DOWN, UP, A, Y, B]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
        ),
        Pause(1),
        Set7000ToPressedButton(),
        JmpIf7000AllBitsClear(
            bits=[], destinations=["EVENT_3212_pause_action_script_0"]
        ),
        EnableControlsUntilReturn([]),
        SetSyncActionScript(NPC_2, A0351_OERLIKONS_AND_3D_MAZE),
        ActionQueueSync(
            target=MARIO, subscript=[ASSetPriority(3), ASSetVRAMPriority(PRIORITY_3)]
        ),
        Pause(1, identifier="EVENT_3212_pause_10"),
        JmpIfMarioInAir(["EVENT_3212_pause_10"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Z, pixel=True, bit_7=True),
        VarShiftLeft(UNKNOWN_7006, 1),
        CloseDialog(),
        RunDialog(
            dialog_id=DI1658_3D_MAZE_GIVE_UP_PROMPT,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        JmpIfDialogOptionBSelected(["EVENT_3212_pause_action_script_19"]),
        RunDialog(
            dialog_id=DI1657_3D_MAZE_OVERLAY,
            above_object=Bowser,
            closable=False,
            sync=True,
            multiline=False,
            use_background=False,
        ),
        Jmp(["EVENT_3212_pause_action_script_0"]),
        PauseActionScript(NPC_2, identifier="EVENT_3212_pause_action_script_19"),
        RemoveObjectFromCurrentLevel(NPC_2),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASObjectMemoryModifyBits(arg_1=0x09, set_bits=[5], clear_bits=[4, 6]),
                ASSetVRAMPriority(NORMAL_PRIORITY),
            ],
        ),
        EnterArea(
            room_id=R168_SUNKEN_SHIP_PUZZLE_ROOM_3,
            face_direction=NORTHWEST,
            x=31,
            y=116,
            z=0,
            run_entrance_event=True,
        ),
        Return(),
    ]
)
