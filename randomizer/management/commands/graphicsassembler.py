from django.core.management.base import BaseCommand
from randomizer.logic.sprites import Sprites 
from randomizer.data.graphics import sprites, images, animations
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short, writeline, bit_bool_from_num
from randomizer.data.sprites.objects.sprites import sprites as commonsprites
from randomizer.data.sprites.insertions.geno.sprites import sprites as genosprites
from randomizer.data.sprites.insertions.toadstool.sprites import sprites as toadstoolsprites
from randomizer.data.sprites.insertions.mallow.sprites import sprites as mallowsprites
from randomizer.data.sprites.insertions.bowser.sprites import sprites as bowsersprites

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-w', '--whitespace', action="store_true",
                            help='If set, adds whitespace around specific few sprites')

    def handle(self, *args, **options):
        whitespace = options['whitespace']
        # sprite_data, image_data, animation_pointers, animation_data_bank_1, animation_data_bank_2 = Sprites.assemble_from_tables(sprites, images, animations)

        # f = open(f'write_to_0x250000.img', 'wb')
        # f.write(sprite_data)
        # f.close()  

        # f = open(f'write_to_0x251800.img', 'wb')
        # f.write(image_data + animation_pointers)
        # f.close() 

        # f = open(f'write_to_0x259000.img', 'wb')
        # f.write(animation_data_bank_1)
        # f.close()

        # f = open(f'write_to_0x360000.img', 'wb')
        # f.write(animation_data_bank_2)
        # f.close()

        # for gsi, gs in enumerate(genosprites):
        #     if gs is not None:
        #         commonsprites[gsi] = gs

        # for gsi, gs in enumerate(toadstoolsprites):
        #     if gs is not None:
        #         commonsprites[gsi] = gs

        # for gsi, gs in enumerate(mallowsprites):
        #     if gs is not None:
        #         commonsprites[gsi] = gs

        # for gsi, gs in enumerate(bowsersprites):
        #     if gs is not None:
        #         commonsprites[gsi] = gs

        sprite_data, image_data, animation_pointers, animation_data, tiles = Sprites.assemble_from_tables(commonsprites, whitespace)

        f = open(f'write_to_0x250000.img', 'wb')
        f.write(sprite_data)
        f.close()  

        f = open(f'write_to_0x251800.img', 'wb')
        f.write(image_data + animation_pointers)
        f.close() 

        for animation_offset, animation in animation_data:
            f = open('write_to_0x%06x.img' % animation_offset, 'wb')
            f.write(animation)
            f.close()

        for tileset_offset, tileset in tiles:
            f = open('write_to_0x%06x.img' % tileset_offset, 'wb')
            f.write(tileset)
            f.close()