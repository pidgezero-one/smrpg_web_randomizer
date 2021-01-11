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
        val = self.consolidate_flags(flags) | (sequence_or_mold << 8) | inc_sprite
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

