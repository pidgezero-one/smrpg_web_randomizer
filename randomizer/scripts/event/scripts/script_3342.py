# pylint: disable=C0301

"""E3342_VOLCANO_5TH_BOSS_PATH_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(
            VOLCANO_STAIRCASE_ANIMATION_COMPLETED,
            ["EVENT_3342_run_event_as_subroutine_2"]),
        ActionQueueSync(
            target=NPC_2, subscript=[ASTransferXYZFSteps(x=0, y=0, z=8, direction=EAST)]
        ),
        RunEventAsSubroutine(
            E0843_VOLCANO_POST_BOSS_ROOM_WITH_ENEMY_WARPS_SHUFFLED_NPC_ANIMATION_LOADER
        ),
        RunEventAsSubroutine(
            E0015_STANDARD_ROOM_LOADER,
            identifier="EVENT_3342_run_event_as_subroutine_2"),
        JmpIfBitSet(VOLCANO_STAIRCASE_ANIMATION_COMPLETED, ["EVENT_3342_ret_5"]),
        RunBackgroundEvent(
            event_id=E3345_VOLCANO_CHASE_SEQEUNCE, return_on_level_exit=True
        ),
        Return(identifier="EVENT_3342_ret_5"),
    ]
)
