# pylint: disable=C0301

"""E0337_MUSHROOM_KINGDOM_SHOP_BOOKSHELF"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_256_ret_0"]),
        SetBit(TEMP_7043_0),
        SetVarToConst(TEMP_70A9, 0),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASResetProperties(),
                ASStartLoopNTimes(9),
                ASTurnClockwise45DegreesNTimes(1),
                ASPause(2),
                ASEndLoop(),
                ASSetSequenceSpeed(NORMAL),
                ASSetSpriteSequence(
                    index=10, sprite_offset=2, is_sequence=True, looping=False
                ),
                ASPause(30),
                ASSetSequenceSpeed(VERY_SLOW),
                ASPause(40),
                ASFaceSouth(),
                ASResetProperties(),
            ],
        ),
        Pause(30),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFaceSouthwest(),
                ASPause(20),
                ASSetSpriteSequence(
                    index=0, sprite_offset=3, is_sequence=True, looping=True
                ),
                ASJumpToHeight(height=64, silent=True),
            ],
        ),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASFaceNortheast(),
                ASSetWalkingSpeed(VERY_FAST),
                ASAddZCoord1Step(),
                ASDecZCoord1Step(),
                ASSetWalkingSpeed(NORMAL),
            ],
        ),
        RunDialog(
            dialog_id=DI0608_SHOPKEEPER_YELLS_AT_YOU_ON_SHELF,
            above_object=NPC_14,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False,
        ),
        RememberLastObject(),
        ActionQueueAsync(
            target=MARIO,
            subscript=[ASResetProperties(), ASJumpToHeight(64), ASWalk1StepSouthwest()],
        ),
        RunEventAsSubroutine(E0278_UNKNOWN),
        ActionQueueAsync(target=NPC_1, subscript=[ASFaceSouthwest()]),
        SetSyncActionScript(MARIO, A0395_PLAYER_RESET_PROPERTIES_AND_SOLIDITY),
        UnsyncActionScript(MARIO),
        Return(),
    ]
)
