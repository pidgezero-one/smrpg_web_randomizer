from django.core.management.base import BaseCommand
from randomizer.data.eventtables import controller_direction_table, radial_direction_table, room_table, sound_table, area_object_table, npc_packet_table, location_table, shop_table, event_sequence_table, menu_tutorial_table, overworld_sequence_table, playable_characters_table, equip_slots_table, dialog_duration_table, intro_titles_table, colours_table, palette_set_types_table, music_table, _0x40_flags, _0x60_flags, _0x62_flags, _0x63_flags, _0x68_flags, _0x6A_flags, _0x6B_flags, _0x81_flags, _0x84_flags
from randomizer.data.items import get_default_items
from randomizer.management.disassembler_common import shortify, bit, dbyte, named, con, byte, byte_int, short, short_int, build_table, use_table_name, get_flag_string


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
    },
    {
        "start": 0x200800,
        "end": 0x20DFFF
    },
]

"""start = 0x200800
end = 0x20DFFF"""
# why do these addresses break it?
# probably needs an animation parser to fix

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
            if 0xF0 <= sub_command <= 0xF1:
                l = obj_event_lens[sub_command & 0x0F] + \
                    (rom[dex+2] & 0x7F) + addend
            elif 0xF2 <= sub_command <= 0xFF:
                l = obj_event_lens[sub_command & 0x0F] + addend
            else:
                l = (sub_command & 0x7F) + 2 + addend
        # print(rom[dex:dex+l], hex(dex))
        if l == 0:
            print(hex(cmd), hex(rom[dex+2]), hex(dex))
            for i in script:
                print(list(map(hex, i)))
            print(hex(cmd), hex(dex))
            1/0
        # print(list(map(hex, [l, start, end, dex])))
        script.append((rom[dex:dex+l], dex))
        dex += l
    return script


fd_names = [None]*256
names = [None]*256


def append_to_dialog_at_7000(args):
    return 'append_to_dialog_at_7000', [get_flag_string(args[0], '_0x63Flags', _0x63_flags, [5, 7])]


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
    return ['%s' % (use_table_name('AreaObjects', area_object_table, args[0])), 'width=%i' % (args[1]), 'speed=%i' % (args[2])]


def circle_mask_nonstatic(args):
    return 'circle_mask_nonstatic', circle_mask(args)


def circle_mask_static(args):
    return 'circle_mask_static', circle_mask(args)


def enable_controls(args):
    enabled_bits = get_flag_string(
        args[0], 'ControllerDirections', controller_direction_table)
    return 'enable_controls', [enabled_bits]


def enable_controls_until_return(args):
    enabled_bits = get_flag_string(
        args[0], 'ControllerDirections', controller_direction_table)
    return 'enable_controls_until_return', [enabled_bits]


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


def modify_party(args):
    char_byte = args[0]
    is_joining = (char_byte & 0x80) >> 7
    char = char_byte & ~0x80
    if (is_joining):
        return 'join_party', ['%s' % (use_table_name('AreaObjects', area_object_table, char))]
    else:
        return 'leave_party', ['%s' % (use_table_name('AreaObjects', area_object_table, char))]


def open_location(args):
    location_byte = args[0]
    enabled_bits = get_flag_string(args[1], bits=[5, 6, 7])
    return 'open_location', ['%s' % (use_table_name('Locations', location_table, location_byte)), enabled_bits]


def palette_set(args):
    palette_set = args[1]
    row = (args[0] >> 4) + 1
    return 'palette_set', ['palette_set=%i' % (palette_set), 'row=%i' % (row)]


def palette_set_morphs(args):
    morph_type = args[0] >> 4
    duration = args[0] & 0x0F
    palette_set = args[2]
    row = args[1]
    return 'palette_set_morphs', ['%s' % (use_table_name('PaletteSetTypes', palette_set_types_table, morph_type)), 'duration=%i' % (duration), 'palette_set=%i' % (palette_set), 'row=%i' % (row)]



def pixelate_layers(args):
    layers = get_flag_string(
        args[0], "_0x84Flags", _0x84_flags, bits=[0, 1, 2, 3])
    size = args[0] >> 4
    duration = args[1]
    return 'pixelate_layers', [layers, 'size=%i' % (size), 'duration=%i' % (duration)]


def priority_set(args):
    mainscreen = get_flag_string(args[0], '_0x81Flags', _0x81_flags)
    subscreen = get_flag_string(args[1], '_0x81Flags', _0x81_flags)
    color_math = get_flag_string(args[2], '_0x81Flags', _0x81_flags)
    return 'priority_set', ['mainscreen=%s' % (mainscreen), 'subscreen=%s' % (subscreen), 'color_math=%s' % (color_math)]


def resume_background_event(args):
    timer_memory = 0x701C + args[0] * 2
    return 'resume_background_event', ['timer_memory=0x%04x' % (timer_memory)]


def run_background_event(args):
    event_byte = shortify(args, 0)
    event_id = event_byte & 0x0FFF
    flags = get_flag_string(event_byte, '_0x40Flags',
                            _0x40_flags, [13, 14, 15])
    return 'run_background_event', ['%i' % (event_id), flags]


def run_bkgd_event_pause_math(args):
    short = shortify(args, 0)
    event_id = short & 0x0FFF
    timer_memory = 0x701C + (args[1] >> 6) * 2
    return ['event_id=%i' % (event_id), 'timer_memory=0x%04x' % (timer_memory), get_flag_string(short, bits=[12, 13])]


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
    above = args[position_arg] & 0x2F
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


def set_short_member_in_slot(args):
    slot = args[0] - 0x08
    return 'set_short_member_in_slot', ['%i' % (slot)]


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
    return 'tint_layers', ['0x%02x' % (red), '0x%02x' % (green), '0x%02x' % (blue), 'speed=%i' % (speed), flags]


# names[0x00] = named('animate_object', byte(), byte(), )
names[0x30] = named('freeze_all_npcs_until_return')
names[0x31] = named('unfreeze_all_npcs')
names[0x32] = named('jmp_if_present_in_current_level', byte(
    prefix="AreaObjects", table=area_object_table), short())
# 33 undocumented
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
names[0x4B] = open_location
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
# 0x59 undocumented
# 0x5A undocumented
names[0x5B] = named('pause_script_if_menu_open')
names[0x5C] = named('read_from_address', short())
names[0x5D] = named('load_600f')
# 0x5E undocumented
# 0x5F undocumented
names[0x60] = run_dialog
names[0x61] = run_dialog
names[0x62] = run_dialog_duration
names[0x63] = append_to_dialog_at_7000
names[0x64] = named('close_dialog')
names[0x65] = named('unsync_dialog')
names[0x66] = named('jmp_if_dialog_option_b', short())
names[0x67] = named('jmp_if_dialog_option_b_or_c', short(), short())
names[0x68] = enter_area
# 0x69 undocumented, unfortunately
names[0x6A] = apply_tile_mod
names[0x6B] = apply_solidity_mod
# 0x6C undocumented
# 0x6D undocumented
# 0x6E undocumented
# 0x6F undocumented
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
# 0x85 undocumented
# 0x86 undocumented
names[0x87] = circle_mask_nonstatic
# 0x88 undocumented
names[0x89] = palette_set_morphs
names[0x8A] = palette_set
# 0x8B undocumented
# 0x8C undocumented
# 0x8D undocumented
# 0x8E undocumented
names[0x8F] = circle_mask_static
names[0x90] = named('play_music_current_volume', byte(prefix="Music", table=music_table))
names[0x91] = named('play_music_default_volume', byte(prefix="Music", table=music_table))
names[0x92] = named('fade_in_music', byte(prefix="Music", table=music_table))
names[0x93] = named('fade_out_music')
names[0x94] = named('stop_music')
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
names[0xD1] = named('call_event', short_int())
names[0xD2] = named('jmp', short())
names[0xE0] = named('jeq_byte', byte(0x70A0), byte(), short())
names[0xE2] = named('jeq_short', con(0x7000), short(), short())
names[0xF0] = named('pause', byte_int())
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
fd_names[0x43] = named('stop_all_background_events')
fd_names[0x46] = named('run_event_at_return', short_int()
                       )
fd_names[0x4D] = named('run_star_piece_sequence', byte())
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
fd_names[0x60] = named('pause_script_resume_on_next_dialog_page_a')
fd_names[0x61] = named('pause_script_resume_on_next_dialog_page_a')
fd_names[0x64] = named('set_experience_packet_7000')
fd_names[0x65] = named('run_levelup_bonus_sequence')
fd_names[0x66] = named('display_intro_title', byte_int(), byte(
    prefix="IntroTitles", table=intro_titles_table))
fd_names[0x67] = named('run_ending_credits')
#fd_names[0x94] = deactivate_sound_channels


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('-r', '--rom', dest='rom',
                            help='Path to a Mario RPG rom')

    def handle(self, *args, **options):
        # print(short()(0x02, 0x80))
        global rom  # Should make the round tripper work...?
        rom = bytearray(open(options['rom'], 'rb').read())
        print('from enscript import EventScript')  # This doesn't exist...yet.
        print('from .eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags')
        print('from randomizer.management.commands.battledisassembler import tok, rom')
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
                    # print (name, args)
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
