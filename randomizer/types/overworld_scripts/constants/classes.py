class AreaObject(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(AreaObject, cls).__new__(cls, num)


class PartyCharacter(AreaObject):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 0x0B
        return super(PartyCharacter, cls).__new__(cls, num)


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


class ControllerInput(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 7
        return super(ControllerInput, cls).__new__(cls, num)


class PaletteType(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert num in [0x00, 0x06, 0x0C, 0x0E]
        return super(PaletteType, cls).__new__(cls, num)


class Layer(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 3
        return super(Layer, cls).__new__(cls, num)


class Colour(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 7
        return super(Colour, cls).__new__(cls, num)


class IntroTitleText(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 5
        return super(IntroTitleText, cls).__new__(cls, num)


class Scene(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 16
        return super(Scene, cls).__new__(cls, num)


class Tutorial(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 3
        return super(Tutorial, cls).__new__(cls, num)


class Battlefield(int):
    def __new__(cls, *args, **kwargs):
        num = args[0]
        assert 0 <= num <= 63
        return super(Battlefield, cls).__new__(cls, num)
