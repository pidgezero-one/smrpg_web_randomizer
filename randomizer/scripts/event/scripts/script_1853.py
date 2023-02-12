# E1853_SKY_BRIDGE_RIDE_SHAMAN

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AE),
        JmpIfMarioOnAnObjectOrNot(
            ["EVENT_1853_stop_all_background_events_5", "EVENT_1853_run_dialog_3"]
        ),
        RunDialog(
            dialog_id=DI1313_ELEVATOR_SHAMAN,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_1853_run_dialog_3",
        ),
        Return(),
        StopAllBackgroundEvents(identifier="EVENT_1853_stop_all_background_events_5"),
        ClearBit(TEMP_7043_0),
        ClearBit(TEMP_7044_3),
        ClearBit(TEMP_7043_2),
        SetBit(SKY_BRIDGE_COURSE_CHOICE),
        SetBit(SKY_BRIDGE_COURSE_1_CHOSEN),
        SetVarToConst(TEMP_702E, 48),
        SetVarToConst(TEMP_702C, 70),
        ActionQueueSync(
            target=NPC_17,
            subscript=[ASTransferToXYZF(x=20, y=104, z=18, direction=EAST)],
        ),
        Db(bytearray(b"\xc7\x90")),
        ActionQueueAsync(
            target=MARIO, subscript=[ASFloatingOff(), ASRunAwayShift(), ASFloatingOn()]
        ),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASFaceNorthwest(),
                ASShiftZUpSteps(10),
                ASShiftNorthSteps(3),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPlaySound(sound=SO161_GHOST, channel=4),
                ASJumpToHeight(128),
                ASStartLoopNTimes(4),
                ASVisibilityOff(),
                ASPause(1),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASSetSolidityBits(bit_4=True, cant_walk_through=True),
                ASTransferToXYZF(x=20, y=112, z=0, direction=EAST),
                ASFaceSouthwest(),
            ],
        ),
        Return(),
    ]
)
