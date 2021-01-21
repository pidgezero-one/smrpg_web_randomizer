from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_618_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_618_jmp_if_var_not_equals_short_1',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 22, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_618_jmp_if_bit_clear_2',
        "command": 'jmp_if_bit_clear',
        "args": [0x7056, 4, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_618_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 7, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_618_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_618_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 2, 'ACTION_618_shirt_to_xy_coords_12']
    },
    {
        "identifier": 'ACTION_618_jmp_if_bit_clear_6',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 3, 'ACTION_617_visibility_off_10']
    },
    {
        "identifier": 'ACTION_618_transfer_to_xyzf_7',
        "command": 'transfer_to_xyzf',
        "args": [9, 20, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_618_shift_northeast_pixels_8',
        "command": 'shift_northeast_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_618_face_southeast_9',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_618_sequence_looping_off_10',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_618_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_618_shirt_to_xy_coords_12',
        "command": 'shirt_to_xy_coords',
        "args": [4, 24]
    },
    {
        "identifier": 'ACTION_618_visibility_on_13',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_618_face_mario_14',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_618_sequence_looping_on_15',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_618_sequence_playback_on_16',
        "command": 'sequence_playback_on'
    },
    {
        "identifier": 'ACTION_618_ret_17',
        "command": 'ret'
    }
]
