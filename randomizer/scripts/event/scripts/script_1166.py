# pylint: disable=C0301

"""E1166_SHED_KEY_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(SEASIDE_BOSS_SET, ["EVENT_1166_ret_2"]),
        SetVarToConst(ITEM_ID, ShedKey),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1166_pause_3"]),
        RunDialog(
            dialog_id=DI2802_NEED_THE_SHED_KEY,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(identifier="EVENT_1166_ret_2"),
        Pause(5, identifier="EVENT_1166_pause_3"),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE,
            mod_id=0,
        ),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromSpecificLevel(
            NPC_6, R208_SEASIDE_TOWN_DURING_YARIDOVICH_OUTSIDE
        ),
        Pause(5),
        Return(),
    ]
)
