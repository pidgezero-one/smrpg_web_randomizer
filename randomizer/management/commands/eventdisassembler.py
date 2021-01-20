import re
from django.core.management.base import BaseCommand
from randomizer.data.eventtables import controller_direction_table, radial_direction_table, room_table, sound_table, area_object_table, npc_packet_table, location_table, shop_table, event_sequence_table, menu_tutorial_table, overworld_sequence_table, playable_characters_table, equip_slots_table, dialog_duration_table, intro_titles_table, colours_table, palette_set_types_table, music_table, music_direction_table, music_pitch_table, coord_table, coord_unit_table, tutorial_table, _0x40_flags, _0x60_flags, _0x62_flags, _0x63_flags, _0x68_flags, _0x6A_flags, _0x6B_flags, _0x81_flags, _0x84_flags
from randomizer.data.items import get_default_items
from randomizer.management.disassembler_common import shortify, bit, dbyte, hbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string, flags, con_int, flags_short
from randomizer.management.commands.objectsequencedisassembler import Command as OSCommand
import sys
sys.stdout.reconfigure(encoding='utf-8')

banks = [
    {
        "id": 0x1E,
        "start": 0x1E0C00,
        "end": 0x1EFFFF,
        "pointers": {
            "start": 0x1E0000,
            "end": 0x1E0BFF
        }
    },
    {
        "id": 0x1F,
        "start": 0x1F0C00,
        "end": 0x1FFFFF,
        "pointers": {
            "start": 0x1F0000,
            "end": 0x1F0BFF
        }
    },
    {
        "id": 0x20,
        "start": 0x200800,
        "end": 0x20DFFF,
        "pointers": {
            "start": 0x200000,
            "end": 0x2007FF
        }
    },
]


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
    3, 3, 4, 4, 4, 4, 2, 2,  2, 2, 2, 2, 2, 2, 2, 2,
]

items_table = build_table(get_default_items(None))

jmp_cmds = [0x3F, 0x3E, 0xD2, 0x41, 0xE6, 0xE7, 0xDC, 0xDD, 0xDE, 0xD8, 0xD9, 0xDA, 0xEC, 0xED, 0x66, 0xEA, 0xEF, 0xEE, 0xEB, 0x3D, 0x39, 0xDF, 0xDB, 0xF8, 0x3A, 0x32, 0xE9, 0xE8, 0xE0, 0xE2, 0xE4, 0xE1, 0xE3, 0xE5]

jmp_cmds_double = [0x42, 0x67]

jmp_cmds_fd = [0x3E, 0x62, 0x96, 0x97, 0x3D, 0xF0, 0x34, 0x33]

def is_eligible_nonembedded_command(cmd):
    if cmd[0] == 0x10:
        return True
    elif cmd[0] == 0x7D:
        return True
    elif cmd[0] == 0xFD and cmd[1] == 0x9E:
        return True
    else:
        return False

jumped_to_from_action_queue = []

def tok(rom, start, end, bank):
    dex = start
    script = []
    while dex <= end:
        cmd = None
        sub_command = None
        is_nonembedded = dex in jumped_to_from_action_queue and is_eligible_nonembedded_command(rom[dex:(dex+2)])
        sequence_bytes = []

        # I don't trust this at all, but I have no idea how to determine this otherwise
        # Determines the length of a non-embedded action queue
        if is_nonembedded:
            ind_ = 0
            oc = OSCommand()
            return_bytes = []
            while (len(return_bytes) == 0 and (dex + ind_ <= end)):
                ind_ += 1
                try:
                    cmds = oc.get_embedded_script(rom[dex:(dex + ind_)])
                    return_bytes = [c['cmd'] for c in cmds["commands"] if c['cmd'] == 0xFE]
                except:
                    pass
            l = ind_
            sequence_bytes = rom[(dex):(dex+l)]
        else:
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
                if 0xF0 <= sub_command <= 0xF1:
                    l = obj_event_lens[sub_command & 0x0F] + \
                        (rom[dex+2] & 0x7F) + addend
                    sequence_bytes = rom[(dex+3):(dex+l)]
                elif 0xF2 <= sub_command <= 0xFF:
                    l = obj_event_lens[sub_command & 0x0F] + addend
                else:
                    l = (sub_command & 0x7F) + 2 + addend
                    sequence_bytes = rom[(dex+2):(dex+l)]

        if (cmd is not None and sub_command is not None and cmd < 0x30 and sub_command <= 0xF1) or is_nonembedded:

            oc = OSCommand()
            cmds = oc.get_embedded_script(sequence_bytes)
            jump_cmds = [c for c in cmds["commands"] if c['has_jump']]
            # I don't know if this will cover every scenario.
            # This assumes _a lot_ about non-embedded queues, namely:
            # Must be jumped to from another embedded queue in the same script, and must start with 0xFD 9E, 0x10, or 0x7D
            # Also assumes the jump address is the single last arg in an object sequence script, which appears to be true
            # - at least for all documented functions.
            # Don't need to worry about FD object sequence commands as none of them seem to have jumps
            if (len(jump_cmds) > 0):
                for jmp in jump_cmds:
                    target_addr_bytes = jmp["args"][-2:]
                    target_addr = shortify(target_addr_bytes, 0)
                    dubious_address = (bank["id"] << 16) | target_addr
                    jumped_to_from_action_queue.append(dubious_address)

        if l == 0:
            print(hex(cmd), hex(rom[dex+2]), hex(dex))
            for i in script:
                print(list(map(hex, i)))
            print(hex(cmd), hex(dex))
            1/0
        script.append((rom[dex:dex+l], dex))
        dex += l
    return script


def parse_line(line, offset, with_comments=True):
    if offset in jumped_to_from_action_queue and is_eligible_nonembedded_command(line[0:2]):
        name, args = 'non_embedded_action_queue', ['%r' % line[0:2]]
    else:
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

    return name, args

fd_names = [None]*256
names = [None]*256

def is_jump(line):
    if line[0] == 0xFD:
        is_jump = line[1] in jmp_cmds_fd
    else:
        is_jump = line[0] in jmp_cmds or line[0] in jmp_cmds_double
    return is_jump


def get_jump_args(line, args):
    if line[0] in jmp_cmds_double:
        return -2
    else:
        return -1



def adjust_music_calc(args):
    duration = args[0]
    speed_byte = args[1]
    direction = bit(args, 1, 7)
    if speed_byte > 127:
        change = (256-speed_byte)
    else:
        change = speed_byte
    return direction, change, duration


def adjust_music_pitch(args):
    direction, change, duration = adjust_music_calc(args)
    return 'adjust_music_pitch', ['%s' % (use_table_name('MusicPitch', music_pitch_table, direction)), '%i' % (change), '%i' % (duration)]


def adjust_music_tempo(args):
    direction, change, duration = adjust_music_calc(args)
    return 'adjust_music_tempo', ['%s' % (use_table_name('MusicDirections', music_direction_table, direction)), '%i' % (change), '%i' % (duration)]

def level_mod(args, prefix, table):
    area_byte = shortify(args, 0)
    use_alternate = get_flag_string(area_byte, prefix, table, [15])
    area = area_byte & 0x01FF
    mod = (args[1] >> 1) & 0x3F
    return ['%s' % (use_table_name('Rooms', room_table, area)), '%i' % (mod), use_alternate]


def apply_tile_mod(args):
    return 'apply_tile_mod', level_mod(args, '_0x6AFlags', _0x6A_flags)


def apply_solidity_mod(args):
    return 'apply_solidity_mod', level_mod(args, '_0x6BFlags', _0x6B_flags)


def circle_mask(args):
    return ['%s' % (use_table_name('AreaObjects', area_object_table, args[0])), '%i' % (args[1]), '%i' % (args[2])]


def circle_mask_nonstatic(args):
    return 'circle_mask_nonstatic', circle_mask(args)


def circle_mask_static(args):
    return 'circle_mask_static', circle_mask(args)


def enter_area(args):
    room_short = shortify(args, 0)
    room = room_short & ~0x8000 & ~0x800
    x = args[2]
    y = args[3] & ~0x80
    flags = get_flag_string(args[:4], "_0x68Flags", _0x68_flags, [11, 15, 31])
    z_direction = args[4]
    z = z_direction & 0x1F
    direction = z_direction >> 5
    return 'enter_area', ['%s' % (use_table_name('Rooms', room_table, room)), '%s' % (use_table_name('RadialDirections', radial_direction_table, direction)), '%i' % (x), '%i' % (y), '%i' % (z), flags]


def fade_out_music_to_volume(args):
    return 'fade_out_music_to_volume', ['%i' % (args[0]), '%i' % (args[1])]


def fade_out_sound_to_volume(args):
    return 'fade_out_sound_to_volume', ['%i' % (args[0]), '%i' % (args[1])]


def jmp_depending_on_object_event_trigger(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    addr = shortify(args, 2)
    if presence:
        func = 'jmp_if_object_trigger_enabled'
    else:
        func = 'jmp_if_object_trigger_disabled'
    return func, ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%s' % (use_table_name('Rooms', room_table, level)), '0x%04x' % (addr)]


def jmp_depending_on_object_presence(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    addr = shortify(args, 2)
    if presence:
        func = 'jmp_if_object_in_level'
    else:
        func = 'jmp_if_object_not_in_level'
    return func, ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%s' % (use_table_name('Rooms', room_table, level)), '0x%04x' % (addr)]


def mem_7000_shift_left(args):
    addr = 2*args[0] + 0x7000
    shift = 256 - args[1]
    return 'mem_7000_shift_left', ['0x%04x' % (addr), '%i' % (shift)]


def modify_party(args):
    char_byte = args[0]
    is_joining = (char_byte & 0x80) >> 7
    char = char_byte & ~0x80
    if (is_joining):
        return 'join_party', ['%s' % (use_table_name('AreaObjects', area_object_table, char))]
    else:
        return 'leave_party', ['%s' % (use_table_name('AreaObjects', area_object_table, char))]


def palette_set(args):
    palette_set = args[1]
    row = (args[0] >> 4) + 1
    return 'palette_set', ['%i' % (palette_set), '%i' % (row)]


def palette_set_morphs(args):
    morph_type = args[0] >> 4
    duration = args[0] & 0x0F
    palette_set = args[2]
    row = args[1]
    return 'palette_set_morphs', ['%s' % (use_table_name('PaletteSetTypes', palette_set_types_table, morph_type)), '%i' % (duration), '%i' % (palette_set), '%i' % (row)]


def parse_object_coord(cmd):
    def inner_parse_object_coord(args):
        obj = args[0] & 0x3F
        unit = bit(args, 0, 6)
        coord = cmd - 0xC4
        func_params = ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%s' % (
            use_table_name('Coords', coord_table, coord))]
        if (cmd < 0xC9):
            func_params.append('%s' % (use_table_name(
                'CoordUnits', coord_unit_table, unit)))
        return 'set_7000_to_object_coord', func_params
    return inner_parse_object_coord


def parse_obj_fxn(obj):
    def inner_parse_obj_fxn(args):
        sub_command = args[0]
        if sub_command <= 0xF1:
            is_async = bit(args, 0, 7)
            if sub_command < 0xF0:
                if (is_async):
                    cmd = 'action_queue_async'
                else:
                    cmd = 'action_queue_sync'
                if len(args) > 1:
                    script = args[1:]
                else:
                    script = []
            else:  # 0xF0 and 0xF1 don't appear to be different...
                if (is_async):
                    cmd = 'start_embedded_action_script_async'
                else:
                    cmd = 'start_embedded_action_script_sync'
                if len(args) > 2:
                    script = args[2:]
                else:
                    script = []
            return cmd, ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%r' % script]
        elif sub_command == 0xF2:
            script = shortify(args, 1)
            return 'set_action_script_sync', ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%i' % (script)]
        elif sub_command == 0xF3:
            script = shortify(args, 1)
            return 'set_action_script_async', ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%i' % (script)]
        elif sub_command == 0xF4:
            script = shortify(args, 1)
            return 'set_temp_action_script_sync', ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%i' % (script)]
        elif sub_command == 0xF5:
            script = shortify(args, 1)
            return 'set_temp_action_script_async', ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%i' % (script)]
        elif sub_command == 0xF6:
            return 'unsync_action_script', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xF7:
            return 'summon_to_current_level_at_marios_coords', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xF8:
            return 'summon_to_current_level', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xF9:
            return 'remove_from_current_level', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xFA:
            return 'pause_action_script', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xFB:
            return 'resume_action_script', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xFC:
            return 'enable_trigger', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xFD:
            return 'disable_trigger', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        elif sub_command == 0xFE:
            return 'stop_embedded_action_script', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
        else:
            return 'reset_coords', ['%s' % (use_table_name('AreaObjects', area_object_table, obj))]
    return inner_parse_obj_fxn


def pause(args):
    return 'pause', ['%i' % (args[0] + 1)]


def pause_short(args):
    s = shortify(args, 0)
    return 'pause_short', ['%i' % (s + 1)]


def pixelate_layers(args):
    layers = get_flag_string(
        args[0], "_0x84Flags", _0x84_flags, bits=[0, 1, 2, 3])
    size = args[0] >> 4
    duration = args[1]
    return 'pixelate_layers', [layers, '%i' % (size), '%i' % (duration)]


def priority_set(args):
    mainscreen = get_flag_string(args[0], '_0x81Flags', _0x81_flags)
    subscreen = get_flag_string(args[1], '_0x81Flags', _0x81_flags)
    color_math = get_flag_string(args[2], '_0x81Flags', _0x81_flags)
    return 'priority_set', ['%s' % (mainscreen), '%s' % (subscreen), '%s' % (color_math)]


def resume_background_event(args):
    timer_memory = 0x701C + args[0] * 2
    return 'resume_background_event', ['0x%04x' % (timer_memory)]


def run_background_event(args):
    event_byte = shortify(args, 0)
    event_id = event_byte & 0x0FFF
    f = get_flag_string(event_byte, '_0x40Flags', _0x40_flags, [13, 14, 15])
    return 'run_background_event', ['%i' % (event_id), f]


def run_bkgd_event_pause_math(args):
    s = shortify(args, 0)
    event_id = s & 0x0FFF
    timer_memory = 0x701C + (args[1] >> 6) * 2
    return ['%i' % (event_id), '0x%04x' % (timer_memory), '%s' % get_flag_string(s, bits=[12, 13])]


def run_background_event_with_pause(args):
    return 'run_background_event_with_pause', run_bkgd_event_pause_math(args)


def run_background_event_with_pause_return_on_exit(args):
    return 'run_background_event_with_pause_return_on_exit', run_bkgd_event_pause_math(args)


# what to do about flags for this?
# maybe make a shared fxn that gets full byte as one number & extracts bits that way
def run_dialog(args):
    if len(args) == 3:
        flags_arg = 1
        position_arg = 2
        dialog_id = shortify(args, 0) & 0x0FFF
        dialog_output = '%i' % (dialog_id)
    else:
        flags_arg = 0
        position_arg = 1
        dialog_id = 0x7000
        dialog_output = '0x%04x' % (dialog_id)
    flags = get_flag_string(
        args[flags_arg:position_arg+1], '_0x60Flags', _0x60_flags, [5, 7, 14, 15])
    above = args[position_arg] & 0x3F
    return 'run_dialog', [dialog_output, '%s' % (use_table_name('AreaObjects', area_object_table, above)), flags]


def run_dialog_duration(args):
    dialog_id = shortify(args, 0) & 0x0FFF
    flags = get_flag_string(args[1], '_0x60Flags', _0x60_flags, [7])
    duration = (args[1] & 0x7F) >> 5
    return 'run_dialog_duration', ['%i' % (dialog_id), '%s' % (use_table_name('DialogDurations', dialog_duration_table, duration)), flags]


def run_event_sequence(args):
    def determine_table_value():
        if args[0] == 0x02:
            return '%s' % (use_table_name('Locations', location_table, args[1]))
        elif args[0] == 0x03:
            return '%s' % (use_table_name('Shops', shop_table, args[1]))
        elif args[0] == 0x05:
            return '%s' % (use_table_name('items', items_table, args[1]))
        elif args[0] == 0x07:
            return '%s' % (use_table_name('MenuTutorials', menu_tutorial_table, args[1]))
        elif args[0] == 0x10:
            return '%s' % (use_table_name('OverworldSequences', overworld_sequence_table, args[1]))
        else:
            return '0x%02x' % (args[1])
    return 'run_event_sequence', ['%s' % (use_table_name('EventSequences', event_sequence_table, args[0])), determine_table_value()]


def parse_target_bit(cmd, args):
    bit = args[0] & 0x07
    addr = 0x7040 + (0x0020 * (cmd & 0x0F)) + (args[0] >> 3)
    return addr, bit


# name bit vars eventually
def set_bit(cmd):
    def inner_set_bit(args):
        addr, bit = parse_target_bit(cmd, args)
        return 'set_bit', ['0x%04x' % addr, '%i' % bit]
    return inner_set_bit


def clear_bit(cmd):
    def inner_clear_bit(args):
        addr, bit = parse_target_bit(cmd - 0xA4, args)
        return 'clear_bit', ['0x%04x' % addr, '%i' % bit]
    return inner_clear_bit


def store_set_bits(cmd):
    def inner_set_bit(args):
        addr, bit = parse_target_bit(cmd - 0xA8, args)
        return 'store_set_bits', ['0x%04x' % addr, '%i' % bit]
    return inner_set_bit


def jmp_if_bit_clear(cmd):
    def inner_jmp_if_bit_clear(args):
        addr, bit = parse_target_bit(cmd - 0xDC, args)
        to_addr = shortify(args, 1)
        return 'jmp_if_bit_clear', ['0x%04x' % addr, '%i' % bit, '0x%04x' % to_addr, ]
    return inner_jmp_if_bit_clear


def jmp_if_bit_set(cmd):
    def inner_jmp_if_bit_set(args):
        addr, bit = parse_target_bit(cmd - 0xD8, args)
        to_addr = shortify(args, 1)
        return 'jmp_if_bit_set', ['0x%04x' % addr, '%i' % bit, '0x%04x' % to_addr, ]
    return inner_jmp_if_bit_set


def set_short_member_in_slot(args):
    slot = args[0] - 0x08
    return 'set_short_member_in_slot', ['%i' % (slot)]


def set_object_presence_in_level(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    if presence:
        func = 'summon_to_level'
    else:
        func = 'remove_from_level'
    return func, ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%s' % (use_table_name('Rooms', room_table, level))]


def set_object_trigger_in_level(args):
    presence = bit(args, 1, 7)
    obj = (args[1] & 0x7F) >> 1
    level = shortify(args, 0) & 0x1FF
    if presence:
        func = 'enable_trigger_in_level'
    else:
        func = 'disable_trigger_in_level'
    return func, ['%s' % (use_table_name('AreaObjects', area_object_table, obj)), '%s' % (use_table_name('Rooms', room_table, level))]


def stop_background_event(args):
    timer_memory = 0x701C + args[0] * 2
    return 'stop_background_event', ['timer_memory=0x%04x' % (timer_memory)]


def tint_layers(args):
    colour_bytes = shortify(args, 0)
    red = (colour_bytes & 0x001F) << 3
    green = (colour_bytes & 0x03E0) >> 2
    blue = (colour_bytes & 0x7C00) >> 7
    speed = args[3]
    flags = get_flag_string(args[2], '_0x81Flags',
                            _0x81_flags, [0, 1, 2, 4, 5, 6, 7])
    return 'tint_layers', ['0x%02x' % (red), '0x%02x' % (green), '0x%02x' % (blue), '%i' % (speed), '%s' % flags]


names[0x00] = parse_obj_fxn(0x00)
names[0x01] = parse_obj_fxn(0x01)
names[0x02] = parse_obj_fxn(0x02)
names[0x03] = parse_obj_fxn(0x03)
names[0x04] = parse_obj_fxn(0x04)
names[0x05] = parse_obj_fxn(0x05)
names[0x06] = parse_obj_fxn(0x06)
names[0x07] = parse_obj_fxn(0x07)
names[0x08] = parse_obj_fxn(0x08)
names[0x09] = parse_obj_fxn(0x09)
names[0x0A] = parse_obj_fxn(0x0A)
names[0x0B] = parse_obj_fxn(0x0B)
names[0x0C] = parse_obj_fxn(0x0C)
names[0x0D] = parse_obj_fxn(0x0D)
names[0x0E] = parse_obj_fxn(0x0E)
names[0x0F] = parse_obj_fxn(0x0F)
names[0x10] = parse_obj_fxn(0x10)
names[0x11] = parse_obj_fxn(0x11)
names[0x12] = parse_obj_fxn(0x12)
names[0x13] = parse_obj_fxn(0x13)
names[0x14] = parse_obj_fxn(0x14)
names[0x15] = parse_obj_fxn(0x15)
names[0x16] = parse_obj_fxn(0x16)
names[0x17] = parse_obj_fxn(0x17)
names[0x18] = parse_obj_fxn(0x18)
names[0x19] = parse_obj_fxn(0x19)
names[0x1A] = parse_obj_fxn(0x1A)
names[0x1B] = parse_obj_fxn(0x1B)
names[0x1C] = parse_obj_fxn(0x1C)
names[0x1D] = parse_obj_fxn(0x1D)
names[0x1E] = parse_obj_fxn(0x1E)
names[0x1F] = parse_obj_fxn(0x1F)
names[0x20] = parse_obj_fxn(0x20)
names[0x21] = parse_obj_fxn(0x21)
names[0x22] = parse_obj_fxn(0x22)
names[0x23] = parse_obj_fxn(0x23)
names[0x24] = parse_obj_fxn(0x24)
names[0x25] = parse_obj_fxn(0x25)
names[0x26] = parse_obj_fxn(0x26)
names[0x27] = parse_obj_fxn(0x27)
names[0x28] = parse_obj_fxn(0x28)
names[0x29] = parse_obj_fxn(0x29)
names[0x2A] = parse_obj_fxn(0x2A)
names[0x2B] = parse_obj_fxn(0x2B)
names[0x2C] = parse_obj_fxn(0x2C)
names[0x2D] = parse_obj_fxn(0x2D)
names[0x2E] = parse_obj_fxn(0x2E)
names[0x2F] = parse_obj_fxn(0x2F)
names[0x30] = named('freeze_all_npcs_until_return')
names[0x31] = named('unfreeze_all_npcs')
names[0x32] = named('jmp_if_present_in_current_level', byte(
    prefix="AreaObjects", table=area_object_table), short())
# 33 undocumented
names[0x34] = named('enable_controls_until_return', flags(
    prefix='ControllerDirections', table=controller_direction_table))
names[0x35] = named('enable_controls', flags(
    prefix='ControllerDirections', table=controller_direction_table))
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
names[0x3F] = named('create_packet_at_7010_coords_jmp_if_null', byte(
    prefix="NPCPackets", table=npc_packet_table), short())
names[0x40] = run_background_event
names[0x41] = named('jmp_if_316D_is_3', short())
names[0x42] = named('jmp_fork_mario_on_object', short(), short())
# 0x43 undocumented
names[0x44] = run_background_event_with_pause
names[0x45] = run_background_event_with_pause_return_on_exit
names[0x46] = stop_background_event
names[0x47] = resume_background_event
# 0x48 undocumented
names[0x49] = named('start_battle_700E')
names[0x4A] = named('start_battle', short(), byte_int())
names[0x4B] = named('open_location', byte(
    prefix='Locations', table=location_table), flags(bits=[5, 6, 7]))
names[0x4C] = named('open_shop', byte(prefix="Shops", table=shop_table))
# 0x4D undocumented
names[0x4E] = run_event_sequence
names[0x4F] = named('open_menu_or_run_event_sequence', byte(
    prefix="EventSequences", table=event_sequence_table))
names[0x50] = named('put_inventory', byte(prefix="items", table=items_table))
names[0x51] = named('remove_one_from_inventory',
                    byte(prefix="items", table=items_table))
names[0x52] = named('add_coins', byte_int())
names[0x53] = named('add_frog_coins', byte_int())
names[0x54] = named('equip_item_to_character', byte(prefix="PlayableCharacters",
                                                    table=playable_characters_table), byte(prefix="items", table=items_table))
names[0x55] = named('store_empty_inventory_slot_count_7000')
names[0x56] = named('dec_current_HP_7000', byte(
    prefix="PlayableCharacters", table=playable_characters_table))
names[0x57] = named('dec_current_FP_7000')
names[0x58] = named('store_current_FP_7000')
# 0x59 - 0x5A undocumented
names[0x5B] = named('pause_script_if_menu_open')
names[0x5C] = named('read_from_address', short())
names[0x5D] = named('load_600f')
# 0x5E - 0x5F undocumented
names[0x60] = run_dialog
names[0x61] = run_dialog
names[0x62] = run_dialog_duration
names[0x63] = named('append_to_dialog_at_7000', flags(
    prefix='_0x63Flags', table=_0x63_flags, bits=[5, 7]))
names[0x64] = named('close_dialog')
names[0x65] = named('unsync_dialog')
names[0x66] = named('jmp_if_dialog_option_b', short())
names[0x67] = named('jmp_if_dialog_option_b_or_c', short(), short())
names[0x68] = enter_area
# 0x69 undocumented, unfortunately
names[0x6A] = apply_tile_mod
names[0x6B] = apply_solidity_mod
# 0x6C - 0x6F undocumented
names[0x70] = named('fade_in_from_black_sync')
names[0x71] = named('fade_in_from_black_async')
names[0x72] = named('fade_in_from_black_sync_duration',
                    byte_int())
names[0x73] = named('fade_in_from_black_async_duration',
                    byte_int())
names[0x74] = named('fade_out_to_black_sync')
names[0x75] = named('fade_out_to_black_async')
names[0x76] = named('fade_out_to_black_sync_duration',
                    byte_int())
names[0x77] = named('fade_out_to_black_async_duration',
                    byte_int())
names[0x78] = named('fade_in_from_colour_duration', byte_int(), byte(
    prefix="Colours", table=colours_table))
names[0x79] = named('fade_out_to_colour_duration', byte_int(), byte(
    prefix="Colours", table=colours_table))
names[0x7A] = named('star_mask_expand_from_screen_center')
names[0x7B] = named('star_mask_shrink_to_screen_center')
names[0x7C] = named('circle_mask_expand_from_screen_center')
names[0x7D] = named('circle_mask_shrink_to_screen_center')
names[0x7E] = named('initiate_battle_mask')
names[0x7F] = named('pause_script_until_effect_done')
names[0x80] = tint_layers
names[0x81] = priority_set
names[0x82] = named('reset_priority_set')
names[0x83] = named('screen_flashes_with_colour', byte(
    prefix="Colours", table=colours_table))
# note: LS interface doesn't allow the duration arg to exceed 63, however the source code suggests it should.
names[0x84] = pixelate_layers
# 0x85 - 0x86 undocumented
names[0x87] = circle_mask_nonstatic
# 0x88 undocumented
names[0x89] = palette_set_morphs
names[0x8A] = palette_set
# 0x8B - 0x8E undocumented
names[0x8F] = circle_mask_static
names[0x90] = named('play_music_current_volume',
                    byte(prefix="Music", table=music_table))
names[0x91] = named('play_music_default_volume',
                    byte(prefix="Music", table=music_table))
names[0x92] = named('fade_in_music', byte(prefix="Music", table=music_table))
names[0x93] = named('fade_out_music')
names[0x94] = named('stop_music')
names[0x95] = fade_out_music_to_volume
# 0x96 undocumented
names[0x97] = adjust_music_tempo
names[0x98] = adjust_music_pitch
# 0x99 - 0x9A undocumented
names[0x9B] = named('stop_sound')
names[0x9C] = named('play_sound', byte(
    prefix="Sounds", table=sound_table), con_int(6))
names[0x9D] = named('play_sound_balance', byte(
    prefix="Sounds", table=sound_table), byte_int())
names[0x9E] = fade_out_sound_to_volume
# 0x9F undocumented
names[0xA0] = set_bit(0xA0)
names[0xA1] = set_bit(0xA1)
names[0xA2] = set_bit(0xA2)
names[0xA3] = named('set_mem_704x_at_7000_bit')
names[0xA4] = clear_bit(0xA4)
names[0xA5] = clear_bit(0xA5)
names[0xA6] = clear_bit(0xA6)
names[0xA7] = named('clear_mem_704x_at_7000_bit')
names[0xA8] = named('set', byte(0x70A0), byte_int())
names[0xA9] = named('add', byte(0x70A0), byte_int())
names[0xAA] = named('add', byte(0x70A0), con(1))
names[0xAB] = named('dec', byte(0x70A0))
names[0xAC] = named('set', con(0x7000), short_int())
names[0xAD] = named('add', con(0x7000), short_int())
names[0xAE] = named('add', con(0x7000), con(1))
names[0xAF] = named('dec', con(0x7000))
names[0xB0] = named('set_short', dbyte(0x7000), short())
names[0xB1] = named('add_short', dbyte(0x7000), short())
names[0xB2] = named('add_short', dbyte(0x7000), con(1))
names[0xB3] = named('dec_short', dbyte(0x7000))
names[0xB4] = named('set_short_mem', con(0x7000), byte(0x70A0))
names[0xB5] = named('set_short_mem', byte(0x70A0), con(0x7000))
names[0xB6] = named('set_random', con(0x7000), short_int())
names[0xB7] = named('set_random', dbyte(0x7000),
                    short_int())  # may be confused for 0xB6
names[0xB8] = named('add_short_mem', con(0x7000), dbyte(0x7000))
names[0xB9] = named('dec_short_mem', con(0x7000), dbyte(0x7000))
names[0xBA] = named('set_short_mem', con(0x7000),
                    dbyte(0x7000))  # may be confused for 0xB4
names[0xBB] = named('set_short_mem',
                    dbyte(0x7000), con(0x7000))  # may be confused for 0xB5
names[0xBC] = named('set_short_mem',
                    dbyte(0x7000), dbyte(0x7000))  # may be confused for 0xB4 or 0xB5
names[0xBD] = named('swap_short_mem', dbyte(0x7000), dbyte(0x7000))
names[0xBE] = named('move_7010_7012_7014_to_7016_7018_701A')
names[0xBF] = named('move_7016_7018_701A_to_7010_7012_7014')
names[0xC0] = named('mem_compare', con(0x7000), short_int())
names[0xC1] = named('mem_compare', con(0x7000), dbyte(0x7000))
names[0xC2] = named('mem_compare', dbyte(0x7000), short_int())
names[0xC3] = named('set_7000_to_current_level')
names[0xC4] = parse_object_coord(0xC4)
names[0xC5] = parse_object_coord(0xC5)
names[0xC6] = parse_object_coord(0xC6)
names[0xC7] = named('set_7010_to_object_xyz', byte(
    prefix="AreaObjects", table=area_object_table))
names[0xC8] = named('set_7016_to_object_xyz', byte(
    prefix="AreaObjects", table=area_object_table))
names[0xC9] = parse_object_coord(0xC9)
names[0xCA] = named('set_7000_to_pressed_button')
names[0xCB] = named('set_7000_to_tapped_button')
# 0xCC - 0xCF undocumented
names[0xD0] = named('jmp_to_event', short_int())
names[0xD1] = named('run_event_as_subroutine', short_int())
names[0xD2] = named('jmp', short())
names[0xD3] = named('jmp_to_subroutine', short())
names[0xD4] = named('start_loop_n_times', byte_int())
names[0xD5] = named('start_loop_n_frames', short_int())
names[0xD6] = named('set_object_memory_to', dbyte(0x7000))
names[0xD7] = named('end_loop')
names[0xD8] = jmp_if_bit_set(0xD8)
names[0xD9] = jmp_if_bit_set(0xD9)
names[0xDA] = jmp_if_bit_set(0xDA)
names[0xDB] = named('jmp_if_mem_704x_at_7000_bit_set', short())
names[0xDC] = jmp_if_bit_clear(0xDC)
names[0xDD] = jmp_if_bit_clear(0xDD)
names[0xDE] = jmp_if_bit_clear(0xDE)
names[0xDF] = named('jmp_if_mem_704x_at_7000_bit_set', short())
names[0xE0] = named('jmp_if_var_equals_byte',
                    byte(0x70A0), byte_int(), short())
names[0xE1] = named('jmp_if_var_not_equals_byte',
                    byte(0x70A0), byte_int(), short())
names[0xE2] = named('jmp_if_var_equals_short',
                    con(0x7000), short_int(), short())
names[0xE3] = named('jmp_if_var_not_equals_short',
                    con(0x7000), short_int(), short())
names[0xE4] = named('jmp_if_var_equals_short', dbyte(
    0x7000), short_int(), short())  # may be confused for 0xE2
names[0xE5] = named('jmp_if_var_not_equals_short', dbyte(
    0x7000), short_int(), short())  # may be confused for 0xE3
names[0xE6] = named('jmp_if_7000_all_bits_clear', flags_short(), short())
names[0xE7] = named('jmp_if_7000_any_bits_set', flags_short(), short())
names[0xE8] = named('jmp_if_random_above_128', short())
names[0xE9] = named('jmp_if_random_above_66', short())
names[0xEA] = named('jmp_if_loaded_memory_is_0', short())
names[0xEB] = named('jmp_if_loaded_memory_is_not_0', short())
names[0xEC] = named('jmp_if_comparison_result_is_greater_or_equal', short())
names[0xED] = named('jmp_if_comparison_result_is_lesser', short())
names[0xEE] = named('jmp_if_loaded_memory_is_below_0', short())
names[0xEF] = named('jmp_if_loaded_memory_is_above_or_equal_0', short())
names[0xF0] = pause
names[0xF1] = pause_short
names[0xF2] = set_object_presence_in_level
names[0xF3] = set_object_trigger_in_level
names[0xF4] = named('summon_object_at_70A8_to_current_level')
names[0xF5] = named('remove_object_at_70A8_from_current_level')
names[0xF6] = named('enable_event_trigger_for_object_at_70A8')
names[0xF7] = named('disable_event_trigger_for_object_at_70A8')
names[0xF8] = jmp_depending_on_object_presence
names[0xF9] = named('jmp_to_start_of_this_script')  # indistinguishable from F9
names[0xFA] = named('jmp_to_start_of_this_script')
names[0xFB] = named('reset_and_choose_game')
names[0xFC] = named('reset_game')
# 0xFD is a special case
names[0xFE] = named('ret')
names[0xFF] = named('end_all')

fd_names[0x30] = named('unfreeze_camera')
fd_names[0x31] = named('freeze_camera')
fd_names[0x32] = named('remember_last_object')
fd_names[0x33] = named('jmp_if_objects_action_script_running', byte(
    prefix="AreaObjects", table=area_object_table), short())
fd_names[0x34] = named('jmp_if_object_underwater', byte(
    prefix="AreaObjects", table=area_object_table), short())
# 0x35 - 0x3C undocumented
fd_names[0x3D] = named('jmp_if_object_in_air', byte(
    prefix="AreaObjects", table=area_object_table), short())
fd_names[0x3E] = named('create_packet_event_at_coords_jmp_if_null', byte(
    prefix="NPCPackets", table=npc_packet_table), short(), short())
# 0x3F undocumented
fd_names[0x40] = named('move_script_to_main_thread')
fd_names[0x41] = named('move_script_to_background_thread_1')
fd_names[0x42] = named('move_script_to_background_thread_2')
fd_names[0x43] = named('stop_all_background_events')
# 0x44 - 0x45 undocumented
fd_names[0x46] = named('run_event_at_return', short_int())
# 0x47 - 0x49 undocumented
fd_names[0x4A] = named('open_save_menu')
fd_names[0x4B] = named('inc_exp_by_packet')
fd_names[0x4C] = named('run_menu_tutorial', byte(
    prefix="Tutorials", table=tutorial_table))
fd_names[0x4D] = named('run_star_piece_sequence', byte_int())
fd_names[0x4E] = named('run_moleville_mountain_sequence')
fd_names[0x4F] = named('run_moleville_mountain_intro_sequence')
fd_names[0x50] = named('put_inventory', con(0x70A7))
fd_names[0x51] = named('put_70A7_equips_inventory')
fd_names[0x52] = named('add_coins', con(0x7000))
fd_names[0x53] = named('dec_coins')
fd_names[0x54] = named('add_frog_coins', con(0x7000))
fd_names[0x55] = named('dec_frog_coins_7000')
fd_names[0x56] = named('add_current_FP_7000')
fd_names[0x57] = named('add_max_FP_7000')
fd_names[0x58] = named('store_item_amount_7000',
                       byte(prefix="items", table=items_table))
fd_names[0x59] = named('store_coin_amount_7000')
fd_names[0x5A] = named('store_frog_coin_amount_7000')
fd_names[0x5B] = named('restore_all_hp')
fd_names[0x5C] = named('restore_all_fp')
fd_names[0x5D] = named('store_character_equipment_7000', byte(prefix="PlayableCharacters",
                                                              table=playable_characters_table), byte(prefix="EquipSlots", table=equip_slots_table), )
fd_names[0x5E] = named('store_7000_item_quantity_to_70A7')
# 0x5F undocumented
fd_names[0x60] = named('pause_script_resume_on_next_dialog_page_a')
fd_names[0x61] = named('pause_script_resume_on_next_dialog_page_a')
fd_names[0x62] = named('if_0210_bits_012_clear_do_not_jump', short())
# 0x63 undocumented
fd_names[0x64] = named('set_experience_packet_7000')
fd_names[0x65] = named('run_levelup_bonus_sequence')
fd_names[0x66] = named('display_intro_title', byte_int(), byte(
    prefix="IntroTitles", table=intro_titles_table))
fd_names[0x67] = named('run_ending_credits')
# 0x68 - 0x87 undocumented
fd_names[0x88] = named('set_bit_7_offset', dbyte(0x0158))
fd_names[0x89] = named('clear_bit_7_offset', dbyte(0x0158))
# 0x8A undocumented
fd_names[0x8B] = named('set_bit_3_offset', dbyte(0x0158))
# 0x8C - 0x8F undocumented
fd_names[0x90] = named('store_bytes_to_0335_0556', byte(), byte())
fd_names[0x91] = named('store_FF_to_0335')
fd_names[0x92] = named('store_01_to_0334')
fd_names[0x93] = named('store_00_to_0334')
fd_names[0x94] = named('deactivate_sound_channels', flags())
# 0x95 undocumented
fd_names[0x96] = named('jmp_if_audio_memory_at_least', byte_int(), short())
fd_names[0x97] = named('jmp_if_audio_memory_equals', byte_int(), short())
# 0x98 - 0x9B undocumented
fd_names[0x9C] = named('play_sound', byte(
    prefix="Sounds", table=sound_table), con_int(4))
fd_names[0x9D] = named('play_sound_balance', byte(
    prefix="Sounds", table=sound_table), byte_int())  # indistinguishable from 0x9D
fd_names[0x9E] = named('play_music', byte(prefix="Music", table=music_table))
fd_names[0x9F] = named('stop_music')  # indistinguishable from 0x94
fd_names[0xA0] = named('stop_music')  # indistinguishable from 0x94
fd_names[0xA1] = named('stop_music')  # indistinguishable from 0x94
fd_names[0xA2] = named('stop_music')  # indistinguishable from 0x94
fd_names[0xA3] = named('fade_out_music')  # indistinguishable from 0x93
fd_names[0xA4] = named('slow_down_music')
fd_names[0xA5] = named('speed_up_music_to_normal')
fd_names[0xA6] = named('stop_music')  # indistinguishable from 0x94
# 0xA7 undocumented
fd_names[0xA8] = store_set_bits(0xA8)  # this is the same as 0xA0
fd_names[0xA9] = store_set_bits(0xA9)  # this is the same as 0xA1
fd_names[0xAA] = store_set_bits(0xAA)  # this is the same as 0xA2
# 0xAB undocumented
fd_names[0xAC] = named('set_7000_to_7F_mem_var', short(0xF800))
# 0xAD - 0xAF undocumented
fd_names[0xB0] = named('mem_7000_and_const', short())
fd_names[0xB1] = named('mem_7000_or_const', short())
fd_names[0xB2] = named('mem_7000_xor_const', short())
fd_names[0xB3] = named('mem_7000_and_var', dbyte(0x7000))
fd_names[0xB4] = named('mem_7000_or_var', dbyte(0x7000))
fd_names[0xB5] = named('mem_7000_xor_var', dbyte(0x7000))
fd_names[0xB6] = mem_7000_shift_left
fd_names[0xB7] = named('generate_random_num_from_range_var', dbyte(0x7000))
fd_names[0xB8] = named('store_7000_minecart_timer')
# 0xB9 - 0xC5 undocumented
fd_names[0xC6] = named(
    'clear_7016_to_7018_and_isolate_701A_high_byte_if_7018_bit_0_set')
# 0xC7 undocumented
fd_names[0xC8] = named(
    'multiply_and_add_mem_3148_store_to_offset_7FB000_plus_outputx2', byte_int(), byte_int())
# 0xC9 - 0xEF undocumented
fd_names[0xF0] = jmp_depending_on_object_event_trigger
# 0xF1 - 0xF7 undocumented
fd_names[0xF8] = named('exor_crashes_into_keep')
fd_names[0xF9] = named('mario_glows')
fd_names[0xFA] = named('set_bit_3', con(0x01D8))
fd_names[0xFB] = named('store_01_to_0248')
fd_names[0xFC] = named('store_00_to_0248')
fd_names[0xFD] = named('store_02_to_0248')
fd_names[0xFE] = named('xor_3105_with_01')


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

    def handle(self, *args, **options):
        # print(short()(0x02, 0x80))
        global rom  # Should make the round tripper work...?
        rom = bytearray(open(options['rom'], 'rb').read())
        print('from django.core.management.base import BaseCommand')
        print('from randomizer.logic.enscript import EventScript')
        print('from randomizer.management.commands.eventdisassembler import tok, banks')
        print('from randomizer.logic.osscript import ObjectSequenceScript as OSCommand')
        print('from randomizer.data import items')

        scripts_data = []

        scripts = []

        #determine what the individual lines are
        for j in range(len(banks)):

            bank = banks[j]
            ptrs = []
            for i in range(bank["pointers"]["start"], bank["pointers"]["end"], 2):
                ptrs.append((bank["id"] << 16) | (shortify(rom, i)))
            event_lengths = []
            for i in range(len(ptrs)):
                if (i < len(ptrs) - 1):
                    event_lengths.append(ptrs[i + 1] - ptrs[i])
                    script_content = tok(rom, ptrs[i], ptrs[i + 1] - 1, bank)
                else:
                    event_lengths.append(bank["end"] - ptrs[i])
                    script_content = tok(rom, ptrs[i], bank["end"], bank)
                scripts.append(script_content)



        #not working for non-embedded action queues

        
        #translate lines into commands and note any jump addresses
        for i in range(len(scripts)):
            script = scripts[i]
            sd = []
            for j in range(len(script)):
                line, offset = script[j]
                name, args = parse_line(line, offset, False)
                identifier = 'EVENT_%i_%s_%i' % (i, name, j)
                subscript = []
                if (is_jump(line)):
                    arg_index = get_jump_args(line, args)
                    jump_args = [(int(ja, 16) | (offset & 0xFF0000)) for ja in args[arg_index:]]
                else:
                    jump_args = []
                    if (line[0] < 0x30 and line[1] <= 0xF1):
                        if 0xF0 <= line[1] <= 0xF1:
                            additional_offset = 3
                        else:
                            additional_offset = 2
                        ss = args[-1:][0]
                        args = args[:-1]
                        oc = OSCommand()
                        disassembled_queue = oc.get_embedded_script(ss)
                        disassembled_queue_commands = disassembled_queue["commands"]
                        for k in range(len(disassembled_queue_commands)):
                            cmd = disassembled_queue_commands[k]
                            if cmd["has_jump"]:
                                sub_jump_args = [(int(ja, 16) | (offset & 0xFF0000)) for ja in cmd["parsed_args"][-1:]]
                            else:
                                sub_jump_args = []
                            subscript.append({
                                'command': cmd["name"],
                                'args': cmd["parsed_args"],
                                'original_offset': offset + additional_offset + cmd["original_offset"],
                                'identifier': identifier + "_SUBSCRIPT_%s_%i" % (cmd["name"], k),
                                'jumps': sub_jump_args
                            })
                sd.append({
                    'command': name,
                    'args': args,
                    "original_offset": offset,
                    "identifier": identifier,
                    "jumps": jump_args,
                    "subscript": subscript
                })
            scripts_data.append(sd)

        print('scripts = [None]*%i' % len(scripts_data))

        scripts_with_named_jumps = []

        #get the identifiers corresponding to where the jumps are going
        for i in range(len(scripts_data)):
            script = scripts_data[i]
            this_script = []
            for cmd in script:
                jumps = []
                commands_to_replace = len(cmd["jumps"]) * -1
                for j in cmd["jumps"]:
                    for sd in scripts_data:
                        candidates = [c for c in sd if c["original_offset"] == j]
                        if (len(candidates) > 0):
                            jumped_command = candidates[0]
                            jumps.append('\'%s\'' % jumped_command["identifier"])
                if commands_to_replace == 0:
                    new_args = cmd["args"]
                else:
                    new_args = cmd["args"][:commands_to_replace] + jumps

                subscript = []
                for emb in cmd["subscript"]:
                    commands_to_replace = len(emb["jumps"]) * -1
                    subscript_jumps = []
                    for j in emb["jumps"]:
                        for sd in scripts_data:
                            candidates = [c for c in sd if c["original_offset"] == j]
                            if (len(candidates) > 0):
                                jumped_command = candidates[0]
                                subscript_jumps.append('\'%s\'' % jumped_command["identifier"])
                            else:
                                for command in sd:
                                    candidates = [c for c in command["subscript"] if c["original_offset"] == j]
                                    if (len(candidates) > 0):
                                        jumped_command = candidates[0]
                                        subscript_jumps.append('\'%s\'' % jumped_command["identifier"])
                                    #not working
                                    #search for jmp_if_loaded
                    if commands_to_replace == 0:
                        new_subscript_args = emb["args"]
                    else:
                        new_subscript_args = emb["args"][:commands_to_replace] + subscript_jumps
                    subscript_cmd_with_named_jumps = {
                        'command': emb["command"],
                        'args': new_subscript_args,
                        "identifier": emb["identifier"],
                        #"offset": emb["original_offset"]
                    }
                    subscript.append(subscript_cmd_with_named_jumps)

                cmd_with_named_jumps = {
                    'command': cmd["command"],
                    'args': new_args,
                    "identifier": cmd["identifier"],
                    #"offset": cmd["original_offset"],
                    "subscript": subscript
                }
                this_script.append(cmd_with_named_jumps)
            scripts_with_named_jumps.append(this_script)

        def writeline(f, ln):
            f.write(ln + "\n")

        for i in range(len(scripts_with_named_jumps)):
            file = open("randomizer/data/eventscripts/script_%i.py" % i, "w")
            writeline(file, 'from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags')
            writeline(file, 'from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags')
            script = scripts_with_named_jumps[i]
            if len(script) == 0:
                writeline(file, 'script = []')
            else:
                writeline(file, 'script = [')
                for cmd in script:
                    writeline(file, '    {')
                    #writeline(file, '        "offset": 0x%x,' % cmd["offset"])
                    writeline(file, '        "identifier": %r,' % cmd['identifier'])
                    writeline(file, '        "command": %r,' % cmd['command'])
                    writeline(file, '        "args": [%s],' % ', '.join(cmd["args"]))
                    if len(cmd['subscript']) > 0:
                        writeline(file, '        "subscript": [')
                        for ss in cmd['subscript']:
                            writeline(file, '            {')
                            #writeline(file, '                "offset": 0x%x,' % ss["offset"])
                            writeline(file, '                "identifier": %r,' % ss["identifier"])
                            writeline(file, '                "command": %r,' % ss["command"])
                            writeline(file, '                "args": [%s]' % ', '.join(ss["args"]))
                            writeline(file, '            },')
                        writeline(file, '        ]')
                    else:
                        writeline(file, '        "subscript": %s' % cmd['subscript'])
                    writeline(file, '    },')
                writeline(file, ']')
            file.close()


# not working right now because non-embedded action queues mess everything up
# as well as duplicate commands (like 0x94 and 0xFD0xA2) w/ diff lengths
# next step should be to introduce jump system