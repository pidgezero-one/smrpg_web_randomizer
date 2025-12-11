# pylint: disable=C0301

"""E0621_MARRYMORE_INN_ELDERLY_GUEST"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 12, ["EVENT_621_jmp_if_bit_set_86"]),
        JmpIfBitSet(GUEST_DROPPED_OFF, ["EVENT_621_jmp_if_bit_set_109"]),
        Pause(10),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASClearSolidityBits(cant_pass_walls=True),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkToXYCoords(x=6, y=62),
                ASFaceNorthwest(),
            ]),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_10"]),
        SetVarToConst(TEMP_70A9, 27),
        Jmp(["EVENT_621_action_queue_sync_11"]),
        SetVarToConst(TEMP_70A9, 26, identifier="EVENT_621_set_10"),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASPause(30),
                ASFaceSoutheast(),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkSoutheastSteps(2),
            ],
            identifier="EVENT_621_action_queue_sync_11"),
        Pause(30),
        PlaySound(sound=SO004_JUMP, channel=6),
        SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASWalkNortheastSteps(3),
            ]),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[ASWalkSoutheastSteps(2), ASWalkNortheastSteps(2)]),
        Pause(30),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R006_MARRYMORE_INN_2F,
            face_direction=NORTHEAST,
            x=15,
            y=52,
            z=1,
            z_add_half_unit=True),
        FadeInFromBlack(sync=True),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_25"]),
        SetVarToConst(TEMP_70A9, 22),
        Jmp(["EVENT_621_pause_26"]),
        SetVarToConst(TEMP_70A9, 21, identifier="EVENT_621_set_25"),
        Pause(1, identifier="EVENT_621_pause_26"),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalk1StepNortheast(),
                ASWalkNorthwestSteps(4),
                ASFaceSoutheast(),
            ]),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASPause(30),
                ASFaceNortheast(),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASTransferToXYZF(x=15, y=52, z=3, direction=EAST),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalk1StepNortheast(),
                ASWalkNorthwestSteps(2),
            ]),
        RememberLastObject(),
        ActionQueueSync(
            target=MARIO, subscript=[ASWalkNorthwestSteps(3), ASWalkNortheastSteps(3)]
        ),
        ActionQueueSync(target=MEM_70A9, subscript=[ASWalkNorthwestSteps(4)]),
        Pause(50),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R011_MARRYMORE_INN_3F,
            face_direction=NORTHEAST,
            x=12,
            y=73,
            z=1,
            z_add_half_unit=True),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_39"]),
        SetVarToConst(TEMP_70A9, 25),
        Jmp(["EVENT_621_pause_40"]),
        SetVarToConst(TEMP_70A9, 24, identifier="EVENT_621_set_39"),
        Pause(1, identifier="EVENT_621_pause_40"),
        FadeInFromBlack(sync=True),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkNortheastSteps(1),
                ASWalkSoutheastSteps(2),
                ASWalkSoutheastPixels(8),
                ASWalkNortheastSteps(3),
                ASPause(30),
                ASFaceSouthwest(),
                ASPause(30),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkNortheastSteps(2),
            ]),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASPause(30),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASFaceNortheast(),
                ASTransferToXYZF(x=12, y=73, z=3, direction=EAST),
                ASSetWalkingSpeed(NORMAL),
                ASSetSequenceSpeed(FAST),
                ASWalkNortheastSteps(1),
                ASWalkSoutheastSteps(2),
                ASWalkSoutheastPixels(8),
                ASWalkNortheastSteps(2),
            ]),
        Pause(52),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True, room_id=R011_MARRYMORE_INN_3F, mod_id=0
        ),
        ApplySolidityModToLevel(
            permanent=True, room_id=R011_MARRYMORE_INN_3F, mod_id=1
        ),
        Pause(70),
        FadeOutToBlack(sync=False),
        EnterArea(
            room_id=R012_MARRYMORE_INN_SUITE_ROOM,
            face_direction=NORTHEAST,
            x=3,
            y=21,
            z=0),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASTransferXYZFPixels(x=0, y=248, z=0, direction=EAST),
                ASSetSpriteSequence(index=0, is_sequence=True, looping=True),
            ]),
        SetBit(TEMP_7044_5),
        CopyVarToVar(from_var=TEMP_70B8, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 3, ["EVENT_621_set_57"]),
        SetVarToConst(TEMP_70A9, 22),
        Jmp(["EVENT_621_fade_in_from_black_sync_58"]),
        SetVarToConst(TEMP_70A9, 21, identifier="EVENT_621_set_57"),
        FadeInFromBlack(sync=True, identifier="EVENT_621_fade_in_from_black_sync_58"),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetSequenceSpeed(FAST),
                ASWalkNortheastSteps(2),
                ASFaceSouthwest(),
            ]),
        ActionQueueSync(
            target=MEM_70A9,
            subscript=[
                ASPause(30),
                ASFaceNortheast(),
                ASTransferToXYZF(x=3, y=22, z=0, direction=EAST),
                ASSetWalkingSpeed(SLOW),
                ASWalkNortheastSteps(2),
            ]),
        RememberLastObject(),
        FreezeCamera(),
        Pause(30),
        PlaySound(sound=SO004_JUMP, channel=6),
        SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASSetWalkingSpeed(VERY_FAST),
                ASSetSequenceSpeed(VERY_FAST),
                ASWalkNorthwestSteps(3),
                ASFaceSouth(),
            ]),
        ActionQueueSync(target=MEM_70A9, subscript=[ASPause(20), ASFaceNorthwest()]),
        RememberLastObject(),
        PlaySound(sound=SO004_JUMP, channel=6),
        SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
        PlaySound(sound=SO004_JUMP, channel=6),
        SetAsyncActionScript(MARIO, A0636_54_VELOCITY_SINGLE_JUMP),
        ActionQueueSync(
            target=MARIO, subscript=[ASWalk1StepSoutheast(), ASWalkEastSteps(7)]
        ),
        ActionQueueSync(target=MEM_70A9, subscript=[ASPause(30), ASFaceNortheast()]),
        RememberLastObject(),
        Pause(30),
        PlaySound(sound=SO004_JUMP, channel=6),
        Pause(30),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASWalkWestSteps(5),
                ASWalkSouthwestSteps(2),
                ASPause(30),
                ASSetSpriteSequence(index=6, is_sequence=True, looping=True),
                ASPause(12),
            ]),
        SetAsyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        Pause(30),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouth()]),
        SetBit(GUEST_DROPPED_OFF),
        UnfreezeCamera(),
        Return(),
        JmpIfBitSet(
            TEMP_7044_2,
            ["EVENT_621_run_dialog_107"],
            identifier="EVENT_621_jmp_if_bit_set_86"),
        SetBit(TEMP_7044_2),
        RunEventAsSubroutine(E0622_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_1),
        Return(),
        RunDialog(
            dialog_id=DI1016_THANKS_A_LOT,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_621_run_dialog_107"),
        Return(),
        JmpIfBitSet(
            MARRYMORE_MAJOR_TIP_GIVEN,
            ["EVENT_621_major_tip_already_given"],
            identifier="EVENT_621_jmp_if_bit_set_109"),
        RunEventAsSubroutine(E0212_NPC_QUEST_7_CONTAINER),
        SetBit(MARRYMORE_MAJOR_TIP_GIVEN),
		Return(),
        JmpIfBitSet(
            TEMP_7044_1,
            ["EVENT_621_run_dialog_122"],
            identifier="EVENT_621_major_tip_already_given"),
        SetBit(TEMP_7044_1),
        RunEventAsSubroutine(E0626_MARRYMORE_INN_ELDERLY_GUEST_TIP_SUBROUTINE_FLOWERBOX),
        Return(),
        RunDialog(
            dialog_id=DI2048_HOTEL_GUEST_LEAVING,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
            identifier="EVENT_621_run_dialog_122"),
        Return(),
    ]
)
