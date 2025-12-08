# pylint: disable=C0301

"""E1591_LANDS_END_GROTTO_BARREL_KICK"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_1591_ret_5"]),
        ActionQueueSync(
            target=MARIO,
            subscript=[
                ASFloatingOff(),
                ASJumpToHeight(height=80, silent=True),
                ASSetWalkingSpeed(FAST),
                ASWalk1StepSouthwest(),
                ASSetWalkingSpeed(NORMAL),
                ASFloatingOn(),
            ]),
        ActionQueueSync(
            target=SCREEN_FOCUS,
            subscript=[
                ASSetWalkingSpeed(FAST),
                ASWalkSoutheastSteps(4),
                ASShiftSouthSteps(2),
                ASSetWalkingSpeed(NORMAL),
            ]),
        ActionQueueSync(
            target=NPC_0,
            subscript=[
                ASFaceSouthwest(),
                ASFixedFCoordOn(),
                ASPlaySound(sound=SO049_BIG_SHELL_HIT, channel=4),
                ASJumpToHeight(64),
                ASSetAllSpeeds(FAST),
                ASWalkSoutheastSteps(3),
                ASSetSolidityBits(cant_pass_walls=True),
                ASStartLoopNTimes(1),
                ASPause(
                    1, identifier="EVENT_1591_action_queue_sync_3_SUBSCRIPT_pause_8"
                ),
                ASJmpIfObjectInAir(
                    NPC_0, ["EVENT_1591_action_queue_sync_3_SUBSCRIPT_pause_8"]
                ),
                ASPlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
                ASJumpToHeight(64),
                ASWalkEastPixels(14),
                ASEndLoop(),
                ASStartLoopNTimes(2),
                ASPause(
                    1, identifier="EVENT_1591_action_queue_sync_3_SUBSCRIPT_pause_15"
                ),
                ASJmpIfObjectInAir(
                    NPC_0, ["EVENT_1591_action_queue_sync_3_SUBSCRIPT_pause_15"]
                ),
                ASPlaySound(sound=SO109_BIG_SHELL_HIT, channel=4),
                ASJumpToHeight(40),
                ASWalkEastPixels(6),
                ASEndLoop(),
            ]),
        SetBit(LANDS_END_GROTTO_BARREL_FLIPPED),
        Return(identifier="EVENT_1591_ret_5"),
    ]
)
