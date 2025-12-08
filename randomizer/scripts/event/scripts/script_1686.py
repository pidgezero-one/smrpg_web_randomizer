# pylint: disable=C0301

"""E1686_TEMPLE_FORTUNE_HEAD_2"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfBitClear(BELOME_FORTUNE_1, ["EVENT_1686_ret_30"]),
        Set7000ToTappedButton(),
        JmpIf7000AllBitsClear(bits=[], destinations=["EVENT_1686_ret_30"]),
        ActionQueueSync(target=MARIO, subscript=[ASJumpToHeight(64)]),
        JmpIfBitSet(BELOME_HEAD_2, ["EVENT_1686_ret_30"]),
        Pause(1, identifier="EVENT_1686_pause_5"),
        JmpIfMarioInAir(["EVENT_1686_pause_5"]),
        PlaySound(sound=SO154_BIG_SQUISH, channel=6),
        Pause(2),
        Store02To0248(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM,
            mod_id=33),
        Store00To0248(),
        Pause(1),
        SetBit(BELOME_HEAD_2),
        JmpIfVarNotEqualsConst(
            SECONDARY_TEMP_7024, 0, ["EVENT_1686_jmp_if_var_not_equals_const_20"]
        ),
        SetVarToConst(SECONDARY_TEMP_7024, 2),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 32),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        Jmp(["EVENT_1685_set_7000_to_7000_short_mem_39"]),
        JmpIfVarNotEqualsConst(
            TEMP_7026,
            0,
            ["EVENT_1686_set_7000_to_70A0_short_mem_26"],
            identifier="EVENT_1686_jmp_if_var_not_equals_const_20"),
        SetVarToConst(TEMP_7026, 8),
        CopyVarToVar(from_var=TEMP_70AC, to_var=PRIMARY_TEMP_7000),
        AddConstToVar(PRIMARY_TEMP_7000, 32),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        Jmp(["EVENT_1685_set_7000_to_7000_short_mem_39"]),
        CopyVarToVar(
            from_var=TEMP_70AC,
            to_var=PRIMARY_TEMP_7000,
            identifier="EVENT_1686_set_7000_to_70A0_short_mem_26"),
        AddConstToVar(PRIMARY_TEMP_7000, 32),
        CopyVarToVar(from_var=PRIMARY_TEMP_7000, to_var=TEMP_70AC),
        Jmp(["EVENT_1685_set_29"]),
        Return(identifier="EVENT_1686_ret_30"),
    ]
)
