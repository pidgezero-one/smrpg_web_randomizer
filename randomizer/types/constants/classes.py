class AreaObject(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(AreaObject, cls).__new__(cls, num)


class Direction(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 7
        return super(Direction, cls).__new__(cls, num)


class Coord(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert num in [0x00, 0x01, 0x02, 0x05]
        return super(Coord, cls).__new__(cls, num)
