# E3318_SET_OERLIKON_PACK

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_3318_set_7000_to_current_level_2"]),
        JmpToEvent(E0255_EXP_STAR_HIT),
        Set7000ToCurrentLevel(identifier="EVENT_3318_set_7000_to_current_level_2"),
        JmpIfVarEqualsConst(PRIMARY_TEMP_7000, 362, ["EVENT_3318_start_battle_6"]),
        StartBattleAtBattlefield(104, BF20_BARREL_VOLCANO),
        Jmp(["EVENT_3318_jmp_if_bit_set_7"]),
        StartBattleAtBattlefield(
            105, BF20_BARREL_VOLCANO, identifier="EVENT_3318_start_battle_6"
        ),
        JmpIfBitSet(
            RUN_AWAY,
            ["EVENT_3319_set_temp_action_script_sync_14"],
            identifier="EVENT_3318_jmp_if_bit_set_7",
        ),
        JmpIfBitSet(GAME_OVER, ["EVENT_3319_reset_and_choose_game_17"]),
        PauseActionScript(MEM_70A8),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASVisibilityOff(),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASPause(1),
            ],
        ),
        CopyVarToVar(from_var=ACTIVE_NPC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 7),
        ClearMem704XAt7000Bit(),
        FadeInFromBlack(sync=False),
        Return(),
    ]
)
