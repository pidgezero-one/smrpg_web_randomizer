"""Base classes for numbers and numerical operations."""

from random import random, randint

from .constants import SMALL_BOOST_AMOUNT


class Mutator:
    """Mutator class that shuffles stat attributes based on min/max values
    and a difficulty setting."""

    def __init__(self, difficulty=None):
        # Placeholder for future difficulty option.
        self.difficulty = difficulty

    def mutate_normal(self, value: int | float, minimum=0, maximum=0xFF) -> int:
        """Mutate a value with a given range.
        This is roughly simulating a normal distribution with mean <value>,
        std deviation approx 1/5 <value>."""
        # The actual value we're shuffling is the difference between the default value
        # and the minimum or maximum, whichever is smaller.
        # Shuffle this distance value, then recompute the new actual value below.
        value = max(minimum, min(value, maximum))
        reverse = value > (minimum + maximum) / 2

        if reverse:
            value = maximum - value
        else:
            value = value - minimum

        # For very small values, give a small boost amount to allow for a bit more variance.
        # Subtract this later.
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
            random_a, random_b = random(), random()
            value = half + (half * random_a) + (half * random_b)

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
        value = max(minimum, min(value, maximum))
        value = int(round(value))
        return value


class GlobalMutator:
    """Container class for the global mutator instance so we can control the difficulty."""

    mutator = Mutator()

    @classmethod
    def get_mutator(cls) -> Mutator:
        """Return the mutator."""
        return cls.mutator

    @classmethod
    def set_difficulty(cls, difficulty) -> None:
        """Set the mutator difficulty."""
        cls.mutator.difficulty = difficulty
