from randomizer.types.numbers.classes import UInt16, UInt4, UInt8

# disassembler classes


class Sprite:
    _index: UInt16
    _image_num: UInt16
    _palette_offset: UInt4
    _animation_num: UInt16
    _unknown: UInt8

    @property
    def index(self) -> UInt16:
        return self._index

    def set_index(self, index: int) -> None:
        self._index = UInt16(index)

    @property
    def image_num(self) -> UInt16:
        return self._image_num

    def set_image_num(self, image_num: int) -> None:
        assert 0 <= image_num < 512
        self._image_num = UInt16(image_num)

    @property
    def palette_offset(self) -> UInt4:
        return self._palette_offset

    def set_palette_offset(self, palette_offset: int) -> None:
        self._palette_offset = UInt4(palette_offset)

    @property
    def animation_num(self) -> UInt16:
        return self._animation_num

    def set_animation_num(self, animation_num: int) -> None:
        self._animation_num = UInt16(animation_num)

    @property
    def unknown(self) -> UInt8:
        return self._unknown

    def set_unknown(self, unknown: int) -> None:
        self._unknown = UInt8(unknown)

    def __init__(
        self,
        index: int,
        image_num: int,
        palette_offset: int,
        animation_num: int,
        unknown: int,
    ) -> None:
        self.set_index(index)
        self.set_image_num(image_num)
        self.set_palette_offset(palette_offset)
        self.set_animation_num(animation_num)
        self.set_unknown(unknown)


class ImagePack:
    _index: UInt16
    _graphics_pointer: int
    _palette_pointer: int

    @property
    def index(self) -> UInt16:
        return self._index

    def set_index(self, index: int) -> None:
        assert 0 <= index < 512
        self._index = UInt16(index)

    @property
    def graphics_pointer(self) -> int:
        return self._graphics_pointer

    def set_graphics_pointer(self, graphics_pointer: int) -> None:
        self._graphics_pointer = graphics_pointer

    @property
    def palette_pointer(self) -> int:
        return self._palette_pointer

    def set_palette_pointer(self, palette_pointer: int) -> None:
        self._palette_pointer = palette_pointer

    def __init__(
        self,
        index: int,
        graphics_pointer: int,
        palette_pointer: int,
    ) -> None:
        self.set_index(index)
        self.set_graphics_pointer(graphics_pointer)
        self.set_palette_pointer(palette_pointer)
