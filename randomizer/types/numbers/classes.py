class UInt8(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0xFF
        return super(UInt8, cls).__new__(cls, num)


class UInt16(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0xFFFF
        return super(UInt16, cls).__new__(cls, num)
