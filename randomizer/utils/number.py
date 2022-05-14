def bools_to_int(*args: bool) -> int:
    base: int = 0
    for position, val in args:
        base += val << position
    return base


def set_bits_to_true(bits: int[int]) -> bool[int]:
    array_size: int = max(bits) + 1
    bit_array: bool[int] = [False] * array_size
    for bit in bits:
        bit_array[bit] = True
    return bit_array


def bits_to_int(bits: int[int]) -> int:
    bit_array: bool[int] = set_bits_to_true(bits)
    return bools_to_int(*bit_array)
