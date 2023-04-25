"""Utils for NPCs"""

from math import ceil
from randomizer.types.npcs.objects.types.classes import Coin


def min_vram(number_of_tiles: int):
    """Get the expected min vram size from the given number of tiles."""
    return ceil(max(0, number_of_tiles - 4) / 4)


def is_coin(model):
    """Returns true if the model is a coin subclass."""
    return isinstance(model, Coin)
