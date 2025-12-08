"""Numerical util functions."""

from random import random
from randomizer.types.numbers.classes import GlobalMutator, UInt16, UInt8
from randomizer.types.overworld_scripts.variables.classes import ByteVar, ShortVar


def bools_to_int(*args: bool) -> int:
    """Accepts a series of bools and creates an int value
    by setting bits to true or false according to the order of
    the given bools. e.g. True, False, False, True = 9"""
    base: int = 0
    position: int
    val: bool
    for position, val in enumerate(args):
        base += val << position
    return base


def set_bits_to_true(bits: list[int]) -> list[bool]:
    """Sets bools in a list to true according to the indexes given
    in the bits argument."""
    array_size: int = max(bits) + 1
    bit_array: list[bool] = [False] * array_size
    for bit in bits:
        bit_array[bit] = True
    return bit_array


def bits_to_int(bits: list[int]) -> int:
    """Accepts a slice of ints and creates an int value
    by setting bits to true at the indexes indicated by
    the bits argument. e.g. [0, 3] = 9"""
    bit_array: list[bool] = set_bits_to_true(bits)
    return bools_to_int(*bit_array)


def set_difficulty(difficulty):
    """Set the difficulty level for the global mutator that shuffles stats."""
    GlobalMutator.set_difficulty(difficulty)


def coin_flip(odds: float = 0.5):
    """Weighted coin flip with odds."""
    return random() < odds


def mutate_normal(value, minimum: int = 0, maximum: int = 0xFF):
    """Mutate a stat value using the global mutator."""
    return GlobalMutator.get_mutator().mutate_normal(value, minimum, maximum)


def cast_const(value: UInt16 | UInt8 | int) -> UInt16 | UInt8:
    """Convert a number into a uint8 or a uint16 depending on size"""
    if 0 <= value <= 0xFF:
        return UInt8(value)
    return UInt16(value)


def cast_address(address: ShortVar | ByteVar) -> ShortVar | ByteVar:
    """Convert an address into a uint8 or a uint16 depending on size"""
    if 0x70A0 <= address <= 0x719F:
        return ByteVar(address)
    return ShortVar(address)
