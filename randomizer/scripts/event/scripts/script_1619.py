# pylint: disable=C0301

"""E1619_OCCUPIED_MOLEVILLE_EXTERIOR_NPC_TRIGGER_CUTSCENE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        PauseActionScript(NPC_0),
        RunDialog(
            dialog_id=DI1095_MOLEVILLE_NPC_BEFORE_CLEAR,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(MOLEVILLE_MINES_ENTRANCE_GATING, ["EVENT_1619_jmp_if_bit_set_2"]),
        RunDialog(
            dialog_id=DI1051_MOLEVILLE_CLOSED,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        JmpIfBitSet(
            MOLE_DESCENDED,
            ["EVENT_1619_resume_action_script_15"],
            identifier="EVENT_1619_jmp_if_bit_set_2",
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASPause(30),
                ASSetSolidityBits(cant_pass_walls=True),
                ASFloatingOn(),
                ASSetAllSpeeds(NORMAL),
                ASStartLoopNTimes(1),
                ASFixedFCoordOn(),
                ASWalk1StepSouthwest(),
                ASPause(16),
                ASFixedFCoordOff(),
                ASWalk1StepSouthwest(),
                ASPause(10),
                ASFaceNortheast(),
                ASEndLoop(),
            ],
        ),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASBounceToXYWithHeight(x=14, y=27, height=0),
            ],
        ),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASWalkEastSteps(2),
                ASFaceSoutheast(),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
            ],
        ),
        ActionQueueAsync(target=MARIO, subscript=[ASFaceSouthwest7D()]),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASSetSolidityBits(cant_pass_walls=True),
                ASSetSequenceSpeed(FAST),
                ASStartLoopNTimes(3),
                ASJumpToHeight(48),
                ASPause(20),
                ASEndLoop(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        RunDialog(
            dialog_id=DI1098_MOLEVILLE_CUTSCENE,
            above_object=NPC_12,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalk1StepNortheast(),
                ASFaceNorthwest(),
                ASStartLoopNTimes(3),
                ASJumpToHeight(48),
                ASPause(20),
                ASEndLoop(),
                ASClearSolidityBits(cant_pass_walls=True),
            ],
        ),
        RunDialog(
            dialog_id=DI1099_MOLEVILLE_CUTSCENE,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        StartSyncEmbeddedActionScript(
            target=NPC_0,
            prefix=0xF1,
            subscript=[
                ASFaceNortheast(),
                ASSetAllSpeeds(NORMAL),
                ASSequenceLoopingOn(),
            ],
        ),
        StartAsyncEmbeddedActionScript(
            target=NPC_1,
            prefix=0xF1,
            subscript=[
                ASFaceNortheast(),
                ASSetAllSpeeds(NORMAL),
                ASSequenceLoopingOn(),
            ],
        ),
        SetSyncActionScript(NPC_1, A0648_MOLEVILLE_WOMAN_NEAR_MOUNTAIN),
        SetBit(MOLE_DESCENDED),
        ResumeActionScript(NPC_0, identifier="EVENT_1619_resume_action_script_15"),
        Return(),
    ]
)
