from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_619_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_619_jmp_if_var_not_equals_short_1',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 23, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_619_jmp_if_bit_set_2',
        "command": 'jmp_if_bit_set',
        "args": [0x7057, 0, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_619_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_619_jmp_if_bit_clear_4',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 3, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_619_transfer_to_xyzf_5',
        "command": 'transfer_to_xyzf',
        "args": [7, 47, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_619_shift_south_pixels_6',
        "command": 'shift_south_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_619_face_southwest_7',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_619_sequence_looping_off_8',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_619_ret_9',
        "command": 'ret'
    }
]
