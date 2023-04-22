# pylint: disable=C0301

"""E1693_TEMPLE_FINAL_FORTUNE_HEAD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitSet(TEMP_7044_0, ["EVENT_1693_ret_21"]),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(bits=[], destinations=["EVENT_1693_ret_21"]),
        ActionQueueSync(
            target=MARIO, subscript=[ASJumpToHeight(height=64, silent=True)]
        ),
        PlaySound(sound=SO154_BIG_SQUISH, channel=6),
        Pause(2),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R423_BELOME_TEMPLE_AREA_06_BELOMES_FORTUNE_ROOM_WELEVATING_PLATFORM,
            mod_id=32,
        ),
        Store00To0248(),
        Pause(1),
        Inc(UNKNOWN_70AD),
        CopyVarToVar(from_var=UNKNOWN_70AD, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 5),
        SetVarToRandom(TEMP_702A, 20),
        Compare7000ToVar(TEMP_702A),
        JmpIfComparisonResultIsLesser(["EVENT_1693_clear_bit_18"]),
        SetBit(TEMPLE_BOSS_ACCESS_FORTUNE),
        Jmp(["EVENT_1693_set_bit_19"]),
        ClearBit(TEMPLE_BOSS_ACCESS_FORTUNE, identifier="EVENT_1693_clear_bit_18"),
        SetBit(TEMP_7044_0, identifier="EVENT_1693_set_bit_19"),
        ActionQueueAsync(
            target=NPC_1,
            subscript=[
                ASIncPaletteRowBy(1),
                ASFloatingOff(),
                ASClearSolidityBits(cant_pass_walls=True),
                ASSetWalkingSpeed(VERY_FAST),
                ASWalkSoutheastPixels(4),
                ASJumpToHeight(64),
                ASSetSpriteSequence(
                    index=1, is_sequence=True, looping=True, mirror_sprite=True
                ),
                ASVisibilityOn(),
                ASSetWalkingSpeed(FAST),
                ASWalkSoutheastSteps(2),
                ASSetSolidityBits(cant_pass_walls=True),
            ],
        ),
        Return(identifier="EVENT_1693_ret_21"),
    ]
)
