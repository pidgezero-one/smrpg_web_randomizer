from typing import List
from randomizer.types.numbers.classes import GlobalMutator
from random import random


def bools_to_int(*args: bool) -> int:
    base: int = 0
    position: int
    val: bool
    for position, val in enumerate(args):
        base += val << position
    return base


def set_bits_to_true(bits: List[int]) -> List[bool]:
    array_size: int = max(bits) + 1
    bit_array: List[bool] = [False] * array_size
    for bit in bits:
        bit_array[bit] = True
    return bit_array


def bits_to_int(bits: List[int]) -> int:
    bit_array: List[bool] = set_bits_to_true(bits)
    return bools_to_int(*bit_array)


def mutate_normal(value, minimum: int = 0, maximum: int = 0xFF):
    """Mutate a stat value using the global mutator."""
    return GlobalMutator.get_mutator().mutate_normal(value, minimum, maximum)


def set_difficulty(difficulty):
    """Set the difficulty level for the global mutator that shuffles stats."""
    GlobalMutator.set_difficulty(difficulty)


def coin_flip(odds: float = 0.5):
    """Weighted coin flip with odds."""
    return random() < odds
