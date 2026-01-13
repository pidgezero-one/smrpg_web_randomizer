"""Debug configuration loader and utilities."""

import yaml
from pathlib import Path
from typing import Any


def load_debug_config() -> dict[str, Any]:
    """Load debug config from config.yml."""
    config_path = Path(__file__).parent / "config.yml"
    if not config_path.exists():
        return {}
    with open(config_path) as f:
        return yaml.safe_load(f) or {}


def get_item_class(name: str):
    """Get item class by exact name from randomizer.data.items.

    Args:
        name: Exact class name (e.g., 'CastleKey1Item')

    Returns:
        The item class, or None if not found.
    """
    from randomizer.data import items
    cls = getattr(items, name, None)
    if cls is None:
        print(f"Warning: Item class '{name}' not found")
    return cls


def get_prize_class(name: str):
    """Get prize class by exact name from randomizer.progression.prizes.

    Args:
        name: Exact class name (e.g., 'CastleKey1Prize')

    Returns:
        The prize class, or None if not found.
    """
    from randomizer.progression import prizes
    cls = getattr(prizes, name, None)
    if cls is None:
        print(f"Warning: Prize class '{name}' not found")
    return cls


def get_location_class(name: str):
    """Get location class by exact name from randomizer.progression.prizelocations.

    Args:
        name: Exact class name (e.g., 'MushroomWay1LowerChest')

    Returns:
        The location class, or None if not found.
    """
    from randomizer.progression import prizelocations
    cls = getattr(prizelocations, name, None)
    if cls is None:
        print(f"Warning: Location class '{name}' not found")
    return cls
