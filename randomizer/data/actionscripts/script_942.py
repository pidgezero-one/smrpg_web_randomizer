from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_942_set_700C_to_current_level_0',
        "command": 'set_700C_to_current_level'
    },
    {
        "identifier": 'ACTION_942_jmp_if_700C_equals_short_1',
        "command": 'jmp_if_700C_equals_short',
        "args": [13, 'ACTION_942_set_700C_to_pressed_button_37']
    },
    {
        "identifier": 'ACTION_942_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_942_object_memory_set_bit_3',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_942_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_942_clear_solidity_bits_5',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_942_shift_southeast_pixels_6',
        "command": 'shift_southeast_pixels',
        "args": [7]
    },
    {
        "identifier": 'ACTION_942_shift_northeast_pixels_7',
        "command": 'shift_northeast_pixels',
        "args": [3]
    },
    {
        "identifier": 'ACTION_942_set_object_memory_bits_8',
        "command": 'set_object_memory_bits',
        "args": [0x0b, []]
    },
    {
        "identifier": 'ACTION_942_walk_1_step_northeast_9',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_942_db_10',
        "command": 'db',
        "args": [0xc8, 0x07]
    },
    {
        "identifier": 'ACTION_942_set_7000_short_mem_to_7000_short_mem_11',
        "command": 'set_7000_short_mem_to_7000_short_mem',
        "args": [0x7016, 0x7024]
    },
    {
        "identifier": 'ACTION_942_set_7000_short_mem_to_7000_short_mem_12',
        "command": 'set_7000_short_mem_to_7000_short_mem',
        "args": [0x7018, 0x7026]
    },
    {
        "identifier": 'ACTION_942_pause_13',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_942_visibility_on_14',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_942_set_solidity_bits_15',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_942_walk_1_step_southwest_16',
        "command": 'walk_1_step_southwest'
    },
    {
        "identifier": 'ACTION_942_set_solidity_bits_17',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_942_object_memory_clear_bit_18',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_942_sequence_looping_on_19',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_942_fixed_f_coord_off_20',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_942_start_loop_n_times_21',
        "command": 'start_loop_n_times',
        "args": [254]
    },
    {
        "identifier": 'ACTION_942_face_mario_22',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_942_pause_23',
        "command": 'pause',
        "args": [4]
    },
    {
        "identifier": 'ACTION_942_end_loop_24',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_942_jmp_if_bit_clear_25',
        "command": 'jmp_if_bit_clear',
        "args": [0x7055, 7, 'ACTION_942_start_loop_n_times_21']
    },
    {
        "identifier": 'ACTION_942_clear_solidity_bits_26',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_942_object_memory_set_bit_27',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_942_set_object_memory_bits_28',
        "command": 'set_object_memory_bits',
        "args": [0x0b, [0]]
    },
    {
        "identifier": 'ACTION_942_clear_solidity_bits_29',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_942_walk_1_step_northeast_30',
        "command": 'walk_1_step_northeast'
    },
    {
        "identifier": 'ACTION_942_visibility_off_31',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_942_set_7000_short_mem_to_7000_short_mem_32',
        "command": 'set_7000_short_mem_to_7000_short_mem',
        "args": [0x7024, 0x7016]
    },
    {
        "identifier": 'ACTION_942_set_7000_short_mem_to_7000_short_mem_33',
        "command": 'set_7000_short_mem_to_7000_short_mem',
        "args": [0x7026, 0x7018]
    },
    {
        "identifier": 'ACTION_942_run_away_transfer_34',
        "command": 'run_away_transfer'
    },
    {
        "identifier": 'ACTION_942_pause_short_35',
        "command": 'pause_short',
        "args": [900]
    },
    {
        "identifier": 'ACTION_942_jmp_36',
        "command": 'jmp',
        "args": ['ACTION_942_pause_13']
    },
    {
        "identifier": 'ACTION_942_set_700C_to_pressed_button_37',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_942_jmp_if_700C_equals_short_38',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_942_db_43']
    },
    {
        "identifier": 'ACTION_942_db_39',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_942_embedded_animation_routine_40',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x03, 0x80]
    },
    {
        "identifier": 'ACTION_942_pause_41',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_942_jmp_42',
        "command": 'jmp',
        "args": ['ACTION_942_pause_41']
    },
    {
        "identifier": 'ACTION_942_db_43',
        "command": 'db',
        "args": [0x20, 0x04]
    },
    {
        "identifier": 'ACTION_942_embedded_animation_routine_44',
        "command": 'embedded_animation_routine',
        "args": [0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x80, 0x00, 0x03, 0x00, 0x01, 0x00, 0x00, 0x00, 0x03, 0x80]
    },
    {
        "identifier": 'ACTION_942_pause_45',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_942_jmp_46',
        "command": 'jmp',
        "args": ['ACTION_942_pause_45']
    }
]
