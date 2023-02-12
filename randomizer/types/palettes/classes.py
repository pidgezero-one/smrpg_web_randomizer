from os import renames
from typing import List
from randomizer.types.patch.classes import Patch
from randomizer.types.palettes.constants import (
    CLASSIC_PALETTE_OFFSET,
    MAP_PALETTE_OFFSET,
    MINECART_PALETTE_OFFSET,
    UNKNOWN_PALETTE_ADDR,
)


class Palette(list):
    def __new__(cls, *args, **kwargs):
        for colour in args[0]:
            assert isinstance(colour, int)
            assert (colour >> 16) % 8 == 0
            assert (colour >> 8) % 8 == 0
            assert colour % 8 == 0
        return super(Palette, cls).__new__(cls, *args)

    @classmethod
    def _colour_bytes(cls, colour) -> bytearray:
        r = colour >> 19
        g = (colour >> 10) & 0x3E
        b = (colour >> 1) & 0x7C

        byte_1 = r + ((g << 4) & 0xF0)
        byte_2 = b + (g >> 4)
        return bytearray([byte_1, byte_2])

    def to_bytes(self) -> bytearray:
        output = bytearray()
        for colour in self:
            output += Palette._colour_bytes(colour)
        assert len(output) == 30
        return output


class EffectPalette(Palette):
    pass


class SpritePalette(Palette):
    def __new__(cls, *args, **kwargs):
        assert len(*args) == 15
        return super(SpritePalette, cls).__new__(cls, *args)


class CharacterPaletteSet:
    _name: str = ""
    _original_name: str = ""
    _original_clone_name: str = ""

    _addresses_for_default_palette: List[int] = []
    _addresses_for_doll_colours: List[int] = []
    _addresses_for_poison_palette: List[int] = []
    _addresses_for_underwater_palette: List[int] = []

    _address_for_name: int = 0
    _address_for_clone_name: int = 0

    _default_colours: SpritePalette
    _poison_colours: SpritePalette
    _underwater_colours: SpritePalette

    minecart_colours: SpritePalette
    overworld_colours: SpritePalette
    classic_colours: SpritePalette

    @property
    def name(self) -> str:
        return self._name

    @property
    def original_name(self) -> str:
        return self._original_name

    def set_original_name(self, original_name: str) -> None:
        self._original_name = original_name

    @property
    def original_clone_name(self) -> str:
        return self._original_clone_name

    def set_original_clone_name(self, original_clone_name: str) -> None:
        self._original_clone_name = original_clone_name

    @property
    def addresses_for_default_palette(self) -> List[int]:
        return self._addresses_for_default_palette

    @property
    def addresses_for_doll_colours(self) -> List[int]:
        return self._addresses_for_doll_colours

    @property
    def addresses_for_poison_palette(self) -> List[int]:
        return self._addresses_for_poison_palette

    @property
    def addresses_for_underwater_palette(self) -> List[int]:
        return self._addresses_for_underwater_palette

    @property
    def address_for_name(self) -> int:
        return self._address_for_name

    @property
    def address_for_clone_name(self) -> int:
        return self._address_for_clone_name

    @property
    def default_colours(self) -> SpritePalette:
        return self._default_colours

    @property
    def poison_colours(self) -> SpritePalette:
        return self._poison_colours

    @property
    def underwater_colours(self) -> SpritePalette:
        return self._underwater_colours

    @classmethod
    def _pad_name(cls, name: str) -> str:
        empty_space_length = 13 - len(name)
        return name + " " * empty_space_length

    @property
    def clone_name(self) -> str:
        clone_name: str = self.name.upper()
        if len(self.name) < 8:
            clone_name += " CLONE"
        else:
            clone_name += " 2"
        return CharacterPaletteSet._pad_name(clone_name)

    def get_patch(
        self, rename_character: bool = False, main_character: bool = False
    ) -> Patch:
        patch = Patch()
        names = (self.original_name, self.original_clone_name)
        if rename_character:
            names = (self.name, self.clone_name)
        patch.add_data(self.address_for_name, CharacterPaletteSet._pad_name(names[0]))
        patch.add_data(
            self.address_for_clone_name,
            CharacterPaletteSet._pad_name(names[1]),
        )
        for address in self.addresses_for_default_palette:
            patch.add_data(address, self.default_colours.to_bytes())
        for address in self.addresses_for_poison_palette:
            patch.add_data(address, self.poison_colours.to_bytes())
        for address in self.addresses_for_underwater_palette:
            patch.add_data(address, self.underwater_colours.to_bytes())
        if main_character:
            patch.add_data(MINECART_PALETTE_OFFSET, self.minecart_colours.to_bytes())
            patch.add_data(CLASSIC_PALETTE_OFFSET, self.classic_colours.to_bytes())
            patch.add_data(MAP_PALETTE_OFFSET, self.overworld_colours.to_bytes())
            patch.add_data(UNKNOWN_PALETTE_ADDR, self.default_colours.to_bytes())

        return patch


class MarioPaletteSet(CharacterPaletteSet):
    _name: str = "Mario"
    _original_name: str = "Mario"
    _original_clone_name: str = "MARIO CLONE"

    _addresses_for_default_palette: List[int] = [
        # overworld
        0x257998,
        # battle
        0x257B78,
        # portrait
        0x256B88,
        # doll 2
        0x257A4C,
        # scarecrow/mushroom
        0x256AF2,
        # ?
        0x257AE2,
        # ?
        # 0x37A9D8,
        # ?
        0x3EDFFD,
        # ?
        0x3EE0FF,
    ]
    _addresses_for_doll_colours: List[int] = [
        # doll 1 - for mario, 6th colour should be 7th in palette, 7th colour should be 8th in palette, and 8th and 9th colour should both be 9th in palette. 10th colour should be 11th in palette, 11th and 12th colour should be 12th in palette
        # 0x2576E6
        0x258D66
    ]
    _addresses_for_poison_palette: List[int] = [
        0x2579D4,
        0x257BB4,
        0x256BC4,
        # ?
        0x257722,
    ]
    _addresses_for_underwater_palette: List[int] = [0x257A10, 0x257BF0]

    _address_for_name: int = 0x3A134D
    _address_for_clone_name: int = 0x399A96

    @property
    def classic_colours(self) -> EffectPalette:
        return EffectPalette(
            [self.default_colours[10], self.default_colours[6], self.default_colours[1]]
        )

    @property
    def doll_colours(self) -> SpritePalette:
        return SpritePalette(
            [
                self.default_colours[0],
                self.default_colours[1],
                self.default_colours[2],
                self.default_colours[3],
                self.default_colours[4],
                self.default_colours[6],
                self.default_colours[7],
                self.default_colours[8],
                self.default_colours[8],
                self.default_colours[10],
                self.default_colours[11],
                self.default_colours[11],
                self.default_colours[12],
                self.default_colours[13],
                self.default_colours[14],
            ]
        )

    @property
    def minecart_colours(self) -> SpritePalette:
        return SpritePalette(
            [
                0xF8F8F8,
                self.default_colours[13],
                self.default_colours[1],
                self.default_colours[2],
                self.default_colours[8],
                self.default_colours[5],
                self.default_colours[3],
                self.default_colours[6],
                self.default_colours[7],
                self.default_colours[9],
                self.default_colours[4],
                self.default_colours[9],
                self.default_colours[8],
                self.default_colours[10],
                self.default_colours[11],
            ]
        )

    @property
    def overworld_colours(self) -> SpritePalette:
        return SpritePalette(
            [
                self.default_colours[0],
                self.default_colours[1],
                self.default_colours[2],
                self.default_colours[3],
                self.default_colours[4],
                self.default_colours[6],
                self.default_colours[7],
                self.default_colours[8],
                self.default_colours[8],
                self.default_colours[10],
                self.default_colours[11],
                self.default_colours[11],
                self.default_colours[12],
                self.default_colours[13],
                self.default_colours[14],
            ]
        )

    def get_patch(
        self, rename_character: bool = False, main_character: bool = False
    ) -> Patch:
        patch = super().get_patch(rename_character, main_character)
        for address in self.addresses_for_doll_colours:
            patch.add_data(address, self.doll_colours.to_bytes())

        return patch


class MallowPaletteSet(CharacterPaletteSet):
    _name: str = "Mallow"
    _original_name: str = "Mallow"
    _original_clone_name: str = "MALLOW CLONE"

    _addresses_for_default_palette: List[int] = [
        # overworld
        0x2581AE,
        # battle
        0x258244,
        # portrait
        0x256B4C,
        # doll 1 - for mallow, skip 8th and 9th colour replacement
        # maybe leave this out since mario and peach in credits have to share a palette and im probably not going to change them
        # 0x2583CA,
        # scarecrow/mushroom
        # 0x256B4C
        # ?
        # 0x37A9F6
    ]
    _addresses_for_doll_colours: List[int] = []
    _addresses_for_poison_palette: List[int] = [0x2581EA, 0x258280]
    _addresses_for_underwater_palette: List[int] = [0x258226, 0x2582BC]

    _address_for_name: int = 0x3A1375
    _address_for_clone_name: int = 0x399ACA

    # todo
    @property
    def classic_colours(self) -> EffectPalette:
        return EffectPalette(self.default_colours)

    @property
    def doll_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def minecart_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def overworld_colours(self) -> SpritePalette:
        return self.default_colours


class GenoPaletteSet(CharacterPaletteSet):
    _name: str = "Geno"
    _original_name: str = "Geno"
    _original_clone_name: str = "GENO CLONE"

    _addresses_for_default_palette: List[int] = [
        # overworld
        0x258046,
        # battle
        0x2580FA,
        # portrait
        0x256B6A,
        # doll 1
        0x257A88,
        # scarecrow/mushroom
        # 0x256B6A,
        # ?
        # 0x37AA14
    ]
    _addresses_for_doll_colours: List[int] = []
    _addresses_for_poison_palette: List[int] = [0x258082, 0x258136]
    _addresses_for_underwater_palette: List[int] = [0x2580BE, 0x258172]

    _address_for_name: int = 0x3A136B
    _address_for_clone_name: int = 0x399ABD

    @property
    def classic_colours(self) -> EffectPalette:
        return EffectPalette(
            [self.default_colours[3], self.default_colours[6], self.default_colours[1]]
        )

    @property
    def doll_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def minecart_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def overworld_colours(self) -> SpritePalette:
        return self.default_colours


class BowserPaletteSet(CharacterPaletteSet):
    _name: str = "Bowser"
    _original_name: str = "Bowser"
    _original_clone_name: str = "BOWSER CLONE"

    _addresses_for_default_palette: List[int] = [
        # overworld
        0x257DD0,
        # battle
        0x257E66,
        # portrait
        0x256B2E,
        # doll 1
        0x257AA6,
        # scarecrow/mushroom
        # 0x256B2E,
        # ending credits
        # 0x2585AA,
        # ?
        # 0x37B068
    ]
    _addresses_for_doll_colours: List[int] = []
    _addresses_for_poison_palette: List[int] = [0x257E0C, 0x257EA2]
    _addresses_for_underwater_palette: List[int] = [0x257E48, 0x257EDE]

    _address_for_name: int = 0x3A1361
    _address_for_clone_name: int = 0x399AB0

    # needs to be updated
    @property
    def classic_colours(self) -> EffectPalette:
        return EffectPalette(self.default_colours)

    @property
    def doll_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def minecart_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def overworld_colours(self) -> SpritePalette:
        return self.default_colours


class ToadstoolPaletteSet(CharacterPaletteSet):
    _name: str = "Toadstool"
    _original_name: str = "Toadstool"
    _original_clone_name: str = "TOADSTOOL 2"

    _addresses_for_default_palette: List[int] = [
        # overworld
        0x257CA4,
        # battle
        0x257D3A,
        # portrait
        0x256B10,
        # doll 1
        0x257AC4,
        # scarecrow/mushroom
        # 0x256B10,
        # ?
        # 0x37B086
    ]
    _addresses_for_doll_colours: List[int] = []
    _addresses_for_poison_palette: List[int] = [0x257CE0, 0x257D76]
    _addresses_for_underwater_palette: List[int] = [0x257D1C, 0x257DB2]

    _address_for_name: int = 0x3A1357
    _address_for_clone_name: int = 0x399AA3

    @property
    def classic_colours(self) -> EffectPalette:
        return EffectPalette(
            [self.default_colours[6], self.default_colours[3], self.default_colours[1]]
        )

    @property
    def doll_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def minecart_colours(self) -> SpritePalette:
        return self.default_colours

    @property
    def overworld_colours(self) -> SpritePalette:
        return self.default_colours
