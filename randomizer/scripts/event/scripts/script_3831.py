# pylint: disable=C0301

"""E3831_MUSHROOM_KINGDOM_SHOP_CELLAR_MOD"""

from randomizer.scripts.event.script_imports import *

script = EventScript(
    [
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_0,
            R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
            ["EVENT_3831_apply_tile_mod_32"],
        ),
        JmpIfObjectTriggerDisabledInSpecificLevel(
            NPC_1,
            R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
            ["EVENT_3831_apply_tile_mod_41"],
            identifier="EVENT_3831_jmp_if_object_trigger_disabled_6",
        ),
        FadeInFromBlack(
            sync=False, identifier="EVENT_3831_fade_in_from_black_async_12"
        ),
        Return(),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
            mod_id=0,
            identifier="EVENT_3831_apply_tile_mod_32",
        ),
        Jmp(["EVENT_3831_jmp_if_object_trigger_disabled_6"]),
        ApplyTileModToLevel(
            use_alternate=True,
            room_id=R492_MUSHROOM_KINGDOM_ITEM_SHOP_BASEMENT,
            mod_id=1,
            identifier="EVENT_3831_apply_tile_mod_41",
        ),
        Jmp(["EVENT_3831_fade_in_from_black_async_12"]),
    ]
)
