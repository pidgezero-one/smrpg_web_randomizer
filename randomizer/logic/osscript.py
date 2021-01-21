from collections import defaultdict


class ObjectSequenceScript:
    def __init__(self):
        self.commands = []
        self.labels = {}
        self.labels_to_fix = defaultdict(list)

    def fin(self, base=0):
        ret = bytearray(len(self.commands))
        for i, byte in enumerate(self.commands):
            ret[i] = byte
        return ret
    
    #assembles an array of hex lines corresponding to an embedded action script, for assembling in enscript.py
    def get_dummy_bytearray(script):
        dummy_lines = []
        for command in script:
            assembler = ObjectSequenceScript()
            func = getattr(assembler, command["command"], None)
            if "args" in command.keys():
                dummy_args = [0 if isinstance(arg, str) else arg for arg in command["args"]]
            else:
                dummy_args = []
            func(*dummy_args)
            dummy_lines.append(assembler.fin())
        return dummy_lines


    # helper functions

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

    # function-specific assemblers are listed below

    # 0x00
    def visibility_on(self):
        self.append_byte(0x00)
        return self

    # 0x01
    def visibility_off(self):
        self.append_byte(0x01)
        return self

    # 0x02
    def sequence_playback_on(self):
        self.append_byte(0x02)
        return self

    # 0x03
    def sequence_playback_off(self):
        self.append_byte(0x03)
        return self

    # 0x04
    def sequence_looping_on(self):
        self.append_byte(0x04)
        return self

    # 0x05
    def sequence_looping_off(self):
        self.append_byte(0x05)
        return self

    # 0x06
    def fixed_f_coord_on(self):
        self.append_byte(0x06)
        return self

    # 0x07
    def fixed_f_coord_off(self):
        self.append_byte(0x07)
        return self

    # 0x08
    def set_sprite_sequence(self, sequence_or_mold, inc_sprite, flags):
        self.append_byte(0x08)
        val = self.consolidate_flags(flags) | (
            sequence_or_mold << 8) | inc_sprite
        self.append_short(val)
        return self

    # 0x09
    def reset_properties(self):
        self.append_byte(0x09)
        return self

    # 0x0A
    def overwrite_solidity(self, flags):
        self.append_byte(0x0A)
        self.append_byte(self.consolidate_flags(flags))
        return self

    # 0x0B
    def set_solidity_bits(self, flags):
        self.append_byte(0x0B)
        self.append_byte(self.consolidate_flags(flags))
        return self

    # 0x0C
    def clear_solidity_bits(self, flags):
        self.append_byte(0x0C)
        self.append_byte(self.consolidate_flags(flags))
        return self

    # 0x0D
    def set_palette_row(self, row):
        self.append_byte(0x0D)
        self.append_byte(row)
        return self

    # 0x0E
    def inc_palette_row_by(self, rows):
        self.append_byte(0x0E)
        self.append_byte(rows)
        return self

    # 0x0F
    def inc_palette_row_by_1(self):
        self.append_byte(0x0F)
        return self

    # 0x10
    def set_animation_speed(self, speed, flags):
        self.append_byte(0x10)
        self.append_byte(speed | (self.consolidate_flags(flags) << 6))
        return self

    # 0x11, 0x12, 0x14
    def set_object_memory_bits(self, obj, bits):
        if obj == 0x0D:
            self.append_byte(0x11)
        elif obj == 0x0B:
            self.append_byte(0x12)
        elif obj == 0x0E:
            self.append_byte(0x14)
        else:
            1/0
        self.append_byte(self.consolidate_flags(bits))
        return self

    # 0x13
    def set_vram_priority(self, val):
        self.append_byte(0x13)
        self.append_byte(val)
        return self

    # 0x15
    def set_movement_bits(self, flags):
        self.append_byte(0x15)
        self.append_byte(self.consolidate_flags(flags))
        return self

    # 0x21
    def bpl_26_27_28(self):
        self.append_byte(0x21)
        return self

    # 0x22
    def bmi_26_27_28(self):
        self.append_byte(0x21)
        return self

    # 0x26, 0x27, 0x28
    def embedded_animation_routine(self, location):
        self.append_byte(location)
        for i in range(16):
            self.append_byte(0x00)
        return self

    # 0x2A
    def bpl_26_27(self):
        self.append_byte(0x2A)
        return self

    # 0x3D
    def jmp_if_mario_in_air(self, address):
        self.append_byte(0x3D)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x3E
    def create_packet_at_object_coords_jmp_if_null(self, packet_id, object_id, address):
        self.append_byte(0x3E)
        self.append_byte(packet_id)
        self.append_byte(object_id)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x3F
    def create_packet_at_7010_coords_jmp_if_null(self, packet_id, address):
        self.append_byte(0x3F)
        self.append_byte(packet_id)
        self.append_short(self.get_branch_address(address))
        return self

    # 0x40
    def walk_1_step_east(self):
        self.append_byte(0x40)
        return self

    # 0x41
    def walk_1_step_southeast(self):
        self.append_byte(0x41)
        return self

    # 0x42
    def walk_1_step_south(self):
        self.append_byte(0x42)
        return self

    # 0x43
    def walk_1_step_southwest(self):
        self.append_byte(0x43)
        return self

    # 0x44
    def walk_1_step_west(self):
        self.append_byte(0x44)
        return self

    # 0x45
    def walk_1_step_northwest(self):
        self.append_byte(0x45)
        return self

    # 0x46
    def walk_1_step_north(self):
        self.append_byte(0x46)
        return self

    # 0x47
    def walk_1_step_northeast(self):
        self.append_byte(0x47)
        return self

    # 0x48
    def walk_1_step_f_direction(self):
        self.append_byte(0x48)
        return self

    # 0x4A
    def add_z_coord_1_step(self):
        self.append_byte(0x4A)
        return self

    # 0x4B
    def dec_z_coord_1_step(self):
        self.append_byte(0x4B)
        return self

    # 0x50
    def shift_east_steps(self, steps):
        self.append_byte(0x50)
        self.append_byte(steps)
        return self

    # 0x51
    def shift_southeast_steps(self, steps):
        self.append_byte(0x51)
        self.append_byte(steps)
        return self

    # 0x52
    def shift_south_steps(self, steps):
        self.append_byte(0x52)
        self.append_byte(steps)
        return self

    # 0x53
    def shift_southwest_steps(self, steps):
        self.append_byte(0x53)
        self.append_byte(steps)
        return self

    # 0x54
    def shift_west_steps(self, steps):
        self.append_byte(0x54)
        self.append_byte(steps)
        return self

    # 0x55
    def shift_northwest_steps(self, steps):
        self.append_byte(0x55)
        self.append_byte(steps)
        return self

    # 0x56
    def shift_north_steps(self, steps):
        self.append_byte(0x56)
        self.append_byte(steps)
        return self

    # 0x57
    def shift_northeast_steps(self, steps):
        self.append_byte(0x57)
        self.append_byte(steps)
        return self

    # 0x58
    def shift_f_direction_steps(self, steps):
        self.append_byte(0x58)
        self.append_byte(steps)
        return self

    # 0x59
    def shift_z_20_steps(self):
        self.append_byte(0x59)
        return self

    # 0x5A
    def shift_z_up_steps(self, steps):
        self.append_byte(0x5A)
        self.append_byte(steps)
        return self

    # 0x5B
    def shift_z_down_steps(self, steps):
        self.append_byte(0x5B)
        self.append_byte(steps)
        return self

    # 0x5C
    def shift_z_up_20_steps(self):
        self.append_byte(0x5C)
        return self

    # 0x5D
    def shift_z_down_20_steps(self):
        self.append_byte(0x5D)
        return self

    # 0x60
    def shift_east_pixels(self, pixels):
        self.append_byte(0x60)
        self.append_byte(pixels)
        return self

    # 0x61
    def shift_southeast_pixels(self, pixels):
        self.append_byte(0x61)
        self.append_byte(pixels)
        return self

    # 0x62
    def shift_south_pixels(self, pixels):
        self.append_byte(0x62)
        self.append_byte(pixels)
        return self

    # 0x63
    def shift_southwest_pixels(self, pixels):
        self.append_byte(0x63)
        self.append_byte(pixels)
        return self

    # 0x64
    def shift_west_pixels(self, pixels):
        self.append_byte(0x64)
        self.append_byte(pixels)
        return self

    # 0x65
    def shift_northwest_pixels(self, pixels):
        self.append_byte(0x65)
        self.append_byte(pixels)
        return self

    # 0x66
    def shift_north_pixels(self, pixels):
        self.append_byte(0x66)
        self.append_byte(pixels)
        return self

    # 0x67
    def shift_northeast_pixels(self, pixels):
        self.append_byte(0x67)
        self.append_byte(pixels)
        return self

    # 0x68
    def shift_f_direction_pixels(self, pixels):
        self.append_byte(0x68)
        self.append_byte(pixels)
        return self

    # 0x69
    def walk_f_direction_16_pixels(self):
        self.append_byte(0x69)
        return self

    # 0x6A
    def shift_z_up_pixels(self, pixels):
        self.append_byte(0x6A)
        self.append_byte(pixels)
        return self

    # 0x6B
    def shift_z_down_pixels(self, pixels):
        self.append_byte(0x6B)
        self.append_byte(pixels)
        return self

    # 0x70
    def face_east(self):
        self.append_byte(0x70)
        return self

    # 0x71
    def face_southeast(self):
        self.append_byte(0x71)
        return self

    # 0x72
    def face_south(self):
        self.append_byte(0x72)
        return self

    # 0x73
    def face_southwest(self):
        self.append_byte(0x73)
        return self

    # 0x74
    def face_west(self):
        self.append_byte(0x74)
        return self

    # 0x75
    def face_northwest(self):
        self.append_byte(0x75)
        return self

    # 0x76
    def face_north(self):
        self.append_byte(0x76)
        return self

    # 0x77
    def face_northeast(self):
        self.append_byte(0x77)
        return self

    # 0x78
    def face_mario(self):
        self.append_byte(0x78)
        return self

    # 0x79
    def turn_clockwise_45_degrees(self):
        self.append_byte(0x79)
        return self

    # 0x7A
    def turn_random_direction(self):
        self.append_byte(0x7A)
        return self

    # 0x7B
    def turn_clockwise_45_degrees_n_times(self, times):
        self.append_byte(0x7B)
        self.append_byte(times)
        return self

    # 0x7E
    def jump_to_height_silent(self, steps):
        self.append_byte(0x7E)
        self.append_short(steps)
        return self

    # 0x7F
    def jump_to_height(self, steps):
        self.append_byte(0x7F)
        self.append_short(steps)
        return self

    # 0x80
    def walk_to_xy_coords(self, x, y):
        self.append_byte(0x80)
        self.append_byte(x)
        self.append_byte(y)
        return self

    # 0x81
    def walk_xy_steps(self, x, y):
        self.append_byte(0x81)
        self.append_byte(x)
        self.append_byte(y)
        return self

    # 0x82
    def shirt_to_xy_coords(self, x, y):
        self.append_byte(0x82)
        self.append_byte(x)
        self.append_byte(y)
        return self

    # 0x83
    def shift_xy_steps(self, x, y):
        self.append_byte(0x83)
        self.append_byte(x)
        self.append_byte(y)
        return self

    # 0x84
    def shift_xy_pixels(self, x, y):
        self.append_byte(0x84)
        self.append_byte(x)
        self.append_byte(y)
        return self

    # 0x85
    def maximize_sequence_speed(self):
        self.append_byte(0x85)
        return self

    # 0x87
    def transfer_to_object_xy(self, obj):
        self.append_byte(0x87)
        self.append_byte(obj)
        return self

    # 0x88
    def run_away_shift(self):
        self.append_byte(0x88)
        return self

    # 0x89
    def run_away_transfer(self):
        self.append_byte(0x89)
        return self

    # 0x90
    def bounce_to_xy_with_height(self, x, y, height):
        self.append_byte(0x90)
        self.append_byte(x)
        self.append_byte(y)
        self.append_byte(height)
        return self

    # 0x91
    def bounce_xy_steps_with_height(self, x, y, height):
        self.append_byte(0x91)
        self.append_byte(x)
        self.append_byte(y)
        self.append_byte(height)
        return self

    # 0x92
    def transfer_to_xyzf(self, x, y, z, direction):
        self.append_byte(0x92)
        self.append_byte(x)
        self.append_byte(y)
        self.append_byte(z | (direction << 5))
        return self

    # 0x93
    def transfer_xyzf_steps(self, x, y, z, direction):
        self.append_byte(0x93)
        self.append_byte(x)
        self.append_byte(y)
        self.append_byte(z | (direction << 5))
        return self

    # 0x94
    def transfer_xyzf_pixels(self, x, y, z, direction):
        self.append_byte(0x94)
        self.append_byte(x)
        self.append_byte(y)
        self.append_byte(z | (direction << 5))
        return self

    # 0x95
    def transfer_to_object_xyz(self, obj):
        self.append_byte(0x95)
        self.append_byte(obj)
        return self

    # 0x9B
    def stop_sound(self):
        self.append_byte(0x9B)
        return self

    # 0x9C, FD 0x9E
    def play_sound(self, sound_id, channel=6):
        if channel == 4:
            self.append_byte(0xFD)
            self.append_byte(0x9E)
        else:
            self.append_byte(0x9C)
        self.append_byte(sound_id)
        return self
    # 0x9D
    def play_sound_balance(self, sound_id, balance):
        self.append_byte(0x9D)
        self.append_byte(sound_id)
        self.append_byte(balance)
        return self

    # 0x9E
    def fade_out_sound_to_volume(self, duration, volume):
        self.append_byte(0x9E)
        self.append_byte(duration)
        self.append_byte(volume)
        return self

    # 0xA0, 0xA1, 0xA2
    def set_bit(self, addr, bit):
        if addr >= 0x7080:
            cmd = 0xA2
            offset = 0x7080
        elif addr >= 0x7060:
            cmd = 0xA1
            offset = 0x7060
        else:
            cmd = 0xA0
            offset = 0x7040
        self.append_byte(cmd)
        byte_0 = (addr - offset) << 3
        self.append_byte(byte_0 | bit)
        return self

    # 0xA3
    def set_mem_704x_at_700C_bit(self):
        self.append_byte(0xA3)
        return self

    # 0xA4, 0xA5, 0xA6
    def clear_bit(self, addr, bit):
        if addr >= 0x7080:
            cmd = 0xA6
            offset = 0x7080
        elif addr >= 0x7060:
            cmd = 0xA5
            offset = 0x7060
        else:
            cmd = 0xA4
            offset = 0x7040
        self.append_byte(cmd)
        byte_0 = (addr - offset) << 3
        self.append_byte(byte_0 | bit)
        return self

    # 0xA7
    def clear_mem_704x_at_700C_bit(self):
        self.append_byte(0xA7)
        return self

    # 0xA8
    def set(self, address, value):
        if 0x70A0 <= address <= 0x719F:
            self.append_byte(0xA8)
            self.append_byte(address - 0x70A0)
            self.append_byte(value)
        elif address == 0x700C:
            self.append_byte(0xAC)
            self.append_short(value)
        return self
        
    # 0xA9, 0xAA
    def add(self, address, value):
        if 0x70A0 <= address <= 0x719F:
            if value == 1:
                self.append_byte(0xAA)
                self.append_byte(address - 0x70A0)
            else:
                self.append_byte(0xA9)
                self.append_byte(address - 0x70A0)
                self.append_byte(value)
        elif address == 0x700C:
            if (value == 0x01):
                self.append_byte(0xAE)
            else:
                self.append_byte(0xAD)
                self.append_short(value)
        else:
            1/0
        return self

    # 0xAB
    def dec(self, address):
        if 0x70A0 <= address <= 0x719F:
            self.append_byte(0xAB)
            self.append_byte(address - 0x70A0)
        elif address == 0x700C:
            self.append_byte(0xAF)
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

    # 0xB3
    def dec_short(self, address):
        assert 0x7000 <= address <= 0x71FE
        self.append_byte(0xB3)
        self.append_byte((address - 0x7000) // 2)
    
    # 0xB4, 0xB5, 0xBA, 0xBB, 0xBC
    def set_short_mem(self, address_left, address_right):
        if address_left == 0x700C and 0x70A0 <= address_right <= 0x719F:
            self.append_byte(0xB4)
            self.append_byte(address_right - 0x70A0)
        elif address_left == 0x700C and 0x7000 <= address_right <= 0x71FE:
            self.append_byte(0xBA)
            self.append_byte((address_right - 0x7000) // 2)
        elif address_right == 0x700C and 0x70A0 <= address_left <= 0x719F:
            self.append_byte(0xB5)
            self.append_byte(address_left - 0x70A0)
        elif address_right == 0x700C and 0x7000 <= address_left <= 0x71FE:
            self.append_byte(0xBB)
            self.append_byte((address_left - 0x7000) // 2)
        elif 0x7000 <= address_left <= 0x71FE and 0x7000 <= address_right <= 0x71FE:
            self.append_byte(0xBC)
            self.append_byte((address_left - 0x7000) // 2)
            self.append_byte((address_right - 0x7000) // 2)
        else:
            1/0
        return self
        
    # 0xB6, 0xB7
    def set_random(self, address, limit):
        if address == 0x700C:
            self.append_byte(0xB6)
            self.append_short(limit)
        else:
            self.append_byte(0xB7)
            self.append_byte((address - 0x7000) // 2)
            self.append_short(limit)
        return self

    # 0xB8
    def add_short_mem(self, address_left, address_right):
        if address_left == 0x700C and 0x7000 <= address_right <= 0x71FE:
            self.append_byte(0xB8)
            self.append_byte((address_right - 0x7000) // 2)
        else:
            1/0
        return self

    # 0xB9
    def dec_short_mem(self, address_left, address_right):
        if address_left == 0x700C and 0x7000 <= address_right <= 0x71FE:
            self.append_byte(0xB9)
            self.append_byte((address_right - 0x7000) // 2)
        else:
            1/0
        return self
        
    # 0xBD
    def swap_short_mem(self, address_left, address_right):
        if 0x7000 <= address_left <= 0x71FE and 0x7000 <= address_right <= 0x71FE:
            self.append_byte(0xBD)
            self.append_byte((address_left - 0x7000) // 2)
            self.append_byte((address_right - 0x7000) // 2)
        else:
            1/0
        return self
        
    # 0xBE
    def move_7010_7012_7014_to_7016_7018_701A(self, music_id):
        self.append_byte(0xBE)
        return self

    # 0xBF
    def move_7016_7018_701A_to_7010_7012_7014(self, music_id):
        self.append_byte(0xBF)
        return self

    # 0xC0, 0xC1, 0xC2
    def mem_compare(self, address, value):
        if (address == 0x700C):
            if (value >= 0x700C):
                self.append_byte(0xC1)
                self.append_byte((address - 0x700C) // 2)
            else:
                self.append_byte(0xC0)
                self.append_short(value)
        else:
            self.append_byte(0xC2)
            self.append_byte((address - 0x700C) // 2)
            self.append_short(value)
        return self

    # 0xC3
    def set_700C_to_current_level(self):
        self.append_byte(0xC3)
        return self

    # 0xC4, 0xC5, 0xC6
    def set_700C_to_object_coord(self, obj, coord, unit=0):
        val = obj | (unit << 6)
        cmd = coord + 0xC4
        self.append_byte(cmd)
        self.append_byte(val)
        return self

    # 0xCA
    def set_700C_to_pressed_button(self):
        self.append_byte(0xCA)
        return self

    # 0xCB
    def set_700C_to_tapped_button(self):
        self.append_byte(0xCB)
        return self

    # 0xD0
    def jump_to_script(self, id):
        self.append_byte(0xD0)
        self.append_short(id)
        return self

    # 0xD2
    def jmp(self, address):
        self.append_byte(0xD2)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xD3
    def jump_to_subroutine(self, id):
        self.append_byte(0xD3)
        self.append_short(id)
        return self

    # 0xD4
    def start_loop_n_times(self, count):
        self.append_byte(0xD4)
        self.append_byte(count)
        return self

    # 0xD5
    def start_loop_n_frames(self, count):
        self.append_byte(0xD5)
        self.append_short(count)
        return self

    # 0xD6
    def load_mem(self, address):
        self.append_byte(0xD6)
        self.append_byte((address - 0x7000) // 2)
        return self

    # 0xD7
    def end_loop(self):
        self.append_byte(0xD7)
        return self


    # 0xDC, 0xDD, 0xDE
    def jmp_if_bit_clear(self, addr, bit, jump):
        if addr >= 0x7080:
            cmd = 0xDE
            offset = 0x7080
        elif addr >= 0x7060:
            cmd = 0xDD
            offset = 0x7060
        else:
            cmd = 0xDC
            offset = 0x7040
        self.append_byte(cmd)
        byte_0 = (addr - offset) << 3
        self.append_byte(byte_0 | bit)
        self.append_short(jump)
        return self

    # 0xD8, 0xD9, 0xDA
    def jmp_if_bit_set(self, addr, bit, jump):
        if addr >= 0x7080:
            cmd = 0xDA
            offset = 0x7080
        elif addr >= 0x7060:
            cmd = 0xD9
            offset = 0x7060
        else:
            cmd = 0xD8
            offset = 0x7040
        self.append_byte(cmd)
        byte_0 = (addr - offset) << 3
        self.append_byte(byte_0 | bit)
        self.append_short(jump)
        return self

    # 0xDB
    def jmp_if_mem_704x_at_700C_bit_set(self, address):
        self.append_byte(0xDB)
        self.append_short(self.get_branch_address(address))

    # 0xDF
    def jmp_if_mem_704x_at_700C_bit_clear(self, address):
        self.append_byte(0xDF)
        self.append_short(self.get_branch_address(address))

    # 0xE0
    def jmp_if_var_equals_byte(self, test_addr, val, branch):
        self.db(0xE0, test_addr - 0x70A0, val)
        self.append_short(self.get_branch_address(branch))
        return self

    # 0xE1
    def jmp_if_var_not_equals_byte(self, test_addr, val, branch):
        self.db(0xE1, test_addr - 0x70A0, val)
        self.append_short(self.get_branch_address(branch))
        return self

    # 0xE2, 0xE4
    def jmp_if_var_equals_short(self, test_addr, val, branch):
        if test_addr == 0x700C:
            self.append_byte(0xE2)
        else:
            self.append_byte(0xE4)
            self.append_byte((test_addr - 0x7000) // 2)
        self.append_short(val)
        self.append_short(self.get_branch_address(branch))
        return self

    # 0xE3, 0xE5
    def jmp_if_var_not_equals_short(self, test_addr, val, branch):
        if test_addr == 0x700C:
            self.append_byte(0xE3)
        else:
            self.append_byte(0xE5)
            self.append_byte((test_addr - 0x7000) // 2)
        self.append_short(val)
        self.append_short(self.get_branch_address(branch))
        return self

    # 0xE6
    def jmp_if_700C_all_bits_clear(self, bits, address):
        self.append_byte(0xE6)
        self.append_short(self.consolidate_flags(bits))
        self.append_short(address)
        return self

    # 0xE7
    def jmp_if_700C_any_bits_set(self, bits, address):
        self.append_byte(0xE7)
        self.append_short(self.consolidate_flags(bits))
        self.append_short(address)
        return self

    # 0xE8
    def jmp_if_random_above_128(self, address):
        self.append_byte(0xE8)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xE9
    def jmp_if_random_above_66(self, address):
        self.append_byte(0xE9)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xEA
    def jmp_if_loaded_memory_is_0(self, address):
        self.append_byte(0xEA)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xEB
    def jmp_if_loaded_memory_is_not_0(self, address):
        self.append_byte(0xEB)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xEC
    def jmp_if_comparison_result_is_greater_or_equal(self, address):
        self.append_byte(0xEC)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xED
    def jmp_if_comparison_result_is_lesser(self, address):
        self.append_byte(0xED)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xEE
    def jmp_if_loaded_memory_is_below_0(self, address):
        self.append_byte(0xEE)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xEF
    def jmp_if_loaded_memory_is_above_or_equal_0(self, address):
        self.append_byte(0xEF)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xF0
    def pause(self, value):
        assert 1 <= value <= 256
        self.append_byte(0xF0)
        self.append_byte(value - 1)
        return self

    # 0xF1
    def pause_short(self, value):
        self.append_byte(0xF1)
        self.append_short(value)
        return self

    # 0xF2
    def summon_to_level(self, obj, level):
        self.append_byte(0xF2)
        self.append_short(level | (obj << 9) | (1 << 15))
        return self

    def remove_from_level(self, obj, level):
        self.append_byte(0xF2)
        self.append_short((level | (obj << 9)) & 0x7FFF)
        return self

    # 0xF3
    def enable_trigger_in_level(self, obj, level):
        self.append_byte(0xF3)
        self.append_short(level | (obj << 9) | (1 << 15))
        return self

    def disable_trigger_in_level(self, obj, level):
        self.append_byte(0xF3)
        self.append_short((level | (obj << 9)) & 0x7FFF)
        return self

    # 0xF4
    def summon_object_at_70A8_to_current_level(self, args):
        self.append_byte(0xF4)
        return self

    # 0xF5
    def remove_object_at_70A8_from_current_level(self, args):
        self.append_byte(0xF5)
        return self

    # 0xF6
    def enable_event_trigger_for_object_at_70A8(self, args):
        self.append_byte(0xF6)
        return self

    # 0xF7
    def disable_event_trigger_for_object_at_70A8(self, args):
        self.append_byte(0xF7)
        return self

    # 0xF8
    def jmp_if_object_in_level(self, obj, level, address):
        self.append_byte(0xF8)
        self.append_short(level | (obj << 9) | (1 << 15))
        self.append_short(self.get_branch_address(address))
        return self

    def jmp_if_object_not_in_level(self, obj, level, address):
        self.append_byte(0xF8)
        self.append_short((level | (obj << 9)) & 0x7FFF)
        self.append_short(self.get_branch_address(address))
        return self

    # 0xF9, 0xFA - do they need to be distinguished?
    def jump_to_start_of_this_script(self):
        self.append_byte(0xF9)
        return self

    # 0xFE
    def ret(self):
        self.append_byte(0xFE)
        return self

    # 0xFF
    def end_all(self):
        self.append_byte(0xFF)
        return self

    # FD 0x00
    def shadow_on(self):
        self.append_byte(0xFD)
        self.append_byte(0x00)
        return self

    # FD 0x01
    def shadow_off(self):
        self.append_byte(0xFD)
        self.append_byte(0x01)
        return self

    # FD 0x02
    def floating_on(self):
        self.append_byte(0xFD)
        self.append_byte(0x02)
        return self

    # FD 0x03
    def floating_off(self):
        self.append_byte(0xFD)
        self.append_byte(0x03)
        return self
    
    # FD 0x04 - 0x19
    def object_memory_set_bit(self, addr, flags):
        self.append_byte(0xFD)
        if addr == 0x08 and flags == [4]:
            self.append_byte(0x0A)
        elif addr == 0x09 and flags == [7]:
            self.append_byte(0x08)
        elif addr == 0x0B and flags == [3]:
            self.append_byte(0x17)
        elif addr == 0x0C and flags == [3, 4, 5]:
            self.append_byte(0x14)
        elif addr == 0x0D and flags == [6]:
            self.append_byte(0x19)
        elif addr == 0x0E and flags == [4]:
            self.append_byte(0x04)
        elif addr == 0x0E and flags == [5]:
            self.append_byte(0x06)
        elif addr == 0x12 and flags == [5]:
            self.append_byte(0x11)
        elif addr == 0x30 and flags == [4]:
            self.append_byte(0x0D)
        elif addr == 0x3C and flags == [6]:
            self.append_byte(0x18)
        else:
            1/0
        return self

    def object_memory_clear_bit(self, addr, flags):
        self.append_byte(0xFD)
        if addr == 0x08 and flags == [3, 4]:
            self.append_byte(0x0B)
        elif addr == 0x09 and flags == [7]:
            self.append_byte(0x09)
        elif addr == 0x0B and flags == [3]:
            self.append_byte(0x16)
        elif addr == 0x0C and flags == [3, 4, 5]:
            self.append_byte(0x13)
        elif addr == 0x0E and flags == [4]:
            self.append_byte(0x05)
        elif addr == 0x0E and flags == [5]:
            self.append_byte(0x07)
        elif addr == 0x12 and flags == [5]:
            self.append_byte(0x10)
        elif addr == 0x30 and flags == [4]:
            self.append_byte(0x0C)
        else:
            1/0
        return self

    def object_memory_modify_bits(self, addr, set_flags, clear_flags):
        self.append_byte(0xFD)
        if addr == 0x09 and set_flags == [5] and clear_flags == [4, 6]:
            self.append_byte(0x0E)
        elif addr == 0x0C and set_flags == [4] and clear_flags == [3, 4]:
            self.append_byte(0x15)
        else:
            1/0
        return self

    # FD 0x0F
    def set_priority(self, priority):
        self.append_byte(0xFD)
        self.append_byte(0x0F)
        self.append_byte(priority)
        return self

    # FD 0xB0
    def mem_700C_and_const(self, value):
        self.append_byte(0xFD)
        self.append_byte(0xB0)
        self.append_short(value)
        return self

    # FD 0xB1
    def mem_700C_or_const(self, value):
        self.append_byte(0xFD)
        self.append_byte(0xB1)
        self.append_short(value)
        return self

    # FD 0xB2
    def mem_700C_xor_const(self, value):
        self.append_byte(0xFD)
        self.append_byte(0xB2)
        self.append_short(value)
        return self

    # FD 0xB3
    def mem_700C_and_var(self, address):
        self.append_byte(0xFD)
        self.append_byte(0xB0)
        self.append_byte((address - 0x7000) // 2)
        return self

    # FD 0xB4
    def mem_700C_or_var(self, address):
        self.append_byte(0xFD)
        self.append_byte(0xB3)
        self.append_byte((address - 0x7000) // 2)
        return self

    # FD 0xB5
    def mem_700C_xor_var(self, address):
        self.append_byte(0xFD)
        self.append_byte(0xB5)
        self.append_byte((address - 0x7000) // 2)
        return self

    # FD 0xB6
    def mem_700C_shift_left(self, addr, shift):
        self.append_byte(0xFD)
        self.append_byte(0xB6)
        self.append_byte((addr - 0x7000) // 2)
        self.append_byte(256 - shift)
        return self