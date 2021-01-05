from django.core.management.base import BaseCommand
from randomizer.management.commands.battledisassembler import named, con, byte, short, items_table
from randomizer.data.eventtables import ControllerDirections, controller_direction_table, RadialDirections, radial_direction_table, Rooms, room_table, Sounds, sound_table, AreaObjects, area_object_table, NPCPackets, npc_packet_table

""" start = 0x201467
end = 0x201837

start = 0x1E6173
end = 0x1E66F8

start = 0x1FB4C1
end = 0x1FB522 """

banks = [
    {
        "start": 0x1E0C00,
        "end": 0x1EFFFF
    },
    {
        "start": 0x1F0C00,
        "end": 0x1FFFFF
    }
]

"""start = 0x200800
end = 0x20DFFF"""
# why do these addresses break it?

event_lens = [
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    1, 1, 4, 4, 2, 2, 2, 1,  2, 4, 7, 7, 6, 3, 5, 4,
    3, 3, 5, 1, 3, 3, 2, 2,  0, 1, 4, 3, 2, 1, 3, 2,
    2, 2, 2, 2, 3, 1, 2, 1,  1, 1, 1, 1, 3, 1, 1, 1,
    4, 3, 3, 2, 1, 1, 3, 5,  6, 1, 3, 3, 1, 1, 1, 1,
    1, 1, 2, 2, 1, 1, 2, 2,  3, 3, 1, 1, 1, 1, 1, 1,
    5, 4, 1, 2, 3, 1, 1, 4,  1, 4, 3, 1, 1, 1, 1, 4,
    2, 2, 2, 1, 1, 3, 3, 3,  3, 1, 1, 1, 2, 3, 3, 3,
    2, 2, 2, 1, 2, 2, 2, 1,  3, 3, 2, 2, 3, 3, 1, 1,
    4, 4, 2, 2, 2, 2, 3, 4,  2, 2, 2, 2, 3, 3, 1, 1,
    3, 2, 4, 1, 2, 2, 2, 2,  2, 2, 1, 1, 1, 1, 1, 1,
    3, 3, 3, 3, 2, 3, 2, 1,  4, 4, 4, 3, 4, 4, 4, 3,
    5, 5, 5, 5, 6, 6, 5, 5,  3, 5, 3, 3, 3, 3, 3, 3,
    2, 3, 3, 3, 1, 1, 1, 1,  5, 1, 1, 1, 1, 0, 1, 1
]

fd_event_lens = [
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    0, 0, 0, 0, 0, 0, 0, 0,  0, 0, 0, 0, 0, 0, 0, 0,
    2, 2, 2, 5, 5, 2, 2, 2,  2, 2, 2, 2, 2, 5, 7, 4,
    2, 2, 2, 2, 2, 2, 4, 2,  2, 2, 2, 2, 3, 3, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  3, 2, 2, 2, 2, 4, 2, 2,
    2, 2, 4, 2, 2, 2, 4, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  3, 3, 3, 3, 5, 2, 5, 3,
    4, 2, 2, 2, 3, 3, 5, 5,  3, 2, 2, 2, 3, 4, 3, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  3, 3, 3, 2, 4, 2, 2, 2,
    4, 4, 4, 3, 3, 3, 4, 3,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  4, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    2, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
    6, 2, 2, 2, 2, 2, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2
]

obj_event_lens = [
    2, 2, 4, 4, 4, 4, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
]


def tok(rom, start, end):
    dex = start
    script = []
    while dex <= end:
        cmd = rom[dex]
        sub_command = rom[dex+1]
        local_lens = event_lens
        addend = 0

        if cmd == 0xFD:
            cmd = rom[dex+1]
            local_lens = fd_event_lens
            sub_command = rom[dex+2]
            addend = 1

        l = local_lens[cmd]
        if cmd < 0x30:
            if 0xF0 <= sub_command <= 0xFF:
                l = obj_event_lens[sub_command & 0x0F] + addend
            else:
                l = (sub_command & 0x7F) + 2 + addend

        if l == 0:
            print(hex(cmd), hex(rom[dex+2]), hex(dex))
            for i in script:
                print(list(map(hex, i)))
            print(hex(cmd), hex(dex))
            1/0
        #print(list(map(hex, [l, start, end, dex])))
        script.append((rom[dex:dex+l], dex))
        dex += l
    return script


fd_names = [None]*256
names = [None]*256


def dbyte(offset=0):
    def inner_dbyte(args):
        return '0x%04x' % (2*args[0] + offset), args[1:]
    return inner_dbyte


def shortify(arr, dex):
    return arr[dex] + (arr[dex + 1] << 8)


def bit(arr, dex, bit_num):
    return (arr[dex] & 1 << bit_num) >> bit_num


def use_table_name(prefix, table, val):
    return '%s%s' % (prefix and (prefix + '.'), table[val])


def run_dialog(args):
    value, _ = short()(args)
    value = int(value, 16)
    did = value & 0x7FFF
    bit = (value & 0x8000) >> 15
    return 'run_dialog', ['0x%04x' % (did), str(bit), '0x%02x' % (args[2])]


def enter_area(args):
    room_short = shortify(args, 0)
    run_entrance_event = (room_short & 0x8000) >> 15
    show_message = (room_short & 0x800) >> 11
    room = room_short & ~0x8000 & ~0x800

    x = args[2]

    y_zhalf = args[3]
    is_z_half = (y_zhalf & 0x80) >> 7
    y = y_zhalf & ~0x80

    z_direction = args[4]
    z = z_direction & 0x1F
    direction = z_direction >> 5

    return 'enter_area', ['room=%s' % (use_table_name('Rooms', room_table, room)), 'run_entrance_event=%r' % bool(run_entrance_event), 'show_message=%r' % bool(show_message), 'is_z_half=%r' % bool(is_z_half), 'direction=%s' % (use_table_name('RadialDirections', radial_direction_table, direction)), 'x=%i' % (x), 'y=%i' % (y), 'z=%i' % (z)]


def enable_controls(args):
    enabled_bits = [use_table_name('ControllerDirections', controller_direction_table, i)
                    for i in controller_direction_table if args[0] & bit(args, 0, i)]
    return 'enable_controls', enabled_bits


def enable_controls_until_return(args):
    enabled_bits = [use_table_name('ControllerDirections', controller_direction_table, i)
                    for i in controller_direction_table if args[0] & bit(args, 0, i)]
    return 'enable_controls_until_return', enabled_bits


def modify_party(args):
    char_byte = args[0]
    is_joining = (char_byte & 0x80) >> 7
    char = char_byte & ~0x80
    if (is_joining):
        return 'join_party', ['%s' % (use_table_name('AreaObjects', area_object_table, char))]
    else:
        return 'leave_party', ['%s' % (use_table_name('AreaObjects', area_object_table, char))]


def set_short_member_in_slot(args):
    slot = args[0] - 0x08
    return 'set_short_member_in_slot', ['%i' % (slot)]


#names[0x00] = named('animate_object', byte(), byte(), )
names[0x30] = named('freeze_all_npcs_until_return')
names[0x31] = named('unfreeze_all_npcs')
names[0x32] = named('jmp_if_present_in_current_level', byte(
    prefix="AreaObjects", table=area_object_table), short())
names[0x34] = enable_controls_until_return
names[0x35] = enable_controls
names[0x36] = modify_party
names[0x37] = named('set_short_party_capacity')
names[0x38] = set_short_member_in_slot
names[0x39] = named('jmp_if_mario_on_object', byte(
    prefix="AreaObjects", table=area_object_table), short())
names[0x3A] = named('jmp_if_objects_less_than_xy_steps_apart', byte(
    prefix="AreaObjects", table=area_object_table), byte(
    prefix="AreaObjects", table=area_object_table), byte(), byte(), short())
names[0x3B] = named('jmp_if_objects_less_than_xy_steps_apart_same_z_coord', byte(
    prefix="AreaObjects", table=area_object_table), byte(
    prefix="AreaObjects", table=area_object_table), byte(), byte(), short())
# 3C undocumented
names[0x3D] = named('jmp_if_mario_in_air', short())
names[0x3E] = named('create_packet_at_object_coords_jmp_if_null', byte(
    prefix="NPCPackets", table=npc_packet_table), byte(
    prefix="AreaObjects", table=area_object_table), short())
names[0x50] = named('put_inventory', byte(prefix="items", table=items_table))
names[0x60] = run_dialog  # FIX. Dunno what's broken
names[0x68] = enter_area
names[0x9B] = named('stop_sound')
names[0x9C] = named('play_sound', byte(prefix="Sounds", table=sound_table))
names[0xA8] = named('set', byte(0x70A0), byte())
names[0xA9] = named('add', byte(0x70A0), byte())
names[0xAA] = named('add', byte(0x70A0), con(1))
names[0xAB] = named('dec', byte(0x70A0))
names[0xB0] = named('set_short', dbyte(0x7000), short())
names[0xB1] = named('add_short', dbyte(0x7000), short())
names[0xB2] = named('add_short', dbyte(0x7000), con(1))
names[0xB3] = named('dec_short', dbyte(0x7000))
names[0xB4] = named('set_short_mem', con(0x7000), byte(0x70A0))
names[0xB5] = named('set_short_mem', byte(0x70A0), con(0x7000))
names[0xD1] = named('call_event', short())  # maybe output as dec here?
names[0xD2] = named('jmp', short())
names[0xE0] = named('jeq_byte', byte(0x70A0), byte(), short())
names[0xE2] = named('jeq_short', con(0x7000), short(), short())
names[0xF0] = named('pause', byte())
names[0xFE] = named('ret')

fd_names[0x32] = named('remember_last_object')
fd_names[0x33] = named('jmp_if_objects_action_script_running', byte(
    prefix="AreaObjects", table=area_object_table), short())
fd_names[0x34] = named('jmp_if_object_underwater', byte(
    prefix="AreaObjects", table=area_object_table), short())
fd_names[0x3D] = named('jmp_if_object_in_air', byte(
    prefix="AreaObjects", table=area_object_table), short())
fd_names[0x3E] = named('create_packet_event_at_coords_jmp_if_null', byte(
    prefix="NPCPackets", table=npc_packet_table), short(), short())
fd_names[0x50] = named('put_inventory', con(0x70A7))


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

    def handle(self, *args, **options):
        #print(short()(0x02, 0x80))
        global rom  # Should make the round tripper work...?
        rom = bytearray(open(options['rom'], 'rb').read())
        print('from enscript import EventScript')  # This doesn't exist...yet.
        print('from .eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets')
        print('from . import items')
        print('script = EventScript()')

        scripts = [
            {
                "script": tok(rom, bank["start"], bank["end"]),
                "bank": bank
            }
            for bank in banks]

        script = tok(rom, banks[0]["start"], banks[0]["end"])

        for script in scripts:
            for line, offset in script["script"]:
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
                print('script.%s(%s) # 0x%x' %
                      (name, ', '.join(args), offset) + ' ' + repr(line))
            print('''
from randomizer.management.commands.battledisassembler import tok, rom

rez = script.fin()
rez_tok = tok(rez, 0, len(rez)-1)

start = 0x%x
end = 0x%x
rom_tok = tok(rom, start, end)

for l,r in zip(rez_tok, rom_tok):
if l[0] != r[0]:
    print(l, r)

''' % (script["bank"]["start"], script["bank"]["end"]))
