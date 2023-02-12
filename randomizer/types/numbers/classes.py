from typing import Union
from randomizer.types.numbers.constants import SMALL_BOOST_AMOUNT
from random import random, randint


class UInt4(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x0F
        return super(UInt4, cls).__new__(cls, num)

    def to_byte(self) -> int:
        return self


class UInt8(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0xFF
        return super(UInt8, cls).__new__(cls, num)

    def to_byte(self) -> int:
        return int(self)


class Int8(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        if num > 127:
            offset = num - 127 - 1
            num = -128 + offset
        assert -128 <= num <= 127
        return super(Int8, cls).__new__(cls, num)

    def to_byte(self) -> int:
        if self < 0:
            val = 0x100 + self
        else:
            val = int(self)
        return val


class UInt16(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0xFFFF
        return super(UInt16, cls).__new__(cls, num)

    def to_bytes(self) -> int:
        return self

    def little_endian(self) -> bytearray:
        return bytearray([(self & 0xFF), ((self >> 8))])


class Int16(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        if num > 32767:
            offset = num - 32767 - 1
            num = -32768 + offset
        assert -32768 <= num <= 32767
        return super(Int16, cls).__new__(cls, num)

    def to_bytes(self) -> int:
        if self < 0:
            val = 0x10000 + self
        else:
            val = self
        return val

    def little_endian(self) -> bytearray:
        val = self.to_bytes()
        return bytearray([(val & 0xFF), ((val >> 8))])


class BitMapSet(set):
    """A class representing a bitmap of a certain length using the set built-in type to track which bits are set."""

    def __init__(self, num_bytes=1, *args, **kwargs):
        """
        :type num_bytes: int
        """
        super().__init__(*args, **kwargs)
        self._num_bytes = num_bytes

    def as_bytes(self):
        """Return bitmap in little endian byte format for ROM patching.

        :rtype: bytearray
        """
        result = 0
        for value in self:
            result |= 1 << value
        return result.to_bytes(self._num_bytes, "little")

    def __str__(self):
        return "BitMapSet({})".format(super().__str__())


class ByteField:
    """Base class for an integer value field spanning one or more bytes."""

    def __init__(self, value: Union[UInt8, UInt16, int], num_bytes: int = 1):
        """
        :type value: int
        :type num_bytes: int
        """
        if isinstance(value, UInt16):
            num_bytes = 2
        self._value = int(value)
        self._num_bytes = num_bytes

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = int(value)

    def as_bytes(self):
        """Return current value of this stat as a little-endian byte array for the patch.  If the value is less than
        zero, convert this to a signed int in byte format.

        :rtype: bytearray
        """
        if self._value < 0:
            val = self._value + (2 ** (self._num_bytes * 8))
        else:
            val = self._value
        return val.to_bytes(self._num_bytes, "little")

    def __str__(self):
        return "ByteField(current value: {}, number of bytes: {}".format(
            self.value, self._num_bytes
        )


class Mutator:
    """Mutator class that shuffles stat attributes based on min/max values and a difficulty setting."""

    def __init__(self, difficulty=None):
        # Placeholder for future difficulty option.
        self.difficulty = difficulty

    def mutate_normal(self, value, minimum=0, maximum=0xFF):
        """Mutate a value with a given range.
        This is roughly simulating a normal distribution with mean <value>, std deviation approx 1/5 <value>.
        """
        # The actual value we're shuffling is the difference between the default value and the minimum or maximum,
        # whichever is smaller.  Shuffle this distance value, then recompute the new actual value below.
        value = max(minimum, min(value, maximum))
        if value > (minimum + maximum) / 2:
            reverse = True
        else:
            reverse = False

        if reverse:
            value = maximum - value
        else:
            value = value - minimum

        # For very small values, give a small boost amount to allow for a bit more variance.  Subtract this later.
        boosted = False
        if value < SMALL_BOOST_AMOUNT:
            value += SMALL_BOOST_AMOUNT
            if value > 0:
                boosted = True
            else:
                value = 0

        # Make new random value.
        if value > 0:
            half = value / 2.0
            a, b = random(), random()
            value = half + (half * a) + (half * b)

        # If we boosted the value, bring it back down now.
        if boosted:
            value -= SMALL_BOOST_AMOUNT

        # Compute actual final value with new distance from minimum/maximum.
        if reverse:
            value = maximum - value
        else:
            value = value + minimum

        # 1/10 chance to chain mutate for more variance.
        if randint(1, 10) == 10:
            return self.mutate_normal(value, minimum=minimum, maximum=maximum)
        else:
            value = max(minimum, min(value, maximum))
            value = int(round(value))
            return value


class GlobalMutator:
    """Container class for the global mutator instance so we can control the difficulty."""

    mutator = Mutator()

    @classmethod
    def get_mutator(cls):
        return cls.mutator

    @classmethod
    def set_difficulty(cls, difficulty):
        cls.mutator.difficulty = difficulty
