"""Helper classes defining constants used in overworld and
NPC action scripts"""


class AreaObject(int):
    """Base class representing field objects, such as party members and NPCs,
    that can be targeted by overworld and NPC action script commands."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 0x2F
        return super(AreaObject, cls).__new__(cls, num)


class PartyCharacter(AreaObject):
    """Base AreaObject subclass representing field objects that can be targeted
    by commands targeting a pary member, 0x00 to 0x0B, where 0x00-0x04 represent
    your usable party members."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 0x0B
        return super(PartyCharacter, cls).__new__(cls, num)


class Direction(int):
    """Base class representing directions in which an object can walk or face."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Direction, cls).__new__(cls, num)


class Coord(int):
    """Base class representing coordinate axes for commands requiring a coordinate
    or coordinate set."""

    def __new__(cls, *args):
        num = args[0]
        assert num in [0x00, 0x01, 0x02, 0x05]
        return super(Coord, cls).__new__(cls, num)


class ControllerInput(int):
    """Base class representing an input from a specific controller button."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(ControllerInput, cls).__new__(cls, num)


class PaletteType(int):
    """Base class representing special effects that can be applied to a palette."""

    def __new__(cls, *args):
        num = args[0]
        assert num in [0x00, 0x06, 0x0C, 0x0E]
        return super(PaletteType, cls).__new__(cls, num)


class Layer(int):
    """Base class representing a graphical layer in a level."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 3
        return super(Layer, cls).__new__(cls, num)


class Colour(int):
    """Base class representing a colour to be used by certain graphics commands."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 7
        return super(Colour, cls).__new__(cls, num)


class IntroTitleText(int):
    """Base class representing predefined texts that are displayed in the game's intro."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 5
        return super(IntroTitleText, cls).__new__(cls, num)


class Scene(int):
    """Base class representing IDs for some predefined cutscenes and screen transitions."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 16
        return super(Scene, cls).__new__(cls, num)


class Tutorial(int):
    """Base class representing IDs for some predefined in-game tutorial modes."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 3
        return super(Tutorial, cls).__new__(cls, num)


class Battlefield(int):
    """Base class representing IDs for valid battlefields."""

    def __new__(cls, *args):
        num = args[0]
        assert 0 <= num <= 63
        return super(Battlefield, cls).__new__(cls, num)
