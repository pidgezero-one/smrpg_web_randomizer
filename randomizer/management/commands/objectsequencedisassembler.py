from django.core.management.base import BaseCommand
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short
from randomizer.data.objectsequencetables import sequence_speed_table, _0x08_flags, _0x0A_flags, _0x10_flags

start = 0x210800
end = 0x21BADE

sequence_lens = [
    1,  1,  1,  1,  1,  1,  1,  1,    3,  1,  2,  2,  2,  2,  2,  1,
    2,  2,  2,  2,  2,  1,  1,  1,    1,  1,  1,  1,  1,  1,  1,  1,
    2,  1,  1,  2,  5,  5,  16, 16,   16, 2,  1,  5,  3,  3,  3,  7,
    3,  3,  3,  3,  2,  3,  1,  1,    1,  1,  6,  6,  5,  3,  5,  4,
    1,  1,  1,  1,  1,  1,  1,  1,    1,  1,  1,  1,  1,  1,  1,  1,
    2,  2,  2,  2,  2,  2,  2,  2,    2,  1,  2,  2,  1,  1,  1,  1,
    2,  2,  2,  2,  2,  2,  2,  2,    2,  2,  2,  2,  1,  1,  1,  1,  
    1,  1,  1,  1,  1,  1,  1,  1,    1,  1,  1,  2,  1,  1,  3,  3,
    3,  3,  3,  3,  3,  1,  1,  2,    1,  1,  1,  1,  1,  1,  1,  1,
    4,  4,  4,  4,  4,  2,  2,  2,    1,  1,  1,  1,  2,  3,  3,  3,
    2,  2,  2,  1,  2,  2,  2,  1,    3,  3,  2,  2,  3,  3,  1,  1,
    4,  4,  2,  2,  2,  2,  3,  4,    2,  2,  2,  2,  3,  3,  1,  1,
    3,  2,  4,  1,  2,  2,  2,  2,    2,  2,  1,  1,  1,  1,  1,  1,
    3,  1,  3,  3,  2,  1,  2,  1,    4,  4,  4,  3,  4,  4,  4,  3,
    5,  5,  5,  5,  6,  6,  5,  5,    3,  5,  3,  3,  3,  3,  3,  3,
    2,  3,  3,  3,  1,  1,  1,  1,    5,  1,  1,  1,  1,  0,  1,  1
]

#replicant function - appears to mean it's the same as event function???
# may need to import info from event disassembler
fd_sequence_lens = [
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 3,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    5, 2, 2, 4, 4, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    8, 8, 8, 5, 2, 2, 2, 2,  2, 2, 2, 2, 2, 5, 7, 5,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 3, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    4, 4, 4, 3, 3, 3, 4, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  4, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2
]

# I'll refactor this later
def tok(rom, start, end):
    dex = start
    script = []
    while dex <= end:
        cmd = rom[dex]
        local_lens = sequence_lens

        if cmd == 0xFD:
            cmd = rom[dex+1]
            local_lens = fd_sequence_lens

        l = local_lens[cmd]
        if l == 0:
            print(hex(cmd), hex(rom[dex+2]), hex(dex))
            for i in script:
                print(list(map(hex, i)))
            print(hex(cmd), hex(dex))
            1/0
        script.append((rom[dex:dex+l], dex))
        dex += l
    return script

fd_names = [None]*256
names = [None]*256

#This is weird in LS, may not reflect output, however it does follow the docs
def set_sprite_sequence(args):
    sprite = args[0] & 0x07
    flag_short = shortify(args, 0)
    f = get_flag_string(flag_short, "_0x08Flags", _0x08_flags, [3, 4, 6, 15])
    sequence = args[1] & 0x7F
    return 'set_sprite_sequence', ['%i' % sequence, 'inc_sprite=%i' % sprite, 'flags=%s' % f]

def set_animation_speed(args):
    speed = args[0] & 0x07
    flag_short = args[0] >> 6
    f = get_flag_string(flag_short, "_0x10Flags", _0x10_flags, [0, 1])
    return 'set_animation_speed', ['%s' % (use_table_name('SequenceSpeeds', sequence_speed_table, speed)), '%s' % f]


names[0x00] = named('visibility_on')
names[0x01] = named('visibility_off')
names[0x02] = named('sequence_playback_on')
names[0x03] = named('sequence_playback_off')
names[0x04] = named('sequence_looping_on')
names[0x05] = named('sequence_looping_off')
names[0x06] = named('fixed_f_coord_on')
names[0x07] = named('fixed_f_coord_off')
names[0x08] = set_sprite_sequence
names[0x09] = named('reset_properties')
names[0x0A] = named('overwrite_solidity', flags(prefix='_0x0AFlags', table=_0x0A_flags))
names[0x0B] = named('set_solidity_bits', flags(prefix='_0x0AFlags', table=_0x0A_flags))
names[0x0C] = named('clear_solidity_bits', flags(prefix='_0x0AFlags', table=_0x0A_flags))
names[0x0D] = named('set_palette_row', byte_int())
names[0x0E] = named('inc_palette_row_by', byte_int())
names[0x0F] = named('inc_palette_row_by_1')
names[0x10] = set_animation_speed
# 0x16 - 0x1F undocumented
# 0x25 - 0x2F undocumented
# 0x38 - 0x3C undocumented
names[0x3D] = named('inc_palette_row_by_1')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

    def get_embedded_script(self, arr):
        commands_output = ["OSCommand()"]
        for line, _ in arr:
            if line[0] == 0xFD:
                cmd = line[1]
                rest = line[2:]
                table = fd_names
            else:
                cmd = line[0]
                rest = line[1:]
                table = names
            if table[cmd]:
                name, args = table[cmd](rest)
            else:
                name, args = 'db', ['0x%02x' % (i) for i in line]
                #print (name, args)
            commands_output.append('.%s(%s)' %
                    (name, ', '.join(args)))
        commands_output.append('.fin()')
        return "".join(commands_output)


    def handle(self, *args, **options):
        global rom 
        rom = bytearray(open(options['rom'], 'rb').read())
        print('from osscript import ObjectSequenceScript')
        print('from .objectsequencetables import SequenceSpeeds, _0x08Flags, _0x0AFlags, _0x10Flags')
        print('from randomizer.management.commands.objectsequencedisassembler import tok')
        #print('from . import items')
        print('script = ObjectSequenceScript()')

        script = tok(rom, start, end)

        for line, offset in script:
            if line[0] == 0xFD:
                cmd = line[1]
                rest = line[2:]
                table = fd_names
            else:
                cmd = line[0]
                rest = line[1:]
                table = names
            if table[cmd]:
                name, args = table[cmd](rest)
            else:
                name, args = 'db', ['0x%02x' % (i) for i in line]
            print('script.%s(%s) # 0x%x' %
                    (name, ', '.join(args), offset) + ' ' + repr(line))
        print('''
rez = script.fin()
rez_tok = tok(rez, 0, len(rez)-1)

start = 0x%x
end = 0x%x
rom_tok = tok(rom, start, end)

for l,r in zip(rez_tok, rom_tok):
if l[0] != r[0]:
    print(l, r)

''' % (start, end))