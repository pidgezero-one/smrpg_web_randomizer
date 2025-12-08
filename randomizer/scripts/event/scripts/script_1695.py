# pylint: disable=C0301

"""E1695_BANDITS_WAY_GOOMBA"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(TEMP_7076_0, ["EVENT_1695_set_short_2"]),
        JmpToEvent(E0255_EXP_STAR_HIT),
        SetVarToConst(BATTLE_PACK_ID, 7, identifier="EVENT_1695_set_short_2"),
        StartBattleWithPackAt700E(),
        JmpIfBitSet(RUN_AWAY, ["EVENT_1695_fade_in_from_black_sync_9"]),
        JmpIfBitSet(GAME_OVER, ["EVENT_1695_reset_and_choose_game_12"]),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASObjectMemorySetBit(arg_1=0x30, bits=[4]),
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASVisibilityOff(),
            ]),
        FadeInFromBlack(sync=False),
        Return(),
        FadeInFromBlack(sync=True, identifier="EVENT_1695_fade_in_from_black_sync_9"),
        ActionQueueAsync(
            target=MEM_70A8,
            subscript=[
                ASClearSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASSetAllSpeeds(FASTER),
                ASWalkSouthwestSteps(3),
                ASSetSolidityBits(
                    bit_4=True, cant_pass_npcs=True, cant_walk_through=True, bit_7=True
                ),
                ASVisibilityOff(),
            ]),
        Return(),
        ResetAndChooseGame(identifier="EVENT_1695_reset_and_choose_game_12"),
        Return(),
    ]
)
