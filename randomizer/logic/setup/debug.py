"""Debug mode setup functions."""
from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_debug_start_items(world: GameWorld) -> None:
    """Insert starting items into event script 3840 if debug mode is enabled.

    Reads items.start from debug/config.yml and adds AddToInventory commands
    for each item to E3840_STARTER_DEBUG_ITEMS, which runs at game start.
    """
    if not world.settings.debug_mode:
        return

    from randomizer.debug import load_debug_config, get_item_class
    from randomizer.data.variables.event_script_names import E3840_STARTER_DEBUG_ITEMS
    from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
        AddToInventory, Return
    )

    config = load_debug_config()
    start_items = config.get("items", {}).get("start", [])
    if not start_items:
        return

    commands = []
    for item_name in start_items:
        item_cls = get_item_class(item_name)
        if item_cls is not None:
            commands.append(AddToInventory(item_cls))

    commands.append(Return())

    script = world.event_scripts.get_script_by_id(E3840_STARTER_DEBUG_ITEMS)
    script.set_contents(commands)
