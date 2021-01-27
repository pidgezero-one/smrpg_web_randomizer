from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_648_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_648_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_648_add_2',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_648_load_mem_3',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_648_pause_4',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_648_end_loop_5',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_648_set_animation_speed_6',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_648_start_loop_n_times_7',
        "command": 'start_loop_n_times',
        "args": [3]
    },
    {
        "identifier": 'ACTION_648_shift_z_up_pixels_8',
        "command": 'shift_z_up_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_648_shift_z_down_pixels_9',
        "command": 'shift_z_down_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_648_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_648_set_700C_to_pressed_button_11',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_648_jmp_if_700C_equals_short_12',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_648_face_northwest_15']
    },
    {
        "identifier": 'ACTION_648_face_southeast_13',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_648_jmp_14',
        "command": 'jmp',
        "args": ['ACTION_648_set_animation_speed_16']
    },
    {
        "identifier": 'ACTION_648_face_northwest_15',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_648_set_animation_speed_16',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_648_pause_17',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_648_face_northeast_18',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_648_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_648_set_animation_speed_6']
    },
    {
        "identifier": 'ACTION_648_ret_20',
        "command": 'ret'
    }
]
