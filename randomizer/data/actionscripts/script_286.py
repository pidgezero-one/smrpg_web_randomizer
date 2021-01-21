from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_286_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_286_object_memory_set_bit_1',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_286_object_memory_set_bit_2',
        "command": 'object_memory_set_bit',
        "args": [0x0d, [6]]
    },
    {
        "identifier": 'ACTION_286_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_286_set_priority_4',
        "command": 'set_priority',
        "args": [2]
    },
    {
        "identifier": 'ACTION_286_set_700C_to_pressed_button_5',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_286_add_6',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_286_mem_700C_shift_left_7',
        "command": 'mem_700C_shift_left',
        "args": [0x7018, 255]
    },
    {
        "identifier": 'ACTION_286_load_mem_8',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_286_pause_9',
        "command": 'pause',
        "args": [23]
    },
    {
        "identifier": 'ACTION_286_end_loop_10',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_286_floating_on_11',
        "command": 'floating_on'
    },
    {
        "identifier": 'ACTION_286_jump_to_height_silent_12',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_286_pause_13',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_286_db_14',
        "command": 'db',
        "args": [0xfd, 0x3d, 0x07, 0x8d, 0x34]
    },
    {
        "identifier": 'ACTION_286_shadow_off_15',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_286_play_sound_16',
        "command": 'play_sound',
        "args": [Sounds._073_THWOMP_STOMP, 4]
    },
    {
        "identifier": 'ACTION_286_set_700C_to_pressed_button_17',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_286_add_18',
        "command": 'add',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_286_set_mem_704x_at_700C_bit_19',
        "command": 'set_mem_704x_at_700C_bit'
    },
    {
        "identifier": 'ACTION_286_pause_20',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_286_set_700C_to_pressed_button_21',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_286_add_22',
        "command": 'add',
        "args": [0x700c, 4]
    },
    {
        "identifier": 'ACTION_286_clear_mem_704x_at_700C_bit_23',
        "command": 'clear_mem_704x_at_700C_bit'
    },
    {
        "identifier": 'ACTION_286_shadow_on_24',
        "command": 'shadow_on'
    },
    {
        "identifier": 'ACTION_286_set_animation_speed_25',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_286_shift_z_up_pixels_26',
        "command": 'shift_z_up_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_286_set_700C_to_object_coord_27',
        "command": 'set_700C_to_object_coord',
        "args": [AreaObjects.DUMMY_0X07, Coords.Z, CoordUnits.PIXEL]
    },
    {
        "identifier": 'ACTION_286_jmp_if_var_not_equals_short_28',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x700c, 16, 'ACTION_286_set_animation_speed_25']
    },
    {
        "identifier": 'ACTION_286_pause_29',
        "command": 'pause',
        "args": [110]
    },
    {
        "identifier": 'ACTION_286_jmp_30',
        "command": 'jmp',
        "args": ['ACTION_286_floating_on_11']
    }
]
