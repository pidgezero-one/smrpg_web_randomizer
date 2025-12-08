class _TileTuple(
    tuple[
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int,
        int
    ]
):
    def __new__(cls, bytes: bytearray):
        assert len(bytes) == 0x20
        return tuple.__new__(cls, tuple(bytes))
        
x = _TileTuple(bytearray([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10, 11, 12, 13, 14, 15, 16 ,17, 18, 19, 20 ,21 ,22 ,23, 24, 25, 26, 27, 28, 29, 30 ,31]))

y = _TileTuple(bytearray([0, 1, 2, 3, 4, 5, 6, 7, 8 ,9 , 10, 11, 12, 13, 14, 15, 16 ,17, 18, 19, 20 ,21 ,22 ,23, 24, 25, 26, 27, 28, 29, 30 ,31]))

array = ["x", x]

print(array.index(y))