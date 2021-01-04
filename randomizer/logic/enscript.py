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

    # 0xD1
    def call_event(self, script_id):
        self.append_byte(0xD1)
        self.append_short(script_id)
        return self

    # 0xAB
    def dec(self, address):
        assert 0x70A0 <= address <= 0x719F
        self.append_byte(0xAB)
        self.append_byte(address - 0x70A0)

    # 0xB3
    def dec_short(self, address):
        assert 0x7000 <= address <= 0x71FE
        self.append_byte(0xB3)
        self.append_byte((address - 0x7000) // 2)

    # 0x34
    def enable_controls_until_return(self, *directions):
        enabled_directions = 0x00
        for i in directions:
            enabled_directions |= 1 << i
        assert 0x00 <= enabled_directions <= 0xFF
        return self

    # 0x68
    def enter_area(self, room, run_entrance_event, show_message, is_z_half, direction, x, y, z):
        #print(room, run_entrance_event, show_message, is_z_half, direction, x, y, z)
        room_short = room & (run_entrance_event << 15) & (show_message << 11)
        self.append_short(room_short)
        self.append_byte(x)
        y_zhalf = y & (is_z_half << 7)
        self.append_byte(y_zhalf)
        z_direction = z & (direction << 4)
        self.append_byte(z_direction)
        return self

    # 0x30
    def freeze_all_npcs_until_return(self):
        self.append_byte(0x30)
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

    # 0xF0
    def pause(self, value):
        self.append_byte(value)
        return self

    # 0x9C
    def play_sound(self, sound_id):
        self.append_byte(0x9C)
        self.append_byte(sound_id)
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

    # 0xFE
    def ret(self):
        self.append_byte(0xFE)
        return self

    # 0x60
    def run_dialog(self, dialog_id, bit, flags):
        self.append_byte(0x60)
        self.append_short(dialog_id | bit << 15)
        self.append_byte(flags)
        return self

    # 0xA8
    def set(self, address, value):
        assert 0x70A0 <= address <= 0x719F
        self.append_byte(0xA8)
        self.append_byte(address - 0x70A0)
        self.append_byte(value)

    # 0x9B
    def stop_sound(self):
        self.append_byte(0x9B)
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


"""   def animate_object(self, character_object, length, actions):
    self.append_byte(character_object)
    self.append_byte(length)
    for action in actions:
      self.append_byte(action)
    return self """
