from django.core.management.base import BaseCommand
from randomizer.data.palettes import Sprite, ImagePack, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline
import string, random

TOP_LEVEL_SPRITE_OFFSET = 0x250000
TOP_LEVEL_SPRITE_LENGTH = 0x1000

IMAGE_PACK_INFO_OFFSET = 0x251800
IMAGE_PACK_INFO_LENGTH = 0x800

ANIMATION_PACK_POINTERS_OFFSET = 0x252000
ANIMATION_PACK_POINTERS_LENGTH = 0xC00

TILES_START = 0x280000
TILES_END = 0x330000

PALETTE_OFFSET = 0x253000

def get_animation_pack_data_offset_from_third_byte(short, b):
    return ((b - 0xC0) << 16) + short

alphabet = string.ascii_lowercase + string.digits
def random_tile_id():
    return ''.join(random.choices(alphabet, k=8))

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

        parser.add_argument('-d', '--debug', action="store_true",
                            help='If set, dumps to a gitignored folder instead of overwriting the scripts sourced by SMRPG Randomizer')

    def handle(self, *args, **options):
        global rom
        rom = bytearray(open(options['rom'], 'rb').read())

        sprites = []
        images = []
        packs = []
        all_tiles = []
        tile_ids = []

        for _, offset in enumerate(range(TILES_START, TILES_END, 0x20)):
            tile = rom[offset:offset+0x20]
            dupe = False
            for t in all_tiles:
                if t[1] == tile:
                    dupe = True
            if not dupe:
                tile_id = random_tile_id()
                while tile_id in tile_ids:
                    tile_id = random_tile_id()
                all_tiles.append((tile_id, tile))


        for index, offset in enumerate(range(TOP_LEVEL_SPRITE_OFFSET, TOP_LEVEL_SPRITE_OFFSET + TOP_LEVEL_SPRITE_LENGTH, 4)):
            if shortify(rom, offset+2) > 443:
                sprite = Sprite(index, 0, 0, 0, 0)
            else:
                img = shortify(rom, offset) & 0x1FF
                pal_off = (rom[offset+1] & 0x0E) >> 1
                unknown = (rom[offset+1] >> 4)
                sprite = Sprite(index, img, shortify(rom, offset+2), pal_off, unknown)
            sprites.append(sprite)
            # print(hex(offset), index, hex(rom[offset+1]), unknown)

        for index, offset in enumerate(range(IMAGE_PACK_INFO_OFFSET, IMAGE_PACK_INFO_OFFSET + IMAGE_PACK_INFO_LENGTH, 4)):
            gfx_ptr_short = shortify(rom, offset)
            bank = ((rom[offset] & 0x0F) << 16) + 0x280000
            gfx_ptr = (gfx_ptr_short & 0xFFF0) + bank
            images.append(ImagePack(index, gfx_ptr, 0x250000 + shortify(rom, offset+2)))


        for index, property_offset_ptr_offset in enumerate(range(ANIMATION_PACK_POINTERS_OFFSET, ANIMATION_PACK_POINTERS_OFFSET + ANIMATION_PACK_POINTERS_LENGTH, 3)):
            #if index > 316:
            if index > 465:
                break
            property_offset_ptr_offset = ANIMATION_PACK_POINTERS_OFFSET + (index * 3)
            property_offset = get_animation_pack_data_offset_from_third_byte(shortify(rom, property_offset_ptr_offset), rom[property_offset_ptr_offset + 2])
            if property_offset == -0xc00000:
                continue
            pack = AnimationPack(index)

            molds = []
            sequences = []

            length = shortify(rom, property_offset)
            sequence_packet_ptr_relative_offset = shortify(rom, property_offset+2)
            mold_packet_ptr_relative_offset = shortify(rom, property_offset+4)
            sequence_count = rom[property_offset+6]
            mold_count = rom[property_offset+7]
            vram_size = (shortify(rom, property_offset+8) << 8)
            unknown = shortify(rom, property_offset+10)
            pack.length = length
            pack.unknown = unknown

            for i in range(0, sequence_count):
                sequence_offset = property_offset + sequence_packet_ptr_relative_offset + i * 2
                frames = []
                if shortify(rom, sequence_offset) != 0xFFFF:
                    relative_offset = shortify(rom, sequence_offset) & 0x7FFF
                    offset = relative_offset + property_offset
                    while rom[offset] != 0 and relative_offset != 0x7FFF:
                        frames.append(AnimationSequenceFrame(rom[offset], rom[offset+1]))
                        relative_offset += 2
                        offset = relative_offset + property_offset
                sequences.append(AnimationSequence(frames))

            for i in range(0, mold_count):
                mold_offset = property_offset + mold_packet_ptr_relative_offset + i * 2
                relative_offset = mold_offset
                if shortify(rom, relative_offset) != 0xFFFF:
                    gridplane = (rom[relative_offset+1] & 0x80) == 0x80
                    tile_packet_pointer = shortify(rom, relative_offset) & 0x7FFF
                    relative_offset = tile_packet_pointer + property_offset
                    if gridplane:
                        tile_length = 0
                        format = rom[relative_offset]
                        relative_offset += 1
                        is_16bit = (format & 0x08) == 0x08
                        y_plus = 1 if (format & 0x10) == 0x10 else 0
                        y_minus = 1 if (format & 0x20) == 0x20 else 0
                        mirror = (format & 0x40) == 0x40
                        invert = (format & 0x80) == 0x80
                        tile_length += 1
                        format &= 3
                        if is_16bit:
                            subtiles_16bit = shortify(rom, relative_offset)
                            relative_offset += 2
                            tile_length += 2
                        else:
                            subtiles_16bit = 0
                        copy_length = 9
                        if format == 1 or format == 2:
                            copy_length = 12
                        elif format == 3:
                            copy_length = 16
                        tile_length += copy_length
                        subtile_bytes = [1]*copy_length
                        subtile_bytes[0:copy_length] = rom[relative_offset:relative_offset+copy_length]
                        if is_16bit:
                            for j in range(0, copy_length):
                                if (subtiles_16bit & (2 ** j)) == (2 ** j):
                                    subtile_bytes[j] += 0x100
                        molds.append(Mold(i, gridplane, [Tile(mirror=mirror, invert=invert, format=format, length=tile_length, subtile_bytes=subtile_bytes, is_16bit=is_16bit, y_plus=y_plus, y_minus=y_minus, is_clone=False)]))
                    else:
                        tiles = []
                        while rom[relative_offset] != 0:
                            temp_offset = relative_offset
                            is_clone = False
                            if (rom[relative_offset] & 0x03) == 2:
                                is_clone = True
                                y = rom[relative_offset+1]
                                x = rom[relative_offset+2]
                                mirror = (rom[relative_offset] & 0x04) == 0x04
                                invert = (rom[relative_offset] & 0x08) == 0x08
                                within_buffer_offset = shortify(rom, relative_offset+3)
                                if within_buffer_offset >= 0x7FFF:
                                    raise Exception("bad mold offset at %06x, mold %i of animation %i" % (relative_offset, i, index))
                                relative_offset = within_buffer_offset + property_offset
                                clone_tiles = []
                                for _ in range(0, rom[temp_offset] >> 4):
                                    if within_buffer_offset > length:
                                        raise Exception("bad data at %06x, mold %i of animation %i: 0x%04x is larger than length %i" % (relative_offset, i, index, relative_offset - property_offset, length))
                                    tile_length = 0
                                    if (rom[relative_offset] & 0x03) == 2:
                                        raise Exception("bad tile data at %06x, mold %i of animation %i" % (relative_offset, i, index))
                                    else:
                                        temp_offset_2 = relative_offset
                                        format = rom[relative_offset] & 0x0F
                                        mi = (format & 0x04) == 0x04
                                        inv = (format & 0x08) == 0x08
                                        format &= 3
                                        quadrants = [False] * 4
                                        for j in range (0, 4):
                                            div = 128 // (2 ** j)
                                            quadrants[j] = (rom[relative_offset] & div) == div
                                        relative_offset += 1
                                        tile_length += 1
                                        tile_y = (rom[relative_offset] ^ 0x80)# + y
                                        relative_offset += 1
                                        tile_length += 1
                                        tile_x = (rom[relative_offset] ^ 0x80)# + x
                                        relative_offset += 1
                                        tile_length += 1
                                        subtile_bytes = [0]*4
                                        for j in range(0, 4):
                                            if quadrants[j]:
                                                if format == 1:
                                                    subtile_bytes[j] = shortify(rom, relative_offset) & 0x1FF
                                                    relative_offset += 1
                                                    tile_length += 1
                                                else:
                                                    subtile_bytes[j] = rom[relative_offset]
                                                relative_offset += 1
                                                tile_length += 1
                                        relative_offset = temp_offset_2 + tile_length
                                        clone_tiles.append(Tile(mirror=mi, invert=inv, format=format, length=tile_length, subtile_bytes=subtile_bytes, x=tile_x, y=tile_y, is_clone=is_clone))    
                                tiles.append(Clone(x, y, mirror, invert, clone_tiles))
                                relative_offset = temp_offset + 5
                            else:
                                tile_length = 0
                                format = rom[relative_offset] & 0x0F
                                mirror = (format & 0x04) == 0x04
                                invert = (format & 0x08) == 0x08
                                format &= 3
                                quadrants = [False] * 4
                                for j in range (0, 4):
                                    quadrants[j] = (rom[relative_offset] & (128 // (2 ** j))) == (128 // (2 ** j))
                                relative_offset += 1
                                tile_length += 1
                                tile_y = (rom[relative_offset] ^ 0x80)
                                relative_offset += 1
                                tile_length += 1
                                tile_x = (rom[relative_offset] ^ 0x80)
                                relative_offset += 1
                                tile_length += 1
                                subtile_bytes = [0]*4
                                for j in range(0, 4):
                                    if quadrants[j]:
                                        if format == 1:
                                            subtile_bytes[j] = shortify(rom, relative_offset) & 0x1FF
                                            relative_offset += 1
                                            tile_length += 1
                                        else:
                                            subtile_bytes[j] = rom[relative_offset]
                                        relative_offset += 1
                                        tile_length += 1
                                tiles.append(Tile(mirror=mirror, invert=invert, format=format, length=tile_length, subtile_bytes=subtile_bytes, x=tile_x, y=tile_y, is_clone=is_clone))    
                                relative_offset = temp_offset + tile_length
                        molds.append(Mold(i, gridplane, tiles))
                else:
                    molds.append(Mold(i, False, []))

            pack.properties = AnimationPackProperties(sequences, molds, vram_size)
            packs.append(pack)

        # write
        dest = 'randomizer/data/sprites/tiles.py'
        file = open(dest, "w")
        writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
        writeline(file, '# Run the following command if you need to rebuild the table')
        writeline(file, '# python manage.py graphicsdisassembler --rom ROM')
        writeline(file, 'tiles = [')
        for t in all_tiles:
            writeline(file, '''    ("%s", %r),''' % (t[0], t[1]))
        writeline(file, ']\n\n')
        file.close()

        dest = 'randomizer/data/sprites/sprite_containers.py'
        file = open(dest, "w")
        writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
        writeline(file, '# Run the following command if you need to rebuild the table')
        writeline(file, '# python manage.py graphicsdisassembler --rom ROM')
        writeline(file, 'from randomizer.data.palettes import Sprite')
        writeline(file, 'sprites = [')
        for s in sprites:
            writeline(file, "    Sprite(%i, image_num=%i, animation_num=%i, palette_offset=%i, unknown=%i)," % (s.index, s.image_num, s.animation_num, s.palette_offset, s.unknown))
        writeline(file, ']\n\n')
        file.close()

        dest = 'randomizer/data/sprites/image_packs.py'
        file = open(dest, "w")
        writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
        writeline(file, '# Run the following command if you need to rebuild the table')
        writeline(file, '# python manage.py graphicsdisassembler --rom ROM')
        writeline(file, 'from randomizer.data.palettes import ImagePack')
        writeline(file, 'images = [')
        for i in images:
            writeline(file, "    ImagePack(%i, graphics_pointer=0x%06x, palette_pointer=0x%06x)," % (i.index, i.graphics_pointer, i.palette_pointer))
        writeline(file, ']\n\n')
        file.close()

        dest = 'randomizer/data/sprites/animation_packs.py'
        file = open(dest, "w")
        writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
        writeline(file, '# Run the following command if you need to rebuild the table')
        writeline(file, '# python manage.py graphicsdisassembler --rom ROM')
        writeline(file, 'from randomizer.data.palettes import AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone')
        writeline(file, 'animations= [')
        for p in packs:
            writeline(file, "    AnimationPack(%i, length=%i, unknown=0x%04x," % (p.index, p.length, p.unknown))
            writeline(file, "        properties=AnimationPackProperties(vram_size=%i," % p.properties.vram_size)
            writeline(file, "            molds=[")
            for m in p.properties.molds:
                writeline(file, "                Mold(%i, gridplane=%r," % (m.index, m.gridplane))
                writeline(file, "                    tiles=[")
                for t in m.tiles:
                    if not t.is_clone:
                        writeline(file, "                        Tile(mirror=%r, invert=%r, format=%i, length=%i, subtile_bytes=%r, is_16bit=%r, y_plus=%i, y_minus=%i, x=%i, y=%i)," % (t.mirror, t.invert, t.format, t.length, t.subtile_bytes, t.is_16bit, t.y_plus, t.y_minus, t.x, t.y))
                    else:
                        writeline(file, "                        Clone(mirror=%r, invert=%r, x=%i, y=%i, tiles=[" % (t.mirror, t.invert, t.x, t.y))
                        for ct in t.tiles:
                            writeline(file, "                            Tile(mirror=%r, invert=%r, format=%i, length=%i, subtile_bytes=%r, is_16bit=%r, y_plus=%i, y_minus=%i, x=%i, y=%i)," % (ct.mirror, ct.invert, ct.format, ct.length, ct.subtile_bytes, ct.is_16bit, ct.y_plus, ct.y_minus, ct.x, ct.y))
                        writeline(file, "                        ]),")
                writeline(file, "                    ]")
                writeline(file, "                ),")
            writeline(file, "            ],")
            writeline(file, "            sequences=[")
            for s in p.properties.sequences:
                writeline(file, "                AnimationSequence(")
                writeline(file, "                    frames=[")
                for f in s.frames:
                    writeline(file, "                        AnimationSequenceFrame(duration=%i, mold_id=%i)," % (f.duration, f.mold_id))
                writeline(file, "                    ]")
                writeline(file, "                ),")
            writeline(file, "            ]")
            writeline(file, "        )")
            writeline(file, "    ),")
        writeline(file, ']')
        file.close()

        used_images = [False] * 512
        used_packs = [False] * 1024
        used_palettes = [False] * 819

        for index, s in enumerate(sprites):
            palette_offset = s.palette_offset
            unknown = s.unknown
            i = images[s.image_num]
            if s.animation_num >= len(packs):
                break
            p = packs[s.animation_num]

            palette_id_original = ((i.palette_pointer - 0x253000) // 30)
            palette_id = palette_id_original + palette_offset
            used_palettes[palette_id] = True

            used_images[s.image_num] = True

            used_packs[s.animation_num] = True

            gfx_offset = i.graphics_pointer


            dest = 'randomizer/data/sprites/wip/sprite_%i.py' % index
            file = open(dest, "w")
            writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
            writeline(file, '# Run the following command if you need to rebuild the table')
            writeline(file, '# python manage.py graphicsdisassembler --rom ROM')
            writeline(file, 'from randomizer.data.palettes import CompleteSprite, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone')
            writeline(file, 'sprite = CompleteSprite(')
            writeline(file, "    animation=AnimationPack(%i, length=%i, unknown=0x%04x," % (p.index, p.length, p.unknown))
            writeline(file, "        properties=AnimationPackProperties(vram_size=%i," % p.properties.vram_size)
            writeline(file, "            molds=[")
            for m in p.properties.molds:
                writeline(file, "                Mold(%i, gridplane=%r," % (m.index, m.gridplane))
                writeline(file, "                    tiles=[")
                for t in m.tiles:
                    if not t.is_clone:
                        writeline(file, "                        Tile(mirror=%r, invert=%r, format=%i, length=%i, subtile_bytes=[" % (t.mirror, t.invert, t.format, t.length))
                        for sb in t.subtile_bytes:
                            if sb == 0:
                                writeline(file, "                            None,")
                            else:
                                sb_offset = gfx_offset + (0x20 * (sb - 1))
                                writeline(file, "                            %r," % rom[sb_offset:sb_offset+0x20])
                        writeline(file, "                        ], is_16bit=%r, y_plus=%i, y_minus=%i, x=%i, y=%i)," % (t.is_16bit, t.y_plus, t.y_minus, t.x, t.y))
                    else:
                        for subt in t.tiles:
                            writeline(file, "                        Tile(mirror=%r, invert=%r, format=%i, length=%i, subtile_bytes=[" % (subt.mirror, subt.invert, subt.format, subt.length))
                            for sb in subt.subtile_bytes:
                                if sb == 0:
                                    writeline(file, "                            None,")
                                else:
                                    sb_offset = gfx_offset + (0x20 * (sb - 1))
                                    writeline(file, "                            %r," % rom[sb_offset:sb_offset+0x20])
                            writeline(file, "                        ], is_16bit=%r, y_plus=%i, y_minus=%i, x=%i, y=%i)," % (subt.is_16bit, subt.y_plus, subt.y_minus, t.x + subt.x, t.y + subt.y))
                writeline(file, "                    ]")
                writeline(file, "                ),")
            writeline(file, "            ],")
            writeline(file, "            sequences=[")
            for s in p.properties.sequences:
                writeline(file, "                AnimationSequence(")
                writeline(file, "                    frames=[")
                for f in s.frames:
                    writeline(file, "                        AnimationSequenceFrame(duration=%i, mold_id=%i)," % (f.duration, f.mold_id))
                writeline(file, "                    ]")
                writeline(file, "                ),")
            writeline(file, "            ]")
            writeline(file, "        )")
            writeline(file, "    ),")
            writeline(file, "    palette_id=%i," % palette_id_original)
            writeline(file, "    palette_offset=%i," % palette_offset)
            writeline(file, "    unknown_num=%i" % unknown)
            writeline(file, ')')
            file.close()

        
        file = open("randomizer/data/sprites/wip/sprites.py", "w", encoding='utf-8')
        writeline(file, '# AUTOGENERATED DO NOT EDIT!!')
        writeline(file, '# Run the following command if you need to rebuild the table')
        writeline(file, '# python manage.py graphicsdisassembler --rom ROM')
        for i in range(len(sprites)):
            writeline(
                file, 'from randomizer.data.sprites.objects.sprite_%i import sprite as sprite_%i' % (i, i))
        writeline(file, 'sprites = [None]*%i' % len(sprites))
        for i in range(len(sprites)):
            writeline(file, 'sprites[%i] = sprite_%i' % (i, i))
        file.close()


        for arr in [used_images, used_packs, used_palettes]:
            print([ind for ind, x in enumerate(arr) if not x])


