class Target(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(Target, cls).__new__(cls, num)


class CommandType(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 2
        return super(CommandType, cls).__new__(cls, num)
