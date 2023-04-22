# pylint: disable=C0301

"""E1333_PORTRAIT_GAME_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7043_4, ["EVENT_1333_ret_17"]),
        JmpIfVarEqualsConst(SECONDARY_TEMP_7024, 4, ["EVENT_1333_apply_tile_mod_10"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=39,
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=41,
        ),
        PlaySound(sound=SO088_WRONG_SIGNAL, channel=6),
        Pause(30),
        StartBattleAtBattlefield(46, BF12_BOOSTER_TOWER),
        FadeInFromBlack(sync=False),
        Jmp(["EVENT_1338_pause_0"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=39,
            identifier="EVENT_1333_apply_tile_mod_10",
        ),
        Pause(5),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R195_BOOSTER_TOWER_6F_AREA_02_BOOSTERS_ANCESTOR_GAME_ROOM,
            mod_id=40,
        ),
        PlaySound(sound=SO087_CORRECT_SIGNAL, channel=6),
        Pause(10),
        Inc(SECONDARY_TEMP_7024),
        SetBit(TEMP_7043_4),
        Return(identifier="EVENT_1333_ret_17"),
    ]
)
