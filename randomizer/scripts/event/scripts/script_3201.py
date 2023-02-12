# E3201_MINES_1ST_BOSS_FIGHT

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(MINES_BOSS_1_DEFEATED, ["EVENT_3201_set_short_364"]),
        SetBit(TEMP_7043_0),
        SetVarToConst(PRIMARY_TEMP_7000, 518),
        RunEventAsSubroutine(E0353_BOSS_BATTLE),
        JmpIfBitSet(GAME_OVER, ["EVENT_3201_reset_and_choose_game_366"]),
        SetBit(MINES_BOSS_1_DEFEATED),
        RestoreAllHP(),
        RestoreAllFP(),
        FadeInFromBlack(sync=False),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    cant_pass_walls=True,
                    bit_4=True,
                    cant_pass_npcs=True,
                    cant_walk_through=True,
                    bit_7=True,
                ),
                ASSetAllSpeeds(VERY_FAST),
                ASSequenceLoopingOn(),
                ASJumpToHeight(56),
                ASPause(32),
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASPlaySound(sound=SO011_WHOOSH_AWAY, channel=4),
                ASReturn(),
            ],
        ),
        ResumeActionScript(MEM_70A8),
        Set7000ToCurrentLevel(),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000, 277, ["EVENT_3201_jmp_if_7000_not_equals_short_20"]
        ),
        JmpIfBitSet(MINES_HENCHMAN_LEFT_DEFEATED, ["EVENT_3201_set_short_364"]),
        ActionQueueSync(
            target=NPC_1,
            subscript=[
                ASSetBit(TEMP_7043_1),
                ASJmp(
                    ["EVENT_3192_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0"]
                ),
            ],
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            283,
            ["EVENT_3201_jmp_if_7000_not_equals_short_23"],
            identifier="EVENT_3201_jmp_if_7000_not_equals_short_20",
        ),
        JmpIfBitSet(MINES_HENCHMAN_RIGHT_DEFEATED, ["EVENT_3201_set_short_364"]),
        ActionQueueSync(
            target=NPC_2,
            subscript=[
                ASSetBit(TEMP_7043_1),
                ASJmp(
                    ["EVENT_3193_action_queue_sync_4_SUBSCRIPT_object_memory_set_bit_0"]
                ),
            ],
        ),
        JmpIfVarNotEqualsConst(
            PRIMARY_TEMP_7000,
            273,
            ["EVENT_3201_set_short_364"],
            identifier="EVENT_3201_jmp_if_7000_not_equals_short_23",
        ),
        JmpIfBitSet(MINES_HENCHMAN_MIDDLE_DEFEATED, ["EVENT_3201_set_short_364"]),
        ActionQueueSync(
            target=NPC_3,
            subscript=[
                ASSetBit(TEMP_7043_1),
                ASJmp(["EVENT_3194_action_queue_sync_4_SUBSCRIPT_pause_0"]),
            ],
        ),
        SetVarToConst(PRIMARY_TEMP_7000, 518, identifier="EVENT_3201_set_short_364"),
        ClearBit(TEMP_7043_0),
        RunEventAsSubroutine(E0253_NPC_QUEST_1_GRANT),
        SetVarToConst(PRIMARY_TEMP_7000, 518),
        JmpToEvent(E0167_BOSS_GRANT_STAR_PIECE),
        Return(),
        ResetAndChooseGame(identifier="EVENT_3201_reset_and_choose_game_366"),
    ]
)
