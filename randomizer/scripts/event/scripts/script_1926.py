# pylint: disable=C0301

"""E1926_TOWER_BALCONY_LOADER"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TOWER_BOSS_2_DEFEATED, ["EVENT_1926_jmp_if_bit_clear_73"]),
        RunEventAsSubroutine(E0354_BOSS_BATTLE_CONTAINER),
        JmpIfBitClear(GAME_OVER, ["EVENT_1926_fade_out_music_to_volume_49"]),
        ResetAndChooseGame(),
        FadeOutMusicToVolume(
            duration=0, volume=0, identifier="EVENT_1926_fade_out_music_to_volume_49"
        ),
        SummonObjectToSpecificLevel(NPC_0, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        SummonObjectToSpecificLevel(NPC_1, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        SummonObjectToSpecificLevel(NPC_2, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_3, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_4, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_5, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        RemoveObjectFromSpecificLevel(NPC_6, R039_BOOSTER_TOWER_5F_KNIFE_GUYS_ROOM),
        SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT),
        SetBit(UNKNOWN_TOWER_BOSS_2_FIGHT_7089_2),
        EnterArea(
            room_id=R202_BOOSTER_TOWER_ENTRANCE,
            face_direction=SOUTHWEST,
            x=5,
            y=114,
            z=15),
        RestoreAllHP(),
        RestoreAllFP(),
        SetBit(TOWER_BOSS_2_DEFEATED),
        RunEventAsSubroutine(E0205_UNLOCK_MARRYMORE_IF_GATED_BY_TOWER_BOSS),
        SetBit(GAMEBOY_KID_PURCHASE_COMPLETE),
        JmpToEvent(E1328_TOWER_EXTERIOR_LOADER),
        Return(),
        JmpIfBitClear(
            MARRYMORE_LIBERATED,
            ["EVENT_1926_balcony_empty"],
            identifier="EVENT_1926_jmp_if_bit_clear_73"),
        JmpToEvent(E1282_TOWER_BALCONY_LOADER_AFTER_MARRYMORE),
        JmpToEvent(
            E1283_TOWER_BALCONY_LOADER_BEFORE_MARRYMORE,
            identifier="EVENT_1926_balcony_empty"),
    ]
)
