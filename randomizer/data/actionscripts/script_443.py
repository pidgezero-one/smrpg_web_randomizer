from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_443_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_443_set_object_memory_bits_1',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [1]]
    },
    {
        "identifier": 'ACTION_443_object_memory_set_bit_2',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_443_shadow_off_3',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_443_face_mario_4',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_443_start_loop_n_times_5',
        "command": 'start_loop_n_times',
        "args": [7]
    },
    {
        "identifier": 'ACTION_443_set_700C_to_pressed_button_6',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_443_dec_7',
        "command": 'dec',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_443_dec_8',
        "command": 'dec',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_443_set_70A0_short_mem_to_700C_9',
        "command": 'set_70A0_short_mem_to_700C',
        "args": [0x70a9]
    },
    {
        "identifier": 'ACTION_443_db_10',
        "command": 'db',
        "args": [0xc8, 0x11]
    },
    {
        "identifier": 'ACTION_443_add_short_11',
        "command": 'add_short',
        "args": [0x701a, 0x00c0]
    },
    {
        "identifier": 'ACTION_443_add_short_12',
        "command": 'add_short',
        "args": [0x7016, 0x0040]
    },
    {
        "identifier": 'ACTION_443_add_short_13',
        "command": 'add_short',
        "args": [0x7018, 0x0030]
    },
    {
        "identifier": 'ACTION_443_db_14',
        "command": 'db',
        "args": [0x99]
    },
    {
        "identifier": 'ACTION_443_end_loop_15',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_443_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_443_face_mario_4']
    }
]
