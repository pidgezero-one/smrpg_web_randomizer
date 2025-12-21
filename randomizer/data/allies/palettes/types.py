def color_to_bytes(color):
    color_int = int(color, 16)
    r = color_int >> 19
    g = (color_int >> 10) & 0x3E
    b = (color_int >> 1) & 0x7C

    byte_1 = r + ((g << 4) & 0xF0)
    byte_2 = b + (g >> 4)
    return [byte_1, byte_2]


def palette_to_bytes(colors):
    ret = []
    for color in colors:
        ret += color_to_bytes(color)
    return ret


classic_palette_offset = 0x2567E6
minecart_palette_offset = 0x256DFE
map_palette_offset = 0x3E99C1


class Palette:

    # Address array = should be an array containing all child arrays that need palette changes
    # Child arrays should be 16 addresses in length... or maybe 15. Seems the first address is unused?
    starting_addresses: list[int] = []
    doll_addresses: list[int] = (
        []
    )  # only populate this if it follows different palette rules. currently only used for mario
    poison_addresses: list[int] = []
    underwater_addresses: list[int] = []
    classic_addresses: list[int] = []

    colours: list[str] = []
    poison_colours: list[str] = []
    underwater_colours: list[str] = []
    classic_colours: list[str] | None = None
    overworld_map_colours: list[str] | None = None
    name_address = 0
    clone_name_address = 0
    original_name = ""
    name = ""
    rename_character = True

    @property
    def clone_name(self, rename_character = None) -> str:
        rename = self.rename_character if rename_character is None else rename_character
        name = (self.name if rename else self.original_name).upper()
        if len(name) <= 7:
            return f"{name} CLONE"
        if len(name) <= 8:
            return f"{name} COPY"
        if len(name) <= 11:
            return f"{name} 2"
        return f"{name[0:10]}. 2"

    @property
    def strong_clone_name(self, rename_character = None) -> str:
        rename = self.rename_character if rename_character is None else rename_character
        name = (self.name if rename else self.original_name).upper()
        if len(name) <= 5:
            return f"{name} CLONE S"
        if len(name) <= 6:
            return f"{name} COPY S"
        if len(name) <= 11:
            return f"{name} 3"
        return f"{name[0:10]}. 3"

    def special_palette(
        self, colours: list[int | None], address: int
    ) -> dict[int, bytearray]:
        patch: dict[int, bytearray] = {}
        for j in range(0, len(colours)):
            i = colours[j]
            if i is not None:
                colour = self.colours[i]
                patch[address + j * 2] = bytearray(color_to_bytes(colour))
        return patch

    def palette_override(
        self, colours: list[str], address: int
    ) -> dict[int, bytearray]:
        patch: dict[int, bytearray] = {}
        for j in range(0, len(colours)):
            patch[address + j * 2] = bytearray(color_to_bytes(colours[j]))
        return patch

    # TODO poison palettes, underwater palettes
    def standard_patch(self) -> dict[int, bytearray]:
        patch: dict[int, bytearray] = {}
        if self.colours is not None:
            for addr in self.starting_addresses:
                patch.update(self.palette_override(self.colours, addr))
        for addr in self.poison_addresses:
            if self.poison_colours is not None:
                patch.update(self.palette_override(self.poison_colours, addr))
        for addr in self.underwater_addresses:
            if self.underwater_colours is not None:
                patch.update(self.palette_override(self.underwater_colours, addr))
        return patch


class MarioPalette(Palette):
    starting_addresses = [
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
    doll_addresses: list[int] = [
        # doll 1 - for mario, 6th colour should be 7th in palette, 7th colour should be 8th in palette, and 8th and 9th colour should both be 9th in palette. 10th colour should be 11th in palette, 11th and 12th colour should be 12th in palette
        # 0x2576E6
        0x258D66
    ]
    poison_addresses: list[int] = [
        0x2579D4,
        0x257BB4,
        0x256BC4,
        # ?
        0x257722,
    ]
    # Poison palette for battle portrait will not be edited. It is shared by all 5 characters.
    underwater_addresses: list[int] = [0x257A10, 0x257BF0]
    name_address = 0x3A134D
    clone_name_address = 0x399A96
    # poison - 646
    # underwater - 648
    name = "Mario"
    _original_name = "Mario"

    def doll_patch(self) -> dict[int, bytearray]:
        if self.colours is None:
            return {}
        return self.special_palette(
            [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14], self.doll_addresses[0]
        )

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, classic_palette_offset)
        if self.colours is None:
            return {}
        return self.special_palette(
            [
                10,
                6,
                1,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            classic_palette_offset,
        )

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours is None:
            return {}
        return self.special_palette(
            [None, 13, 1, 2, None, 5, 3, 6, 7, 9, 4, 9, 8, 10, 11],
            minecart_palette_offset,
        )

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.colours is None:
            return {}
        return self.special_palette(
            [0, 1, 2, 3, 4, 6, 7, 8, 8, 10, 11, 11, 12, 13, 14],
            map_palette_offset,
        )


class MallowPalette(Palette):
    starting_addresses = [
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
    poison_addresses = [0x2581EA, 0x258280]
    # Poison palette for battle portrait will not be edited. It is shared by all 5 characters.
    underwater_addresses = [0x258226, 0x2582BC]
    name_address = 0x3A1375
    clone_name_address = 0x399ACA
    # poison - 704
    # underwater - 706
    name = "Mallow"
    _original_name = "Mallow"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, classic_palette_offset)
        if self.colours is not None:
            return self.palette_override(self.colours, classic_palette_offset)
        return {}

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours is not None:
            return self.palette_override(
                self.colours,
                minecart_palette_offset,
            )
        else:
            return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, map_palette_offset)
        if self.colours is not None:
            return self.palette_override(self.colours, map_palette_offset)
        return {}


class GenoPalette(Palette):
    starting_addresses = [
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
    poison_addresses = [0x258082, 0x258136]
    # Poison palette for battle portrait will not be edited. It is shared by all 5 characters.
    underwater_addresses = [0x2580BE, 0x258172]
    name_address = 0x3A136B
    clone_name_address = 0x399ABD
    # poison - 693
    # underwater - 695
    name = "Geno"
    _original_name = "Geno"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, classic_palette_offset)
        return self.special_palette(
            [
                3,
                6,
                1,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            classic_palette_offset,
        )

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours is not None:
            return self.palette_override(
                self.colours,
                minecart_palette_offset,
            )
        else:
            return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, map_palette_offset)
        if self.colours is not None:
            return self.palette_override(self.colours, map_palette_offset)
        return {}


class BowserPalette(Palette):
    starting_addresses = [
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
    name_address = 0x3A1361
    clone_name_address = 0x399AB0
    poison_addresses = [0x257E0C, 0x257EA2]
    # Poison palette for battle portrait will not be edited. It is shared by all 5 characters.
    underwater_addresses = [0x257E48, 0x257EDE]
    # poison - 671
    # underwater - 673
    name = "Bowser"
    _original_name = "Bowser"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, classic_palette_offset)
        if self.colours is not None:
            return self.palette_override(self.colours, classic_palette_offset)
        return {}

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours is not None:
            return self.palette_override(
                self.colours,
                minecart_palette_offset,
            )
        else:
            return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, map_palette_offset)
        if self.colours is not None:
            return self.palette_override(self.colours, map_palette_offset)
        return {}


class ToadstoolPalette(Palette):
    starting_addresses = [
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
    name_address = 0x3A1357
    clone_name_address = 0x399AA3
    poison_addresses = [0x257CE0, 0x257D76]
    # Poison palette for battle portrait will not be edited. It is shared by all 5 characters.
    underwater_addresses = [0x257D1C, 0x257DB2]
    # poison - 656
    # underwater - 658
    name = "Toadstool"
    _original_name = "Toadstool"

    def doll_patch(self) -> dict[int, bytearray]:
        return {}

    def classic_patch(self) -> dict[int, bytearray]:
        if self.classic_colours is not None:
            return self.palette_override(self.classic_colours, classic_palette_offset)
        return self.special_palette(
            [
                6,
                3,
                1,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ],
            classic_palette_offset,
        )

    def minecart_patch(self) -> dict[int, bytearray]:
        if self.colours is not None:
            return self.palette_override(
                self.colours,
                minecart_palette_offset,
            )
        else:
            return {}

    def overworld_map_patch(self) -> dict[int, bytearray]:
        if self.overworld_map_colours is not None:
            return self.palette_override(self.overworld_map_colours, map_palette_offset)
        if self.colours is not None:
            return self.palette_override(self.colours, map_palette_offset)
        return {}
