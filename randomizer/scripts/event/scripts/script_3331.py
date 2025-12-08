# pylint: disable=C0301

"""E3331_VOLCANO_1ST_BOSS_FIGHT"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(VOLCANO_MIDBOSS_DEFEATED, ["EVENT_3331_ret_24"]),
        Pause(700),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        SetBit(TEMP_707C_5),
        ClearBit(TEMP_707C_7),
        RunEventAsSubroutine(E0024_BATTLE_RESULT_CHECK),
        RestoreAllHP(),
        RestoreAllFP(),
        SetBit(VOLCANO_MIDBOSS_DEFEATED),
        SetSyncActionScript(NPC_1, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_2, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_3, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_4, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_5, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_6, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_7, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_8, A1023_ERUPTED_MAGMITES),
        SetSyncActionScript(NPC_9, A1023_ERUPTED_MAGMITES),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            mod_id=32),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R352_VOLCANO_AREA_21_CZAR_DRAGONS_ROOM,
            mod_id=33),
        Db(bytearray(b"\xfdD")),
        ResetPrioritySet(),
        FadeInFromBlack(sync=False),
        JmpToEvent(E0168_BOSS_GRANT_STAR_PIECE_CONTAINER),
        Return(identifier="EVENT_3331_ret_24"),
    ]
)
