# pylint: disable=C0301

"""E1564_LANDS_END_CANNON_CONTD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetBit(TEMP_7044_4),
        Db(bytearray(b"\xc7\x90")),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASRunAwayShift(),
                ASFaceSouth(),
                ASFloatingOn(),
                ASPause(6),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSouthPixels(2),
                ASWalkNorthPixels(4),
                ASWalkSouthPixels(4),
                ASWalkNorthPixels(2),
                ASSetWalkingSpeed(NORMAL),
                ASWalkNorthPixels(12),
            ],
        ),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                )
            ],
        ),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASPlaySound(sound=SO009_GREEN_SWITCH, channel=4),
                ASShiftZDownPixels(4),
                ASVisibilityOff(),
                ASShiftZDownPixels(12),
            ],
        ),
        Set7000ToObjectCoord(target_npc=MEM_70A8, coord=COORD_F, pixel=True),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 1, ["EVENT_1564_set_action_script_sync_10"]
        ),
        SetSyncActionScript(MEM_70A8, A0782_LANDS_END_CANNON_WHILE_PLAYER_OCCUPIED),
        Jmp(["EVENT_1564_pause_11"]),
        SetSyncActionScript(
            MEM_70A8,
            A0783_LANDS_END_CANNON_WHILE_PLAYER_OCCUPIED,
            identifier="EVENT_1564_set_action_script_sync_10",
        ),
        Pause(1, identifier="EVENT_1564_pause_11"),
        Pause(1, identifier="EVENT_1564_pause_12"),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(bits=[], destinations=["EVENT_1564_pause_12"]),
        CopyVarToVar(from_var=SECONDARY_TEMP_7024, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_7026),
        VarShiftLeft(PRIMARY_TEMP_7000, 8),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=PRIMARY_TEMP_700C),
        CopyVarToVar(from_var=TEMP_7026, to_var=PRIMARY_TEMP_7000),
        Mem7000AndConst(0x00FF),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1564_action_queue_async_29"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 2, ["EVENT_1564_action_queue_async_32"]),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_1564_action_queue_async_35"]),
        ClearBit(TEMP_7044_4),
        StopSound(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASFaceEast7C(),
                ASFloatingOff(),
                ASJumpToHeight(height=192, silent=True),
                ASSetVarToConst(TEMP_7034, 61166),
                ASCreatePacketAtObjectCoords(
                    packet=P032_BLUE_CLOUD,
                    target_npc=MARIO,
                    destinations=[
                        "EVENT_1564_action_queue_async_26_SUBSCRIPT_set_animation_speed_5"
                    ],
                ),
                ASSetWalkingSpeed(
                    NORMAL,
                    identifier="EVENT_1564_action_queue_async_26_SUBSCRIPT_set_animation_speed_5",
                ),
                ASPause(2),
                ASPlaySound(sound=SO033_JUMPING_BOUNCING_FISH, channel=4),
                ASFloatingOn(),
                ASVisibilityOn(),
            ],
        ),
    ]
)
