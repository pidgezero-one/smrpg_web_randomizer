class ActionScriptCommandName(str):
    pass


class SequenceSpeed(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 6
        return super(SequenceSpeed, cls).__new__(cls, num)


class VRAMPriority(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 3
        return super(Priority, cls).__new__(cls, num)
