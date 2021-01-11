from django.core.management.base import BaseCommand
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short

banks = [
    {
        "start": 0x210800,
        "end": 0x21BADE
    }
]

sequence_lens = [
    1,  1,  1,  1,  1,  1,  1,  1,    3,  1,  2,  2,  2,  2,  2,  1,
    2,  2,  2,  2,  2,  1,  1,  1,    1,  1,  1,  1,  1,  1,  1,  1,
    2,  1,  1,  2,  5,  5,  16, 16,   16, 2,  1,  5,  3,  3,  3,  7,
    3,  3,  3,  3,  2,  3,  1,  1,    1,  1,  6,  6,  5,  3,  5,  4,
    1,  1,  1,  1,  1,  1,  1,  1,    1,  1,  1,  1,  1,  1,  1,  1,
    2,  2,  2,  2,  2,  2,  2,  2,    1,  2,  2,  1,  1,  1,  1,  1,
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
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
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


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

    def get_embedded_script(self, arr):
        commands_output = ["OSCommand()"]
        for line, offset in arr:
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
        return "".join(commands_output)


    def handle(self, *args, **options):
        global rom 
        rom = bytearray(open(options['rom'], 'rb').read())
        print('from osscript import ObjectSequenceScript')  # This doesn't exist...yet.
        #print('from .objectsequencetables import ')
        print('from randomizer.management.commands.battledisassembler import tok')
        #print('from . import items')
        print('script = ObjectSequenceScript()')

        scripts = [
            {
                "script": tok(rom, bank["start"], bank["end"]),
                "bank": bank
            }
            for bank in banks]

        for script in scripts:
            for line, offset in arr:
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

''' % (script["bank"]["start"], script["bank"]["end"]))