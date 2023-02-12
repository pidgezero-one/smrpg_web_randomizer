from randomizer.types.palettes.classes import MallowPaletteSet, SpritePalette


class Default(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0xF0F090,
            0xD8D878,
            0xA0A058,
            0x403828,
            0xF868D0,
            0x902848,
            0x582038,
            0x300810,
            0x28E8F8,
            0x1890B8,
            0x105060,
            0xA08888,
            0x686848,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0xD8C0E8,
            0xC0A8D0,
            0xA070A0,
            0x603860,
            0xF868D0,
            0xC038C0,
            0x782078,
            0x481848,
            0xA0A8F8,
            0x4848C0,
            0x181870,
            0xA088B0,
            0x806890,
            0x806890,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0xA8A8F0,
            0xA0A0A8,
            0x909098,
            0x686880,
            0x282860,
            0xA848D0,
            0x601878,
            0x381870,
            0x200850,
            0x1898F0,
            0x1060C0,
            0x083888,
            0x6858A0,
            0x484878,
            0x181818,
        ]
    )

    @property
    def overworld_colours(self) -> SpritePalette:
        return SpritePalette(
            [
                0xF8F8F8,
                0xF0F090,
                0xD8D878,
                0xA0A058,
                0x403828,
                0xF868D0,
                0x902848,
                0x582038,
                0x300810,
                0x28E8F8,
                0x1890B8,
                0x105060,
                0xA08888,
                0x686848,
                0x181818,
            ]
        )


class Mokura(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xE0F878,
            0x90F090,
            0x78D878,
            0x58A058,
            0x283828,
            0x606060,
            0x404040,
            0x202020,
            0x300810,
            0x80A080,
            0x507050,
            0x204020,
            0x608860,
            0x486848,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8C0D8,
            0xA0B0F8,
            0x88A0D8,
            0x6070A0,
            0x282048,
            0x6848A8,
            0x482870,
            0x201030,
            0x300018,
            0x9070E8,
            0x585090,
            0x202830,
            0x6860A8,
            0x504880,
            0x181020,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x707C6D,
            0x487879,
            0x3C6C6D,
            0x2C505E,
            0x141C46,
            0x303062,
            0x202052,
            0x101042,
            0x18043A,
            0x405071,
            0x28385A,
            0x102042,
            0x304462,
            0x243456,
            0x0C0C3E,
        ]
    )
    name: str = "Mokura"


class Frog(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0x50C800,
            0x50A800,
            0x188800,
            0x004800,
            0x004000,
            0xC02068,
            0x902848,
            0x003800,
            0x001800,
            0x003800,
            0x001000,
            0x002800,
            0x006000,
            0x006800,
            0x000000,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0x608800,
            0x606800,
            0x005000,
            0x002000,
            0x001800,
            0xF80060,
            0xC00038,
            0x001000,
            0x000000,
            0x001000,
            0x000000,
            0x000000,
            0x003000,
            0x003000,
            0x000000,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x2E6A1E,
            0x2E5A1E,
            0x124A1E,
            0x052A1E,
            0x05261E,
            0x661652,
            0x4E1A42,
            0x05221E,
            0x05121E,
            0x05221E,
            0x050E1E,
            0x051A1E,
            0x05361E,
            0x053A1E,
            0x05051E,
        ]
    )
    name: str = "Frog"


class Palom(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF0E5D9,
            0xF0D7BF,
            0xEFBD8C,
            0xC7905A,
            0x403828,
            0xCE3939,
            0xAD1010,
            0x422110,
            0x30170A,
            0x78B820,
            0x6B8C21,
            0x526318,
            0xA17F5D,
            0x8F663F,
            0x400808,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0xF8E8F8,
            0xF8C8F8,
            0xD090B8,
            0x302840,
            0xD82868,
            0xB80008,
            0x300808,
            0x200000,
            0x70C030,
            0x609030,
            0x405820,
            0xA080C8,
            0x906080,
            0x300000,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x78749D,
            0x786C91,
            0x786079,
            0x64485E,
            0x201C46,
            0x681C4E,
            0x58083A,
            0x20103A,
            0x180C36,
            0x3C5C42,
            0x344842,
            0x28303E,
            0x504062,
            0x483452,
            0x200436,
        ]
    )
    name: str = "Palom"


class Porom(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF0E5D9,
            0xF0D7BF,
            0xEFBD8C,
            0xC7905A,
            0x403828,
            0x6B8C21,
            0x526318,
            0x422110,
            0x30170A,
            0xCE3939,
            0xAD1010,
            0x750B0B,
            0xA17F5D,
            0x8F663F,
            0x281800,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0xF8E8F8,
            0xF8C8F8,
            0xD090B8,
            0x302840,
            0x609030,
            0x405820,
            0x300808,
            0x200000,
            0xD82868,
            0xB80008,
            0x750B6C,
            0xA080C8,
            0x906080,
            0x300000,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x78749D,
            0x786C91,
            0x786079,
            0x64485E,
            0x201C46,
            0x344842,
            0x28303E,
            0x20103A,
            0x180C36,
            0x681C4E,
            0x58083A,
            0x3A0537,
            0x504062,
            0x483452,
            0x200436,
        ]
    )
    name: str = "Porom"


class Cloud(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0xF0F0F0,
            0xD8D8D8,
            0xA0A0A0,
            0x404040,
            0x6868F8,
            0x282890,
            0x000060,
            0x000048,
            0xD0D0D0,
            0x000070,
            0x6868F8,
            0x8888A0,
            0x484868,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xC0B0F8,
            0xB8A0F8,
            0xA090F8,
            0x6860B8,
            0x201030,
            0x3838F8,
            0x000098,
            0x000060,
            0x000038,
            0x9890F0,
            0x000070,
            0x3838F8,
            0x5850B8,
            0x202068,
            0x000000,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x8989B4,
            0x8585B0,
            0x7979A4,
            0x5D5D88,
            0x2D2D58,
            0x4141B4,
            0x212180,
            0x0D0D68,
            0x0D0D5C,
            0x7575A0,
            0x0D0D70,
            0x4141B4,
            0x515188,
            0x31316C,
            0x191944,
        ]
    )


class Stormy(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xE8E8F8,
            0xC8C8D8,
            0xB8B8C8,
            0x808090,
            0x484858,
            0x8060C8,
            0x502868,
            0x302078,
            0x101050,
            0xE0E840,
            0xC8A818,
            0x605030,
            0x8088C8,
            0x686888,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8A8F8,
            0xE098F8,
            0xD088F8,
            0x9060F8,
            0x5030A0,
            0x9048F8,
            0x5818C0,
            0x3010D8,
            0x100090,
            0xF8A870,
            0xE08020,
            0x683050,
            0x9060F8,
            0x7048F8,
            0x181020,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x7474AD,
            0x64649D,
            0x5C5C95,
            0x404079,
            0x24245E,
            0x403095,
            0x281465,
            0x18106D,
            0x08085A,
            0x707452,
            0x64543E,
            0x30284A,
            0x404495,
            0x343475,
            0x0C0C3E,
        ]
    )


class Light(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0xF0F0F0,
            0xD8D8D8,
            0xA0A0A0,
            0x404040,
            0xB8A0F8,
            0x6860F8,
            0x464050,
            0x101010,
            0x76ABEE,
            0x4480CA,
            0x3B5678,
            0x8888A0,
            0x686868,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8F8A0,
            0xF8F898,
            0xE0E888,
            0xA8B068,
            0x404028,
            0xC0B0A0,
            0x6868A0,
            0x484030,
            0x101008,
            0x78B898,
            0x408880,
            0x386048,
            0x889068,
            0x687040,
            0x181810,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x7C7CAD,
            0x7878A9,
            0x6C6C9D,
            0x505081,
            0x202052,
            0x5C50AD,
            0x3430AD,
            0x24205A,
            0x08083A,
            0x3C54A9,
            0x204095,
            0x1C2C6D,
            0x444481,
            0x343465,
            0x0C0C3E,
        ]
    )


class Water(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF8F8F8,
            0x70D0E0,
            0x58B8C8,
            0x388090,
            0x105878,
            0x6868D0,
            0x282848,
            0x382038,
            0x100810,
            0xE8E8F8,
            0x6868D0,
            0x282848,
            0x388090,
            0x186070,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xE0B8F8,
            0x5898E8,
            0x4088D0,
            0x205890,
            0x003070,
            0x5040D8,
            0x100840,
            0x200828,
            0x000000,
            0xD0A8F8,
            0x5040D8,
            0x100840,
            0x205890,
            0x004068,
            0x000008,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x8989B4,
            0x4575A8,
            0x39699C,
            0x294D80,
            0x153974,
            0x4141A0,
            0x21215C,
            0x291D54,
            0x151140,
            0x8181B4,
            0x4141A0,
            0x21215C,
            0x294D80,
            0x193D70,
            0x191944,
        ]
    )


class Red(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF8F0F8,
            0xF0D0E0,
            0xE0A0D8,
            0xA07088,
            0x403828,
            0xD83030,
            0x902828,
            0x582038,
            0x301010,
            0x804040,
            0x582020,
            0x180000,
            0xD08080,
            0x684888,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF8B0F8,
            0xF898F8,
            0xF870F8,
            0xB050F8,
            0x482048,
            0xF82050,
            0xA01848,
            0x601060,
            0x300018,
            0x902870,
            0x601030,
            0x180000,
            0xE860E8,
            0x7030F8,
            0x181020,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x7C78AD,
            0x7868A1,
            0x70509D,
            0x503875,
            0x201C46,
            0x6C184A,
            0x481446,
            0x2C104E,
            0x18083A,
            0x402052,
            0x2C1042,
            0x0C0032,
            0x684071,
            0x342475,
            0x0C0C3E,
        ]
    )


class Mint(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0xF0F8F0,
            0xE8F0E8,
            0xC0E8B8,
            0xA0C888,
            0x506850,
            0x70B878,
            0x40B850,
            0x202858,
            0x080830,
            0x0070A8,
            0x005080,
            0x003860,
            0x98D8A0,
            0x506848,
            0x181818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0xF0F0F0,
            0xE8F0E8,
            0xD0D0D0,
            0xB0A8A8,
            0x586058,
            0x909098,
            0x708080,
            0x382858,
            0x180830,
            0x4838A8,
            0x382880,
            0x282060,
            0xB0B8B8,
            0x585858,
            0x181818,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x7878A8,
            0x7078A8,
            0x607090,
            0x506078,
            0x283058,
            0x385870,
            0x205858,
            0x101060,
            0x000048,
            0x003888,
            0x002870,
            0x001860,
            0x486880,
            0x283058,
            0x080840,
        ]
    )


class Demon(MallowPaletteSet):
    default_colours: SpritePalette = SpritePalette(
        [
            0x403038,
            0x283030,
            0x282028,
            0x201018,
            0x182018,
            0x081010,
            0x182020,
            0x182020,
            0x300810,
            0x000000,
            0x100000,
            0x101810,
            0x181810,
            0x181818,
            0xF81818,
        ]
    )
    poison_colours: SpritePalette = SpritePalette(
        [
            0x485028,
            0x305028,
            0x303828,
            0x282820,
            0x283820,
            0x182818,
            0x283820,
            0x283820,
            0x381818,
            0x101010,
            0x201010,
            0x202818,
            0x282818,
            0x282820,
            0xE02820,
        ]
    )
    underwater_colours: SpritePalette = SpritePalette(
        [
            0x20184D,
            0x141849,
            0x141045,
            0x10083D,
            0x0C103D,
            0x040839,
            0x0C1041,
            0x180439,
            0x000031,
            0x080031,
            0x080C39,
            0x0C0C39,
            0x0C0C3D,
            0x7C0C3D,
            0x1818F8,
        ]
    )
