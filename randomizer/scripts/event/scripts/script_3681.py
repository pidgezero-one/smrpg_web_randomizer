# pylint: disable=C0301

"""E3681_BIRDY_BECOMES_PLATFORM"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StartBattleAtBattlefield(92, BF02_BEAN_VALLEY_BEANSTALKS),
        SetBit(TEMP_704A_2),
        RunEventAsSubroutine(E1011_POST_MINES_BOSS_CHECK_IF_WON),
        ClearBit(TEMP_704A_2),
        FadeInFromBlack(sync=False),
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 379, ["EVENT_3681_jmp_to_subroutine_8"]),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 380, ["EVENT_3681_jmp_to_subroutine_14"]
        ),
        JmpToSubroutine(
            ["EVENT_3681_action_queue_async_20"],
            identifier="EVENT_3681_jmp_to_subroutine_8",
        ),
        PlaySound(sound=SO014_FLOWER, channel=6),
        RemoveObjectFromSpecificLevel(NPC_1, R379_BEAN_VALLEY_BEANSTALKS_AREA_02),
        RemoveObjectFromCurrentLevel(NPC_1),
        SummonObjectToCurrentLevel(NPC_2),
        Return(),
        JmpToSubroutine(
            ["EVENT_3681_action_queue_async_20"],
            identifier="EVENT_3681_jmp_to_subroutine_14",
        ),
        PlaySound(sound=SO014_FLOWER, channel=6),
        RemoveObjectFromSpecificLevel(
            NPC_0, R380_BEAN_VALLEY_BEANSTALKS_AREA_03_FROM_RIGHT_BEANSTALK_OF_AREA_02
        ),
        RemoveObjectFromCurrentLevel(NPC_0),
        SummonObjectToCurrentLevel(NPC_1),
        Return(),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASStartLoopNTimes(2),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(8),
                ASEndLoop(),
                ASStartLoopNTimes(7),
                ASVisibilityOff(),
                ASPause(4),
                ASVisibilityOn(),
                ASPause(4),
                ASEndLoop(),
                ASStartLoopNTimes(7),
                ASVisibilityOff(),
                ASPause(2),
                ASVisibilityOn(),
                ASPause(2),
                ASEndLoop(),
                ASStartLoopNTimes(7),
                ASVisibilityOn(),
                ASPause(1),
                ASVisibilityOff(),
                ASPause(1),
                ASEndLoop(),
            ],
            identifier="EVENT_3681_action_queue_async_20",
        ),
        Return(),
    ]
)
