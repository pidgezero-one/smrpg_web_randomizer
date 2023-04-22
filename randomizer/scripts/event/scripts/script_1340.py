# pylint: disable=C0301

"""E1340_PORTRAIT_GAME_ROOM_LOCKED_DOOR"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        StoreItemAmountTo7000(ElderKey),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 1, ["EVENT_1340_apply_tile_mod_5"]),
        RunDialog(
            dialog_id=DI1945_NEED_ELDER_KEY,
            above_object=Bowser,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False,
        ),
        Return(),
        Pause(5),
        PlaySound(sound=SO016_OPEN_DOOR, channel=6),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=33,
            identifier="EVENT_1340_apply_tile_mod_5",
        ),
        ApplySolidityModToLevel(
            permanent=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=1,
        ),
        RemoveObjectFromCurrentLevel(NPC_14),
        RemoveObjectFromSpecificLevel(
            NPC_14, R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM
        ),
        RemoveOneOfItemFromInventory(ElderKey),
        Return(),
    ]
)
