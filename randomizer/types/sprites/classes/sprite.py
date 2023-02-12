from enum import IntEnum
from typing import Generic, List, Optional, TypeVar, Union
from randomizer.types.numbers.classes import UInt16, UInt4, UInt8


class GridplaneFormats(IntEnum):
    _3_WIDE_3_HIGH = 0
    _3_WIDE_4_HIGH = 1
    _4_WIDE_3_HIGH = 2
    _4_WIDE_4_HIGH = 3


class Tile:
    _mirror: bool = False
    _invert: bool = False
    _format: int = 0
    _subtiles: List[Optional[bytearray]] = []

    @property
    def mirror(self) -> bool:
        return self._mirror

    def set_mirror(self, mirror: bool) -> None:
        self._mirror = mirror

    @property
    def invert(self) -> bool:
        return self._invert

    def set_invert(self, invert: bool) -> None:
        self._invert = invert

    @property
    def format(self) -> int:
        return self._format

    def set_format(self, format: int) -> None:
        self._format = format

    @property
    def subtiles(self) -> List[Optional[bytearray]]:
        return self._subtiles

    def set_subtiles(self, subtiles: List[Optional[bytearray]]) -> None:
        self._subtiles = subtiles

    def __init__(
        self,
        mirror: bool,
        invert: bool,
        format: int,
        subtiles: List[Optional[bytearray]],
    ) -> None:
        self.set_mirror(mirror)
        self.set_invert(invert)
        self.set_format(format)
        self.set_subtiles(subtiles)


class GridplaneArrangement(Tile):
    _is_16bit: bool = False
    _y_plus: bool = False
    _y_minus: bool = False

    @property
    def is_16bit(self) -> bool:
        return self._is_16bit

    def set_is_16bit(self, is_16bit: bool) -> None:
        self._is_16bit = is_16bit

    @property
    def y_plus(self) -> bool:
        return self._y_plus

    def set_y_plus(self, y_plus: bool) -> None:
        self._y_plus = y_plus

    @property
    def y_minus(self) -> bool:
        return self._y_minus

    def set_y_minus(self, y_minus: bool) -> None:
        self._y_minus = y_minus

    @property
    def format(self) -> GridplaneFormats:
        return GridplaneFormats(self._format)

    def set_format(self, format: GridplaneFormats) -> None:
        if format in [GridplaneFormats._3_WIDE_3_HIGH]:
            assert len(self.subtiles) == 9
        elif format in [
            GridplaneFormats._4_WIDE_3_HIGH,
            GridplaneFormats._3_WIDE_4_HIGH,
        ]:
            assert len(self.subtiles) == 12
        elif format in [GridplaneFormats._4_WIDE_4_HIGH]:
            assert len(self.subtiles) == 16
        else:
            raise Exception("illegal format for subtile count %i" % len(self.subtiles))
        super().set_format(format)

    def set_subtiles(
        self,
        subtiles: List[Optional[bytearray]],
        format: Optional[GridplaneFormats] = None,
    ) -> None:
        if format is None:
            if self.format in [GridplaneFormats._3_WIDE_3_HIGH]:
                assert len(subtiles) == 9
            elif self.format in [
                GridplaneFormats._4_WIDE_3_HIGH,
                GridplaneFormats._3_WIDE_4_HIGH,
            ]:
                assert len(subtiles) == 12
            elif self.format in [GridplaneFormats._4_WIDE_4_HIGH]:
                assert len(subtiles) == 16
            else:
                raise Exception("illegal subtile count (format is %i)" % self.format)
        else:
            if format in [GridplaneFormats._3_WIDE_3_HIGH]:
                assert len(subtiles) == 9
            elif format in [
                GridplaneFormats._4_WIDE_3_HIGH,
                GridplaneFormats._3_WIDE_4_HIGH,
            ]:
                assert len(subtiles) == 12
            elif format in [GridplaneFormats._4_WIDE_4_HIGH]:
                assert len(subtiles) == 16
            else:
                raise Exception("illegal subtile count for given format")
            self.set_format(format)
        super().set_subtiles(subtiles)

    def __init__(
        self,
        format: GridplaneFormats,
        subtiles: List[Optional[bytearray]],
        mirror: bool = False,
        invert: bool = False,
        y_plus: bool = False,
        y_minus: bool = False,
    ) -> None:
        super().set_mirror(mirror)
        super().set_invert(invert)
        self.set_subtiles(subtiles, format)
        self.set_y_plus(y_plus)
        self.set_y_minus(y_minus)

    @property
    def length(self):
        return 1 + len(self.subtiles) + (2 * self.is_16bit)


class NonGridplaneArrangement(Tile):
    _x: UInt16 = UInt16(0)
    _y: UInt16 = UInt16(0)

    @property
    def x(self) -> UInt16:
        return self._x

    def set_x(self, x: int) -> None:
        self._x = UInt16(x)

    @property
    def y(self) -> UInt16:
        return self._y

    def set_y(self, y: int) -> None:
        self._y = UInt16(y)

    def __init__(
        self,
        format: int,
        subtiles: List[Optional[bytearray]],
        x: int,
        y: int,
        mirror: bool = False,
        invert: bool = False,
    ) -> None:
        super().set_mirror(mirror)
        super().set_invert(invert)
        super().set_format(format)
        self.set_subtiles(subtiles)
        self.set_x(x)
        self.set_y(y)

    @property
    def length(self):
        return 3 + len([s for s in self.subtiles if s is not None])


TTile = TypeVar("TTile", bound=Tile)


class Mold(Generic[TTile]):
    _gridplane: bool
    _offset: UInt8
    _tiles: List[TTile]

    @property
    def gridplane(self) -> bool:
        return self._gridplane

    @property
    def offset(self) -> UInt8:
        return self._offset

    def set_offset(self, offset: int) -> None:
        self._offset = UInt8(offset)

    @property
    def tiles(self) -> List[TTile]:
        return self._tiles

    def set_tiles(self, tiles: List[TTile]) -> None:
        self._tiles = tiles

    def __init__(
        self,
        tiles: List[TTile],
    ) -> None:
        self.set_tiles(tiles)

    def __str__(self, index: int):
        return "<Mold %i gridplane=%r tiles=[\n  %s\n]>" % (
            index,
            self.gridplane,
            "\n  ".join([t.__str__() for t in self.tiles]),
        )

TMold = TypeVar("TMold", bound=Mold)

class GridplaneMold(Mold[GridplaneArrangement]):
    _gridplane: bool = True

    @property
    def tile(self) -> GridplaneArrangement:
        return self.tiles[0]

    def set_tile(self, tile: GridplaneArrangement) -> None:
        self._tiles = [tile]

    def __init__(
        self,
        tile: GridplaneArrangement,
    ) -> None:
        super().__init__([tile])


class NonGridplaneMold(Mold[NonGridplaneArrangement]):
    _gridplane: bool = False

    @property
    def tiles(self) -> List[NonGridplaneArrangement]:
        return super().tiles

    def set_tiles(self, tiles: List[NonGridplaneArrangement]) -> None:
        super().set_tiles(tiles)

    def __init__(
        self,
        tiles: List[NonGridplaneArrangement],
    ) -> None:
        super().__init__(tiles)


class SpriteSequenceFrame:
    _duration: UInt8 = UInt8(0)
    _mold_id: UInt8 = UInt8(0)

    @property
    def duration(self) -> UInt8:
        return self._duration

    def set_duration(self, duration: int) -> None:
        self._duration = UInt8(duration)

    @property
    def mold_id(self) -> UInt8:
        return self._mold_id

    def set_mold_id(self, mold_id: int) -> None:
        assert 0 <= mold_id < 32
        self._mold_id = UInt8(mold_id)

    def __init__(self, duration: int, mold_id: int) -> None:
        self.set_duration(duration)
        self.set_mold_id(mold_id)


class SpriteSequence:
    _frames: List[SpriteSequenceFrame] = []

    @property
    def frames(self) -> List[SpriteSequenceFrame]:
        return self._frames

    def set_frames(self, frames: List[SpriteSequenceFrame]) -> None:
        self._frames = frames

    def __init__(self, frames: List[SpriteSequenceFrame]) -> None:
        self.set_frames(frames)


class AnimationData:
    _molds: List[Union[GridplaneMold, NonGridplaneMold]]
    _sequences: List[SpriteSequence]
    _vram_size: int
    _unknown: UInt4 = UInt4(0)

    @property
    def molds(self) -> List[Union[GridplaneMold, NonGridplaneMold]]:
        return self._molds

    def set_molds(self, molds: List[Union[GridplaneMold, NonGridplaneMold]]) -> None:
        self._molds = molds

    @property
    def sequences(self) -> List[SpriteSequence]:
        return self._sequences

    def set_sequences(self, sequences: List[SpriteSequence]) -> None:
        self._sequences = sequences

    @property
    def vram_size(self) -> int:
        return self._vram_size

    def set_vram_size(self, vram_size: int) -> None:
        # must be power of 2
        assert (
            (vram_size & (vram_size - 1) == 0)
            and vram_size >= 0x100
            and vram_size <= 0x2000
        )
        self._vram_size = vram_size

    @property
    def unknown(self) -> UInt4:
        return self._unknown

    def set_unknown(self, unknown: int) -> None:
        self._unknown = UInt4(unknown)

    def __init__(
        self,
        molds: List[Union[GridplaneMold, NonGridplaneMold]],
        sequences: List[SpriteSequence],
        vram_size: int,
        unknown: int,
    ) -> None:
        self.set_molds(molds)
        self.set_sequences(sequences)
        self.set_vram_size(vram_size)
        self.set_unknown(unknown)


class SpriteContainer:
    _palette_id: UInt16 = UInt16(0)
    _palette_offset: UInt4 = UInt4(0)
    _unknown: UInt4 = UInt4(0)
    _animation_data: AnimationData

    @property
    def palette_id(self) -> UInt16:
        return self._palette_id

    def set_palette_id(self, palette_id: int) -> None:
        self._palette_id = UInt16(palette_id)

    @property
    def palette_offset(self) -> UInt4:
        return self._palette_offset

    def set_palette_offset(self, palette_offset: int) -> None:
        self._palette_offset = UInt4(palette_offset)

    @property
    def unknown(self) -> UInt4:
        return self._unknown

    def set_unknown(self, unknown: int) -> None:
        self._unknown = UInt4(unknown)

    @property
    def animation_data(self) -> AnimationData:
        return self._animation_data

    def set_animation_data(self, animation_data: AnimationData) -> None:
        self._animation_data = animation_data

    def __init__(
        self,
        palette_id: int,
        palette_offset: int,
        unknown: int,
        animation_data: AnimationData,
    ) -> None:
        self.set_palette_id(palette_id)
        self.set_palette_offset(palette_offset)
        self.set_unknown(unknown)
        self.set_animation_data(animation_data)
