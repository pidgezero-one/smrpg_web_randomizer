# pylint: disable=C0301

"""E1773_LANDS_END_BULLET_BILL_BACKGROUND"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        EnableControls([B]),
        SetBit(TEMP_7044_7),
        SetAsyncActionScript(MARIO, A0363_SKY_BRIDGE_HIT_BY_BULLET_BILL),
        EnableControls([LEFT, RIGHT, DOWN, UP, X, A, Y, B]),
        Pause(1),
        SetSyncActionScript(MARIO, A0823_PLAYER_RESET_IN_SKY_BRIDGE_ROOM),
        Return(),
    ]
)
