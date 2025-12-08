# pylint: disable=C0301

"""E0607_LOCKED_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        Set7000ToCurrentLevel(),
        JmpIfVarEqualsConst(
            PRIMARY_TEMP_7000, 409, ["EVENT_607_store_item_amount_7000_4"]
        ),
        RunDialog(
            dialog_id=DI2811_ITS_LOCKED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        Return(),
        StoreItemAmountTo7000(
            CastleKey2, identifier="EVENT_607_store_item_amount_7000_4"
        ),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_607_play_sound_8"]),
        RunDialog(
            dialog_id=DI2811_ITS_LOCKED,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        Return(),
        PlaySound(
            sound=SO005_BLOCK_SWITCH, channel=6, identifier="EVENT_607_play_sound_8"
        ),
        Pause(8),
        PlaySound(sound=SO005_BLOCK_SWITCH, channel=6),
        Pause(8),
        ApplySolidityModToLevel(
            permanent=True, room_id=R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM, mod_id=1
        ),
        RemoveObjectFromCurrentLevel(NPC_6),
        RemoveObjectFromCurrentLevel(NPC_7),
        RemoveObjectFromSpecificLevel(NPC_6, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_7, R409_NIMBUS_CASTLE_AREA_09_BIRDOS_ROOM),
        RemoveOneOfItemFromInventory(CastleKey2),
        Return(),
    ]
)
