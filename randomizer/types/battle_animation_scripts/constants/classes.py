from typing import Tuple

from randomizer.types.numbers.classes import Int8


class Origin(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 3
        return super(Origin, cls).__new__(cls, num)


class PauseUntil(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x10
        return super(PauseUntil, cls).__new__(cls, num)


class ShiftType(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x08
        assert num % 2 == 0
        return super(ShiftType, cls).__new__(cls, num)


class MessageType(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 2
        return super(MessageType, cls).__new__(cls, num)


class LayerPriorityType(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 3
        return super(LayerPriorityType, cls).__new__(cls, num)


class FlashColour(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 7
        return super(FlashColour, cls).__new__(cls, num)


class BonusMessage(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 6
        return super(BonusMessage, cls).__new__(cls, num)


class BattleTarget(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 47
        return super(BattleTarget, cls).__new__(cls, num)


class MaskEffect(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 7
        return super(MaskEffect, cls).__new__(cls, num)


class MaskPoint(Tuple[Int8, Int8]):
    def __new__(cls, *args, **kwargs):
        assert len(args) == 2
        tup = (Int8(args[0]), Int8(args[1]))
        return super(MaskPoint, cls).__new__(cls, tup)
