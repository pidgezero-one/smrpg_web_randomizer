# pylint: disable=C0301

"""E1819_SHY_AWAY_EARLY_LANDS_END"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_0, ["EVENT_1819_ret_13"]),
        SetBit(TEMP_7043_0),
        Pause(1, identifier="EVENT_1819_pause_2"),
        JmpIfMarioInAir(["EVENT_1819_pause_2"]),
        JmpIfBitSet(LANDS_END_GROTTO_BARREL_FLIPPED, ["EVENT_1819_ret_13"]),
        Set7000ToObjectCoord(target_npc=MARIO, coord=COORD_Y, pixel=True, bit_7=True),
        CompareVarToConst(PRIMARY_TEMP_7000, 48),
        JmpIfComparisonResultIsGreaterOrEqual(["EVENT_1819_ret_13"]),
        ResetCoords(NPC_3),
        SetAsyncActionScript(NPC_3, A0160_SEQUENCE_LOOPING_ON),
        ActionQueueAsync(
            target=NPC_3,
            subscript=[
                ASSetAllSpeeds(FAST),
                ASWalkToXYCoords(x=28, y=37),
                ASFaceSoutheast(),
            ]),
        RunDialog(
            dialog_id=DI1277_DEAD_END_SHY_AWAY,
            above_object=MARIO,
            closable=True,
            sync=False,
            multiline=True,
            use_background=False),
        SetSyncActionScript(NPC_3, A0714_LANDS_END_SLOW_RANDOM_MOVING_ENEMIES),
        Return(identifier="EVENT_1819_ret_13"),
    ]
)
