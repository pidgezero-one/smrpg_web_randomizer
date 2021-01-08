from collections import defaultdict


class EventScript:
    def __init__(self):
        self.commands = []
        self.labels = {}
        self.labels_to_fix = defaultdict(list)

    def fin(self, base=0):
        ret = bytearray(len(self.commands))
        for i, byte in enumerate(self.commands):
            ret[i] = byte
        return ret

    def append_short(self, short):
        assert 0 <= short <= 0xFFFF
        self.commands.append(short & 0xFF)
        self.commands.append((short >> 8) & 0xFF)
        return self

    def consolidate_flags(self, flags):
        val = 0x00
        for flag in flags:
            val |= 1 << flag
        return val

    def append_byte(self, byte):
        assert 0 <= byte <= 0xFF
        self.commands.append(byte)

    def db(self, *args):
        self.commands += args
        return self

    def get_branch_address(self, branch):
        if type(branch) == int:
            return branch
        elif branch in self.labels:
            return self.labels[branch]
        elif type(branch) == str:
            self.labels_to_fix[branch].append(len(self.commands))
            return 0
        raise Exception('What did you pass in here?')

    def label(self, name):
        assert name not in self.labels
        self.labels[name] = len(self.commands)
        return self

    def level_mod(self, location, mod, flags):
        return location | mod << 8 | self.consolidate_flags(flags)

    # 0xAA
    def add(self, address, value):
        if 0x70A0 <= address <= 0x719F:
            if value == 1:
                self.append_byte(0xAA)
                self.append_byte(address - 0x70A0)
            else:
                self.append_byte(0xA9)
                self.append_byte(address - 0x70A0)
                self.append_byte(value)
        else:
            1/0
        return self

    # 0x52, FD 0x52
    def add_coins(self, amount):
        if amount == 0x7000:
            self.append_byte(0xFD)
            self.append_byte(0x52)
        else:
            self.append_byte(0x52)
            self.append_byte(amount)
        return self

    # 0xFD 0x56
    def add_current_FP_7000(self):
        self.append_byte(0xFD)
        self.append_byte(0x56)
        return self

    # 0x53, FD 0x54
    def add_frog_coins(self, amount):
        if amount == 0x7000:
            self.append_byte(0xFD)
            self.append_byte(0x54)
        else:
            self.append_byte(0x53)
            self.append_byte(amount)
            return self

    # 0xFD 0x57
    def add_max_FP_7000(self):
        self.append_byte(0xFD)
        self.append_byte(0x57)
        return self

    # 0xB1, 0xB2
    def add_short(self, address, value):
        if 0x7000 <= address <= 0x71FE:
            if value == 1:
                self.append_byte(0xB2)
                self.append_byte((address - 0x7000) // 2)
            else:
                self.append_byte(0xB1)
                self.append_byte((address - 0x7000) // 2)
                self.append_short(value)
        else:
            1/0
        return self

    # 0x63
    def append_to_dialog_at_7000(self, flags):
        self.append_byte(self.consolidate_flags(flags))
        return self

    # 0x6A
    def apply_tile_mod(self, location, mod, flags):
        self.append_short(self.level_mod(location, mod, flags))
        return self

    # 0x6B
    def apply_solidity_mod(self, location, mod, flags):
        self.append_short(self.level_mod(location, mod, flags))
        return self

    # 0xD1
    def call_event(self, script_id):
        self.append_byte(0xD1)
        self.append_short(script_id)
        return self

    # 0x7C
    def circle_mask_expand_from_screen_center(self):
        self.append_byte(0x7C)
        return self

    # 0x87
    def circle_mask_nonstatic(self, obj, width, speed):
        self.append_byte(0x87)
        self.append_byte(obj)
        self.append_byte(width)
        self.append_byte(speed)
        return self

    # 0x7D
    def circle_mask_shrink_to_screen_center(self):
        self.append_byte(0x7D)
        return self

    # 0x8F
    def circle_mask_static(self, obj, width, speed):
        self.append_byte(0x8F)
        self.append_byte(obj)
        self.append_byte(width)
        self.append_byte(speed)
        return self

    # 0x64
    def close_dialog(self):
        self.append_byte(0x64)
        return self

    # 0x3F
    def create_packet_at_7010_coords_jmp_if_null(self, packet_id, address):
        self.append_byte(0x3F)
        self.append_byte(packet_id)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x3E
    def create_packet_at_object_coords_jmp_if_null(self, packet_id, object_id, address):
        self.append_byte(0x3E)
        self.append_byte(packet_id)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # FD 0x3E
    def create_packet_event_at_coords_jmp_if_null(self, packet_id, event_id, address):
        self.append_byte(0xFD)
        self.append_byte(0x3E)
        self.append_byte(packet_id)
        self.append_short(event_id)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xAB
    def dec(self, address):
        assert 0x70A0 <= address <= 0x719F
        self.append_byte(0xAB)
        self.append_byte(address - 0x70A0)

    # 0xFD 0x53
    def dec_coins(self):
        self.append_byte(0xFD)
        self.append_byte(0x53)
        return self

    # 0x57
    def dec_current_FP_7000(self):
        self.append_byte(0x57)
        return self

    # 0x56
    def dec_current_HP_7000(self, character):
        self.append_byte(0x56)
        self.append_byte(character)
        return self

    # 0xFD 0x55
    def dec_frog_coins_7000(self):
        self.append_byte(0xFD)
        self.append_byte(0x55)
        return self

    # 0xB3
    def dec_short(self, address):
        assert 0x7000 <= address <= 0x71FE
        self.append_byte(0xB3)
        self.append_byte((address - 0x7000) // 2)

    # FD 0x66
    def display_intro_title(self, y, title):
        self.append_byte(0xFD)
        self.append_byte(0x66)
        self.append_byte(y)
        self.append_byte(title)
        return self

    # 0x35
    def enable_controls(self, directions):
        self.append_byte(0x35)
        enabled_directions = self.consolidate_flags(directions)
        assert 0x00 <= enabled_directions <= 0xFF
        return self

    # 0x34
    def enable_controls_until_return(self, *directions):
        self.append_byte(0x34)
        enabled_directions = self.consolidate_flags(directions)
        assert 0x00 <= enabled_directions <= 0xFF
        return self

    # 0x68
    def enter_area(self, room, direction, x, y, z, flags):
        f = self.consolidate_flags(flags)
        room_short = room | (f & 0x8800)
        self.append_short(room_short)
        self.append_byte(x)
        y_zhalf = y | ((f >> 24) & 0x80)
        self.append_byte(y_zhalf)
        z_direction = z & (direction << 4)
        self.append_byte(z_direction)
        return self

    # 0x54
    def equip_item_to_character(self, character, item):
        self.append_byte(0x54)
        self.append_byte(character)
        self.append_byte(item)
        return self

    # can probably consolidate these
    # 0x70
    def fade_in_from_black_sync(self):
        self.append_byte(0x70)
        return self

    # 0x71
    def fade_in_from_black_async(self):
        self.append_byte(0x71)
        return self

    # 0x72
    def fade_in_from_black_sync_duration(self, duration):
        self.append_byte(0x72)
        self.append_byte(duration)
        return self

    # 0x73
    def fade_in_from_black_async_duration(self, duration):
        self.append_byte(0x73)
        self.append_byte(duration)
        return self

    # 0x78
    def fade_in_from_colour_duration(self, duration, colour):
        self.append_byte(0x78)
        self.append_byte(duration)
        self.append_byte(colour)
        return self

    # 0x92
    def fade_in_music(self, music_id):
        self.append_byte(0x92)
        self.append_byte(music_id)
        return self

    # 0x93
    def fade_out_music(self):
        self.append_byte(0x93)
        return self

    # 0x74
    def fade_out_to_black_sync(self):
        self.append_byte(0x74)
        return self

    # 0x75
    def fade_out_to_black_async(self):
        self.append_byte(0x75)
        return self

    # 0x76
    def fade_out_to_black_sync_duration(self, duration):
        self.append_byte(0x76)
        self.append_byte(duration)
        return self

    # 0x77
    def fade_out_to_black_async_duration(self, duration):
        self.append_byte(0x77)
        self.append_byte(duration)
        return self

    # 0x79
    def fade_out_to_colour_duration(self, duration, colour):
        self.append_byte(0x79)
        self.append_byte(duration)
        self.append_byte(colour)
        return self

    # 0x30
    def freeze_all_npcs_until_return(self):
        self.append_byte(0x30)
        return self

    # 0x7E
    def initiate_battle_mask(self):
        self.append_byte(0x7E)
        return self

    # 0xE0
    def jeq_byte(self, test_addr, val, branch):
        self.db(0xE0, test_addr - 0x70A0, val)
        self.append_short(self.get_branch_address(branch))
        return self

    # 0xE2
    def jeq_short(self, test_addr, val, branch):
        if test_addr == 0x7000:
            self.append_byte(0xE2)
            self.append_short(val)
            self.append_short(self.get_branch_address(branch))
        else:
            1/0
        return self

    # 0xD2
    def jmp(self, address):
        self.append_byte(0xD2)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x41
    def jmp_if_316D_is_3(self, address):
        self.append_byte(0x41)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x3D
    def jmp_if_mario_in_air(self, address):
        self.append_byte(0x3D)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x42
    def jmp_fork_mario_on_object(self, address_if_on_object, address_else):
        self.append_byte(0x42)
        self.append_short(self.get_branch_address(address_if_on_object))
        self.append_short(self.get_branch_address(address_else))
        return self

    # 0x66
    def jmp_if_dialog_option_b(self, address):
        self.append_byte(0x66)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x67
    def jmp_if_dialog_option_b_or_c(self, address):
        self.append_byte(0x67)
        self.append_short(self.get_branch_address(address))
        self.append_short(self.get_branch_address(address))
        return self

    # 0x39
    def jmp_if_mario_on_object(self, object_id, address):
        self.append_byte(0x39)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # FD 0x3D
    def jmp_if_object_in_air(self, object_id, address):
        self.append_byte(0xFD)
        self.append_byte(0x3D)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # FD 0x34
    def jmp_if_object_underwater(self, object_id, address):
        self.append_byte(0xFD)
        self.append_byte(0x34)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # FD 0x33
    def jmp_if_objects_action_script_running(self, object_id, address):
        self.append_byte(0xFD)
        self.append_byte(0x39)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x3A
    def jmp_if_objects_less_than_xy_steps_apart(self, object_a, object_b, x, y, address):
        self.append_byte(0x3A)
        self.append_byte(object_a)
        self.append_byte(object_b)
        self.append_byte(x)
        self.append_byte(y)
        self.append_short(self.get_branch_address(address))

    # 0x3A
    def jmp_if_objects_less_than_xy_steps_apart_same_z_coord(self, object_a, object_b, x, y, address):
        self.append_byte(0x3B)
        self.append_byte(object_a)
        self.append_byte(object_b)
        self.append_byte(x)
        self.append_byte(y)
        self.append_short(self.get_branch_address(address))

    # 0x32
    def jmp_if_present_in_current_level(self, object_id, address):
        self.append_byte(0x32)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x36
    def join_party(self, member):
        self.append_byte(0x36)
        self.append_byte(member | 0x80)
        return self

    def leave_party(self, member):
        self.append_byte(0x36)
        self.append_byte(member & ~0x80)
        return self

    # 0x5D
    def load_600f(self):
        self.append_byte(0x5D)
        return self

    # 0x4B
    def open_location(self, location, flags):
        self.append_byte(0x4B)
        self.append_short(location | self.consolidate_flags(flags))
        return self

    # 0x4F
    def open_menu_or_run_event_sequence(self, command):
        self.append_byte(0x4F)
        self.append_byte(command)
        return self

    # 0x8A
    def palette_set(self, palette_set, row):
        self.append_byte(0x8A)
        self.append_byte(((row - 1) << 4) | 0x0F)
        self.append_byte(palette_set)
        return self

    # 0x89
    def palette_set_morphs(self, palette_type, duration, palette_set, row):
        self.append_byte(0x89)
        self.append_byte(duration | (palette_type << 4))
        self.append_byte(row)
        self.append_byte(palette_set)
        return self

    # 0xF0
    def pause(self, value):
        self.append_byte(0xF0)
        self.append_byte(value)
        return self

    # 0x5B
    def pause_script_if_menu_open(self):
        self.append_byte(0x5B)
        return self

    # 0x7F
    def pause_script_until_effect_done(self):
        self.append_byte(0x7F)
        return self

    # FD 0x60
    def pause_script_resume_on_next_dialog_page_a(self, character, slot):
        self.append_byte(0xFD)
        self.append_byte(0x60)
        return self

    # FD 0x61
    def pause_script_resume_on_next_dialog_page_b(self, character, slot):
        self.append_byte(0xFD)
        self.append_byte(0x61)
        return self

    # 0x84
    def pixelate_layers(self, layers, size, duration):
        self.append_byte(0x84)
        self.append_byte((size << 4) | self.consolidate_flags(layers))
        self.append_byte(duration)
        return self

    # 0x90
    def play_music_current_volume(self, music_id):
        self.append_byte(0x90)
        self.append_byte(music_id)
        return self

    # 0x91
    def play_music_default_volume(self, music_id):
        self.append_byte(0x91)
        self.append_byte(music_id)
        return self

    # 0x9C
    def play_sound(self, sound_id):
        self.append_byte(0x9C)
        self.append_byte(sound_id)
        return self

    # FD 0x51
    def put_70A7_equips_inventory(self):
        self.append_byte(0xFD)
        self.append_byte(0x51)
        return self

    # 0x50
    def put_inventory(self, item_id):
        if item_id == 0x70A7:
            self.append_byte(0xFD)
            self.append_byte(0x50)
        else:
            self.append_byte(0x50)
            self.append_byte(item_id)
        return self

    # 0x5C
    def read_from_address(self, addr):
        self.append_byte(0x5C)
        self.append_short(addr)
        return self

    # FD 0x32
    def remember_last_object(self):
        self.append_byte(0xFD)
        self.append_byte(0x32)
        return self

    # 0x51
    def remove_one_from_inventory(self, item_id):
        self.append_byte(0x51)
        self.append_byte(item_id)
        return self

    # 0x82
    def reset_priority_set(self):
        self.append_byte(0x82)
        return self

    # FD 0x5C
    def restore_all_fp(self):
        self.append_byte(0xFD)
        self.append_byte(0x5C)
        return self

    # FD 0x5B
    def restore_all_hp(self):
        self.append_byte(0xFD)
        self.append_byte(0x5B)
        return self

    # 0x47
    def resume_background_event(self, timer_memory):
        self.append_byte(0x47)
        timer_memory_bits = ((timer_memory - 0x701C) / 2)
        self.append_byte(timer_memory_bits)
        return self

    # 0xFE
    def ret(self):
        self.append_byte(0xFE)
        return self

    # 0x40
    def run_background_event(self, event_id, return_on_level_exit, bit_6, bit_7):
        self.append_byte(0x60)
        self.append_short(event_id | (bit_7 << 15) | (bit_6 <<
                                                      14) | (return_on_level_exit << 13))
        return self

    # 0x44
    def run_background_event_with_pause(self, event_id, timer_memory, flags):
        self.append_byte(0x44)
        timer_memory_bits = ((timer_memory - 0x701C) / 2)
        self.append_short(event_id | (timer_memory_bits <<
                                      14) | self.consolidate_flags(flags))
        return self

    # 0x45
    def run_background_event_with_pause_return_on_exit(self, event_id, timer_memory, flags):
        self.append_byte(0x45)
        timer_memory_bits = ((timer_memory - 0x701C) / 2)
        self.append_short(event_id | (timer_memory_bits <<
                                      14) | self.consolidate_flags(flags))
        return self

    # 0x60, 0x61
    def run_dialog(self, dialog_id, above, flags):
        if dialog_id == 0x7000:
            self.append_byte(0x61)
            self.append_byte(flags & 0xA0)
        else:
            self.append_byte(0x60)
            self.append_short(dialog_id | ((flags & 0xA0) << 8))
        self.append_byte(above | ((flags >> 8) & 0xC0))
        return self

    # 0x62
    def run_dialog_duration(self, dialog_id, duration, flags):
        self.append_short(dialog_id | (duration << 13) | (flags << 8))
        return self

    # FD 0x67
    def run_ending_credits(self):
        self.append_byte(0xFD)
        self.append_byte(0x67)
        return self

    # FD 0x46
    def run_event_at_return(self, event_id):
        self.append_byte(0xFD)
        self.append_byte(0x46)
        self.append_short(event_id)
        return self

    # 0x4E
    def run_event_sequence(self, sequence, value):
        assert 0x00 <= sequence <= 0x10
        # todo: write more assertions for value
        self.append_byte(0x4E)
        self.append_short(sequence)
        self.append_byte(value)
        return self

    # FD 0x65
    def run_levelup_bonus_sequence(self):
        self.append_byte(0xFD)
        self.append_byte(0x65)
        return self

    # FD 0x4F
    def run_moleville_mountain_intro_sequence(self):
        self.append_byte(0xFD)
        self.append_byte(0x4F)
        return self

    # FD 0x4E
    def run_moleville_mountain_sequence(self):
        self.append_byte(0xFD)
        self.append_byte(0x4E)
        return self

    # FD 0x4D
    def run_star_piece_sequence(self, star):
        self.append_byte(0xFD)
        self.append_byte(0x4D)
        self.append_byte(star)
        return self

    # 0x83
    def screen_flashes_with_colour(self, colour):
        self.append_byte(0x83)
        self.append_byte(colour)

    # 0xA8
    def set(self, address, value):
        assert 0x70A0 <= address <= 0x719F
        self.append_byte(0xA8)
        self.append_byte(address - 0x70A0)
        self.append_byte(value)

    # FD 0x64
    def set_experience_packet_7000(self):
        self.append_byte(0xFD)
        self.append_byte(0x64)
        return self

    # 0x7A
    def star_mask_expand_from_screen_center(self):
        self.append_byte(0x7A)
        return self

    # 0x7B
    def star_mask_shrink_to_screen_center(self):
        self.append_byte(0x7B)
        return self

    # 0x4A
    def start_battle(self, pack, battlefield):
        self.append_byte(0x4A)
        self.append_short(pack)
        self.append_byte(battlefield)
        return self

    # 0x49
    def start_battle_700E(self):
        self.append_byte(0x49)
        return self

    # 0x9B
    def stop_sound(self):
        self.append_byte(0x9B)
        return self

    # FD 0x5E
    def store_7000_item_quantity_to_70A7(self, character, slot):
        self.append_byte(0xFD)
        self.append_byte(0x5E)
        return self

    # FD 0x5D
    def store_character_equipment_7000(self, character, slot):
        self.append_byte(0xFD)
        self.append_byte(0x4D)
        self.append_byte(character)
        self.append_byte(slot)
        return self

    # 0x58
    def store_current_FP_7000(self):
        self.append_byte(0x58)
        return self

    # 0xB0
    def set_short(self, address, value):
        if 0x7000 <= address <= 0x71FE:
            self.append_byte(0xB0)
            self.append_byte((address - 0x7000) // 2)
            self.append_short(value)
        else:
            1/0
        return self

    # 0xB4, 0xB5
    def set_short_mem(self, address_left, address_right):
        if address_left == 0x7000 and 0x70A0 <= address_right <= 0x719F:
            self.append_byte(0xB4)
            self.append_byte(address_right - 0x70A0)
        elif address_right == 0x7000 and 0x70A0 <= address_left <= 0x719F:
            self.append_byte(0xB5)
            self.append_byte(address_left - 0x70A0)
        else:
            1/0
        return self

    # 0x38
    def set_short_member_in_slot(self, slot):
        self.append_byte(0x38)
        self.append_byte(slot + 0x08)
        return self

    # 0x37
    def set_short_party_capacity(self):
        self.append_byte(0x37)
        return self

    # FD 0x43
    def stop_all_background_events(self):
        self.append_byte(0xFD)
        self.append_byte(0x43)
        return self

    # 0x55
    def store_empty_inventory_slot_count_7000(self):
        self.append_byte(0x55)
        return self

    # FD 0x58
    def store_coin_amount_7000(self):
        self.append_byte(0xFD)
        self.append_byte(0x59)
        return self

    # FD 0x59
    def store_item_amount_7000(self, item):
        self.append_byte(0xFD)
        self.append_byte(0x58)
        self.append_byte(item)
        return self

    # FD 0x5A
    def store_frog_coin_amount_7000(self):
        self.append_byte(0xFD)
        self.append_byte(0x5A)
        return self

    # 0x46
    def stop_background_event(self, timer_memory):
        self.append_byte(0x46)
        timer_memory_bits = ((timer_memory - 0x701C) / 2)
        self.append_byte(timer_memory_bits)
        return self

    # 0x80
    def tint_layers(self, red, green, blue, speed, flags):
        self.append_byte(0x7F)
        red_ = red >> 3
        green_ = green >> 3
        blue_ = blue >> 3
        self.append_short(red_ | (green_ << 5) | (blue_ << 10))
        self.append_byte(speed)
        self.append_byte(self.consolidate_flags(flags))
        return self

    # 0x31
    def unfreeze_all_npcs(self):
        self.append_byte(0x31)
        return self

    # 0x65
    def unsync_dialog(self):
        self.append_byte(0x65)
        return self


"""   def animate_object(self, character_object, length, actions):
    self.append_byte(character_object)
    self.append_byte(length)
    for action in actions:
      self.append_byte(action)
    return self """
