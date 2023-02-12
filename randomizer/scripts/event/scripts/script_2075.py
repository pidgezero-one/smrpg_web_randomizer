# E2075_MONSTRO_SEALED_DOOR

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToConst(ITEM_ID, ShinyStone),
        StoreItemAt70A7QuantityTo7000(),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 0, ["EVENT_2075_run_dialog_0"]),
        Pause(15),
        ApplySolidityModToLevel(
            permanent=True, room_id=R324_MONSTRO_TOWN_OUTSIDE, mod_id=0
        ),
        PlaySound(sound=SO081_STAR, channel=6),
        Pause(15),
        RemoveObjectFromCurrentLevel(NPC_2),
        RemoveObjectFromSpecificLevel(NPC_2, R324_MONSTRO_TOWN_OUTSIDE),
        Return(),
        RunDialog(
            dialog_id=DI3335_DUPLICATE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
            identifier="EVENT_2075_run_dialog_0",
        ),
        Return(),
    ]
)
