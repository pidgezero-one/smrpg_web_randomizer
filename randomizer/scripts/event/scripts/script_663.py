# pylint: disable=C0301

"""E0663_INITIATE_MARRYMORE_BOSS_FIGHT_IF_ALL_GEAR_COLLECTED"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        ClearBit(TEMP_7042_0),
        ClearBit(TEMP_7042_1),
        ClearBit(TEMP_7042_2),
        CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 4, ["EVENT_663_adjust_music_tempo_12"]),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        SetVarToConst(PRIMARY_TEMP_7000, 4),
        DecVarFrom7000(SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=SECONDARY_TEMP_7024),
        CopyVarToVar(from_var=WEDDING_GEAR_COUNTER, to_var=PRIMARY_TEMP_7000),
        RunDialog(
            dialog_id=DI2503_NEED_X_MORE_ITEMS_MARRYMORE,
            above_object=MEM_70A8,
            closable=True,
            sync=False,
            multiline=True,
            use_background=True,
        ),
        Return(),
        SlowDownMusicTempoBy(
            duration=0, change=0, identifier="EVENT_663_adjust_music_tempo_12"
        ),
        StopBackgroundEvent(TIMER_701C),
        StopBackgroundEvent(TIMER_701E),
        ActionQueueSync(
            target=NPC_0, subscript=[ASTransferToXYZF(x=23, y=117, z=0, direction=EAST)]
        ),
        ActionQueueSync(
            target=NPC_1, subscript=[ASTransferToXYZF(x=23, y=117, z=0, direction=EAST)]
        ),
        ActionQueueAsync(
            target=NPC_2, subscript=[ASTransferToXYZF(x=23, y=117, z=0, direction=EAST)]
        ),
        JmpToEvent(E0668_SUMMON_MARRYMORE_BOSS_TO_ROOM),
    ]
)
