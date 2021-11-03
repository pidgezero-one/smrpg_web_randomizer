from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline
from randomizer.data.palettes import Sprite, ImagePack, AnimationPack, AnimationPackProperties, AnimationSequence, AnimationSequenceFrame, Mold, Tile, Clone


UNCOMPRESSED_GFX_START = 0x280000
UNCOMPRESSED_GFX_END = 0x330000

SPRITE_PTRS_START = 0x250000
SPRITE_PTRS_END = 0x251000

IMAGE_PTRS_START = 0x251800
IMAGE_PTRS_END = 0x252000

ANIMATION_PTRS_START = 0x252000
ANIMATION_PTRS_END = 0x252C00

ANIMATION_DATA_BANK_1_START = 0x259000
ANIMATION_DATA_BANK_1_END = 0x280000

ANIMATION_DATA_BANK_2_START = 0x360000
ANIMATION_DATA_BANK_2_END = 0x370000

PALETTE_OFFSET = 0x253000

DEBUG_INDEX = 3

class Sprites:
    def __init__(self):
        self.output = []

        # Sprite - high level container consisting of 1 image and 1 animation
        # Image - contains a palette pointer and a graphics offset
        # Animation - image about how to arrange the graphics at the offset in the Image

    def assemble_from_tables(sprites, images, animations):

        sprite_data = []
        image_data = []
        animation_pointers = []
        animation_data_bank_1 = []
        animation_data_bank_2 = []

        used_animations = []

        for sprite in sprites:
            assert sprite.image_num <= 0x1FF
            assert sprite.palette_offset <= 7
            sprite_data.append(sprite.image_num & 0xFF)
            sprite_data.append(((sprite.image_num >> 8) & 0x01) + (sprite.palette_offset << 1) + (sprite.unknown << 4))
            assert sprite.animation_num <= 0xFFFF
            sprite_data.append(sprite.animation_num & 0xFF)
            sprite_data.append((sprite.animation_num >> 8) & 0xFF)
            if sprite.animation_num not in used_animations:
                used_animations.append(sprite.animation_num)

        for image in images:
            bank = ((image.graphics_pointer - UNCOMPRESSED_GFX_START) >> 16) & 0x0F
            gfx_short = image.graphics_pointer & 0xFFF0
            assert gfx_short <= 0xFFFF
            image_data.append((gfx_short & 0xF0) + bank)
            image_data.append(gfx_short >> 8)
            palette_ptr = image.palette_pointer - PALETTE_OFFSET + 0x3000
            assert palette_ptr <= 0xFFFF
            image_data.append(palette_ptr & 0xFF)
            image_data.append(palette_ptr >> 8)

        anim_bank = ANIMATION_DATA_BANK_1_START

        for anim_id, animation in enumerate(animations):

            if anim_id not in used_animations:
                animation = AnimationPack(anim_id, unknown=0x0002, properties=AnimationPackProperties(vram_size=2048,
                    molds=[
                        Mold(0, gridplane=False,
                            tiles=[]
                        ),
                    ],
                    sequences=[
                        AnimationSequence(
                            frames=[]
                        ),
                    ]
                ))

            length_bytes = bytearray([])
            sequence_offset = bytearray([0x0C, 0x00])
            mold_offset = bytearray([])
            num_sequences = len(animation.properties.sequences)
            num_molds = len(animation.properties.molds)
            assert num_molds <= 32
            assert num_sequences <= 32
            count_bytes = bytearray([num_sequences, num_molds])
            vram = animation.properties.vram_size >> 8
            misc_bytes = bytearray([vram & 0xFF, (vram >> 8) & 0xFF, 0x02, 0x00])
            sequence_ptrs = bytearray([])
            sequence_bytes = bytearray([])
            mold_ptrs = bytearray([])
            mold_bytes = bytearray([])

            for sequence in animation.properties.sequences:
                this_sequence_offset = 0x0C + (len(animation.properties.sequences) + 1) * 2 + len(sequence_bytes)
                assert this_sequence_offset <= 0xFFFF
                if len(sequence.frames) == 0:
                    sequence_ptrs.extend([0xFF, 0xFF])
                else:
                    sequence_ptrs.append(this_sequence_offset & 0xFF)
                    sequence_ptrs.append(this_sequence_offset >> 8)
                    for frame in sequence.frames:
                        sequence_bytes.append(frame.duration)
                        sequence_bytes.append(frame.mold_id)
                    sequence_bytes.append(0)
            sequence_ptrs.extend([0, 0])

            mold_offset_short = 0x0C + len(sequence_ptrs) + len(sequence_bytes)
            mold_offset.append(mold_offset_short & 0xFF)
            mold_offset.append((mold_offset_short >> 8) & 0xFF)
            for mold_index, mold in enumerate(animation.properties.molds):
                this_mold_offset = 0x0C + len(sequence_ptrs) + len(sequence_bytes) + (len(animation.properties.molds) + 1) * 2 + len(mold_bytes)
                assert this_mold_offset <= 0x7FFF
                #print(anim_id, mold_index, hex(anim_bank + this_mold_offset))
                animation.properties.molds[mold_index].offset = this_mold_offset
                if mold.gridplane:
                    this_mold_offset += (0x80 << 8)
                if len(mold.tiles) > 0:
                    mold_ptrs.append(this_mold_offset & 0xFF)
                    mold_ptrs.append((this_mold_offset >> 8) & 0xFF)
                    this_mold_bytes = bytearray([])
                    if mold.gridplane:
                        for tile_index, tile in enumerate(mold.tiles):
                            tile_bytes = bytearray([])
                            animation.properties.molds[mold_index].tiles[tile_index].offset = this_mold_offset + len(this_mold_bytes)
                            byte_1 = (tile.format & 0x03) + (tile.is_16bit << 3) + (tile.y_plus << 4) + (tile.y_minus << 5) + (tile.mirror << 6) + (tile.invert << 7)
                            tile_bytes.append(byte_1)
                            if tile.is_16bit:
                                subtile_short = 0
                                for i, subtile_byte in enumerate(tile.subtile_bytes):
                                    if subtile_byte >= 0x100:
                                        subtile_short += (1 << i)
                                tile_bytes.append(subtile_short & 0xFF)
                                tile_bytes.append((subtile_short >> 8) & 0xFF)
                            for subtile_byte in tile.subtile_bytes:
                                tile_bytes.append(subtile_byte & 0xFF)
                            this_mold_bytes += tile_bytes
                    else:
                        for tile_index, tile in enumerate(mold.tiles):
                            tile_bytes = bytearray([])
                            animation.properties.molds[mold_index].tiles[tile_index].offset = this_mold_offset + len(this_mold_bytes)
                            found_clone = False
                            if tile.is_clone:
                                byte_1 = (0x02) + (tile.mirror << 2) + (tile.invert << 3)
                                ct = tile.tiles[0]
                                found_offset = 0
                                tmp = mold_index
                                while tmp >= 0:
                                    m = animation.properties.molds[tmp]
                                    if not found_clone:
                                        for ct_index, compare_tile in enumerate(m.tiles):
                                            if not found_clone and not compare_tile.is_clone:
                                                if compare_tile.mirror == ct.mirror and compare_tile.invert == ct.invert and compare_tile.subtile_bytes == ct.subtile_bytes:
                                                    confirm_tile = True
                                                    conf_i = 0
                                                    while conf_i < len(tile.tiles) and confirm_tile:
                                                        tmp_tile_1 = tile.tiles[conf_i]
                                                        if ct_index + conf_i >= len(m.tiles):
                                                            confirm_tile = False
                                                            continue
                                                        tmp_tile_2 = m.tiles[ct_index + conf_i]
                                                        if tmp_tile_2.is_clone:
                                                            confirm_tile = False
                                                            continue
                                                        elif tmp_tile_1.mirror != tmp_tile_2.mirror or tmp_tile_1.invert != tmp_tile_2.invert or tmp_tile_1.subtile_bytes != tmp_tile_2.subtile_bytes:
                                                            confirm_tile = False
                                                            continue
                                                        conf_i += 1
                                                    if confirm_tile:
                                                        found_clone = True
                                                        found_offset = compare_tile.offset
                                    tmp -= 1
                                if found_clone:
                                    byte_1 += (len(tile.tiles) << 4)
                                    tile_bytes.append(byte_1)
                                    tile_bytes.append(tile.y)
                                    tile_bytes.append(tile.x)
                                    tile_bytes.append(found_offset & 0xFF)
                                    tile_bytes.append((found_offset >> 8) & 0x7F)
                                    this_mold_bytes += tile_bytes
                                else:
                                    raise Exception("no clones found for anim %i mold %i" % (anim_id, mold_index))
                            else:
                                byte_lower_1 = (tile.format & 0x03) + (tile.mirror << 2) + (tile.invert << 3)
                                byte_upper_1 = 0
                                for i, subtile in enumerate(tile.subtile_bytes):
                                    if subtile != 0:
                                        byte_upper_1 += (1 << (3-i))
                                tile_bytes.append(byte_lower_1 + (byte_upper_1 << 4))
                                tile_bytes.append(tile.y ^ 0x80)
                                tile_bytes.append(tile.x ^ 0x80)
                                for i, subtile_byte in enumerate(tile.subtile_bytes):
                                    if subtile_byte > 0:
                                        tile_bytes.append(subtile_byte & 0xFF)
                                        if subtile_byte > 255:
                                            animations[anim_id].properties.molds[mold_index].tiles[tile_index].format = 1
                                            tile.format = 1
                                        if tile.format == 1:
                                            tile_bytes.append((subtile_byte >> 8) & 0x01)
                                this_mold_bytes += tile_bytes
                        this_mold_bytes.append(0)
                    mold_bytes += this_mold_bytes
                else:
                    mold_ptrs.extend([0xFF, 0xFF])
                    this_mold_bytes = bytearray([0x00])
                    mold_bytes += this_mold_bytes
            mold_ptrs.extend([0, 0])

            length_bytes_short = 2 + len(sequence_offset) + len(mold_offset) + len(count_bytes) + len(misc_bytes) + len(sequence_ptrs) + len(sequence_bytes) + len(mold_ptrs) + len(mold_bytes)
            length_bytes = bytearray([length_bytes_short & 0xFF, (length_bytes_short >> 8) & 0xFF])
            finished_bytes = length_bytes + sequence_offset + mold_offset + count_bytes + misc_bytes + sequence_ptrs + sequence_bytes + mold_ptrs + mold_bytes

            if anim_bank == ANIMATION_DATA_BANK_1_START and anim_bank + len(animation_data_bank_1) + len(finished_bytes) >= ANIMATION_DATA_BANK_1_END:
                anim_bank = ANIMATION_DATA_BANK_2_START

            if anim_bank == ANIMATION_DATA_BANK_1_START:
                anim_ptr = 0xC00000 + len(animation_data_bank_1) + anim_bank
                animation_data_bank_1.extend(finished_bytes)
            else: 
                anim_ptr = 0xC00000 + len(animation_data_bank_2) + anim_bank
                animation_data_bank_2.extend(finished_bytes)
            animation_pointers.extend([anim_ptr & 0xFF, (anim_ptr >> 8) & 0xFF, (anim_ptr >> 16) & 0xFF])


        sprite_data += bytearray([0] * (SPRITE_PTRS_END - SPRITE_PTRS_START - len(sprite_data)))
        image_data += bytearray([0] * (IMAGE_PTRS_END - IMAGE_PTRS_START - len(image_data)))
        animation_pointers += bytearray([0] * (ANIMATION_PTRS_END - ANIMATION_PTRS_START - len(animation_pointers)))
        animation_data_bank_1 += bytearray([0] * (ANIMATION_DATA_BANK_1_END - ANIMATION_DATA_BANK_1_START - len(animation_data_bank_1)))
        animation_data_bank_2 += bytearray([0] * (ANIMATION_DATA_BANK_2_END - ANIMATION_DATA_BANK_2_START - len(animation_data_bank_2)))
        
        return bytearray(sprite_data), bytearray(image_data), bytearray(animation_pointers), bytearray(animation_data_bank_1), bytearray(animation_data_bank_2)