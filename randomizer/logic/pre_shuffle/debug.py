"""Debug mode setup functions."""
from __future__ import annotations
from typing import TYPE_CHECKING

from randomizer.data.variables.variable_names import PRIMARY_TEMP_7000
from randomizer.debug import load_debug_config, get_item_class
from randomizer.data.variables.event_script_names import E3840_STARTER_DEBUG_ITEMS
from smrpgpatchbuilder.datatypes.overworld_scripts.event_scripts.commands.commands import (
        AddToInventory, AddCoins, AddFrogCoins, Return, SetVarToConst
    )

if TYPE_CHECKING:
    from ...types.gameworld import GameWorld


def apply_debug_start_items(world: GameWorld) -> None:
    """Insert starting items and coins into event script 3840 if debug mode is enabled.

    Reads items.start from debug/config.yml and adds AddToInventory commands
    for each item to E3840_STARTER_DEBUG_ITEMS, which runs at game start.
    Also adds coins and frog coins (configurable via config.yml).
    """
    if not world.settings.debug_mode:
        return


    commands = []

    config = load_debug_config()

    starting_coins = config.get("starting_coins", 9999)
    starting_frog_coins = config.get("starting_frog_coins", 99)

    # Add coins (AddCoins only takes 0-255, so we need multiple calls)
    full, remainder = divmod(starting_coins, 255)
    for _ in range(full):
        commands.append(AddCoins(255))
    if remainder > 0:
        commands.append(AddCoins(remainder))

    # Add frog coins
    if starting_frog_coins > 0:
        commands.append(SetVarToConst(PRIMARY_TEMP_7000, 999))
        commands.append(AddFrogCoins(PRIMARY_TEMP_7000))

    # Add starting items from config
    start_items = config.get("items", {}).get("start", [])
    for item_name in start_items:
        item_cls = get_item_class(item_name)
        if item_cls is not None:
            commands.append(AddToInventory(item_cls))

    commands.append(Return())

    script = world.event_scripts.get_script_by_id(E3840_STARTER_DEBUG_ITEMS)
    assert script is not None, "Event script E3840_STARTER_DEBUG_ITEMS not found"
    script.set_contents(commands)


