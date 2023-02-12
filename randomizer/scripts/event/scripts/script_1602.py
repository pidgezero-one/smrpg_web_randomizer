# E1602_EXP_STAR_SUBROUTINE_CANCEL_NPC_EVENT_DO_NOT_REMOVE_FROM_LEVEL

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7076_0, ["EVENT_1602_action_queue_sync_77"]),
        Return(),
        ActionQueueSync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPlaySound(sound=SO066_KICK_BALL_SHELL, channel=4),
                ASJumpToHeight(128),
                ASStartLoopNTimes(11),
                ASPause(4),
                ASTurnClockwise45DegreesNTimes(2),
                ASEndLoop(),
                ASSetSolidityBits(bit_4=True, cant_walk_through=True),
            ],
            identifier="EVENT_1602_action_queue_sync_77",
        ),
        EndAll(),
    ]
)
