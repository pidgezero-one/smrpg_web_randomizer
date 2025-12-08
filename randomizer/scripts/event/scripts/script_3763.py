# pylint: disable=C0301

"""E3763_NIMBUS_BACK_EXIT_MARIO_FALL_ANIMATION"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControlsUntilReturn([]),
        ActionQueueAsync(
            target=MARIO,
            subscript=[
                ASDb(bytearray(b"\xc8\x00")),
                ASAddConstToVar(Z_COORD_2, 2304),
                ASDb(bytearray(b"\x99")),
                ASJumpToHeight(height=0, silent=True),
            ]),
        FadeInFromBlack(sync=True),
        Pause(1, identifier="EVENT_3763_pause_3"),
        JmpIfMarioInAir(["EVENT_3763_pause_3"]),
        SetSyncActionScript(NPC_0, A0976_CLOUD_LANDING_BLUE_PUFF_SPAWNER),
        Pause(4),
        Return(),
    ]
)
