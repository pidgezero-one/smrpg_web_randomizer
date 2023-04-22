# pylint: disable=C0301

"""E2208_KEEP_1ST_BOSS_ROOM_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(KEEP_BOSS_1_DEFEATED, ["EVENT_2208_set_action_script_sync_10"]),
        RunEventAsSubroutine(E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_2209_pause_0"]),
        Return(),
        SetSyncActionScript(
            NPC_0,
            A0014_FLOATING_CHEST,
            identifier="EVENT_2208_set_action_script_sync_10",
        ),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASShiftToXYCoords(x=24, y=98),
                ASVisibilityOn(),
                ASFaceSoutheast(),
                ASSequenceLoopingOn(),
            ],
        ),
        ActionQueueAsync(
            target=NPC_0,
            subscript=[
                ASTransferToXYZF(x=27, y=104, z=7, direction=EAST),
                ASVisibilityOn(),
            ],
        ),
        RunEventAsSubroutine(E0847_KEEP_FIRST_BOSS_ROOM_SHUFFLED_NPC_ANIMATION_LOADER),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
