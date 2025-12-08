# pylint: disable=C0301

"""E2670_TOWER_KNIFE_GUY_CONSOLATION_PRIZE"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        SetVarToRandom(PRIMARY_TEMP_7000, 21),
        CompareVarToConst(PRIMARY_TEMP_7000, 3),
        JmpIfComparisonResultIsLesser(["EVENT_2670_jmp_if_bit_set_124"]),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_set_100"]),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_set_102"]),
        SetVarToConst(ITEM_ID, WiltShroom),
        Jmp(["EVENT_2670_play_sound_104"]),
        SetVarToConst(ITEM_ID, RottenMush, identifier="EVENT_2670_set_100"),
        Jmp(["EVENT_2670_play_sound_104"]),
        SetVarToConst(ITEM_ID, MoldyMush, identifier="EVENT_2670_set_102"),
        Jmp(["EVENT_2670_play_sound_104"]),
        PlaySound(
            sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2670_play_sound_104"
        ),
        RunDialog(
            dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_put_inventory_110"]),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_put_inventory_112"]),
        AddToInventory(WiltShroom),
        Return(),
        AddToInventory(RottenMush, identifier="EVENT_2670_put_inventory_110"),
        Return(),
        AddToInventory(MoldyMush, identifier="EVENT_2670_put_inventory_112"),
        Return(),
        PlaySound(
            sound=SO027_FOUND_AN_ITEM, channel=6, identifier="EVENT_2670_play_sound_114"
        ),
        RunDialog(
            dialog_id=DI0524_GOT_A_70A7_AWAIT_TERMINATE,
            above_object=BOWSER,
            closable=True,
            sync=False,
            multiline=False,
            use_background=False),
        JmpIfBitSet(TEMP_7043_7, ["EVENT_2670_put_inventory_120"]),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_put_inventory_122"]),
        AddToInventory(Mushroom),
        Return(),
        AddToInventory(MidMushroom, identifier="EVENT_2670_put_inventory_120"),
        Return(),
        AddToInventory(MaxMushroom, identifier="EVENT_2670_put_inventory_122"),
        Return(),
        JmpIfBitSet(
            TEMP_7043_7,
            ["EVENT_2670_set_128"],
            identifier="EVENT_2670_jmp_if_bit_set_124"),
        JmpIfBitSet(TEMP_7044_0, ["EVENT_2670_set_130"]),
        SetVarToConst(ITEM_ID, Mushroom),
        Jmp(["EVENT_2670_play_sound_114"]),
        SetVarToConst(ITEM_ID, MidMushroom, identifier="EVENT_2670_set_128"),
        Jmp(["EVENT_2670_play_sound_114"]),
        SetVarToConst(ITEM_ID, MaxMushroom, identifier="EVENT_2670_set_130"),
        Jmp(["EVENT_2670_play_sound_114"]),
    ]
)
