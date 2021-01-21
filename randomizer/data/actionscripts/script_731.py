from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_731_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 2, 'ACTION_731_jmp_if_bit_set_55']
    },
    {
        "identifier": 'ACTION_731_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 3, 'ACTION_730_clear_solidity_bits_54']
    },
    {
        "identifier": 'ACTION_731_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_731_clear_solidity_bits_3',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_731_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'ACTION_730_clear_solidity_bits_54']
    },
    {
        "identifier": 'ACTION_731_visibility_off_5',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_731_object_memory_set_bit_6',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_731_clear_solidity_bits_7',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_731_jmp_if_var_equals_byte_8',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 27, 'ACTION_731_transfer_to_xyzf_30']
    },
    {
        "identifier": 'ACTION_731_set_bit_9',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_731_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 23, 'ACTION_731_pause_15']
    },
    {
        "identifier": 'ACTION_731_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 25, 'ACTION_731_pause_18']
    },
    {
        "identifier": 'ACTION_731_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 19, 'ACTION_731_pause_21']
    },
    {
        "identifier": 'ACTION_731_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 21, 'ACTION_731_pause_24']
    },
    {
        "identifier": 'ACTION_731_jmp_if_var_equals_byte_14',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 17, 'ACTION_731_pause_27']
    },
    {
        "identifier": 'ACTION_731_pause_15',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_731_set_16',
        "command": 'set',
        "args": [0x70b5, 25]
    },
    {
        "identifier": 'ACTION_731_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_731_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_731_pause_18',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_731_set_19',
        "command": 'set',
        "args": [0x70b5, 19]
    },
    {
        "identifier": 'ACTION_731_jmp_20',
        "command": 'jmp',
        "args": ['ACTION_731_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_731_pause_21',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_731_set_22',
        "command": 'set',
        "args": [0x70b5, 21]
    },
    {
        "identifier": 'ACTION_731_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_731_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_731_pause_24',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_731_set_25',
        "command": 'set',
        "args": [0x70b5, 17]
    },
    {
        "identifier": 'ACTION_731_jmp_26',
        "command": 'jmp',
        "args": ['ACTION_731_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_731_pause_27',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_731_set_28',
        "command": 'set',
        "args": [0x70b5, 27]
    },
    {
        "identifier": 'ACTION_731_jmp_29',
        "command": 'jmp',
        "args": ['ACTION_731_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_731_transfer_to_xyzf_30',
        "command": 'transfer_to_xyzf',
        "args": [10, 31, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_731_jmp_if_bit_set_31',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_731_face_northeast_38']
    },
    {
        "identifier": 'ACTION_731_set_animation_speed_32',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_731_shift_northeast_steps_33',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_731_set_animation_speed_34',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_731_set_bit_35',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_731_visibility_on_36',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_731_jmp_37',
        "command": 'jmp',
        "args": ['ACTION_731_object_memory_clear_bit_41']
    },
    {
        "identifier": 'ACTION_731_face_northeast_38',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_731_visibility_on_39',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_731_shift_northeast_steps_40',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_731_object_memory_clear_bit_41',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_731_set_solidity_bits_42',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_731_play_sound_43',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 4]
    },
    {
        "identifier": 'ACTION_731_shift_northeast_steps_44',
        "command": 'shift_northeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_731_shift_northwest_steps_45',
        "command": 'shift_northwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_731_face_southeast_46',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_731_sequence_looping_on_47',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_731_jump_to_height_48',
        "command": 'jump_to_height',
        "args": [48]
    },
    {
        "identifier": 'ACTION_731_pause_49',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'ACTION_731_sequence_looping_off_50',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_731_shift_southwest_steps_51',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_731_shift_northwest_steps_52',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_731_set_53',
        "command": 'set',
        "args": [0x70b5, 23]
    },
    {
        "identifier": 'ACTION_731_jmp_54',
        "command": 'jmp',
        "args": ['ACTION_731_jmp_if_bit_set_4']
    },
    {
        "identifier": 'ACTION_731_jmp_if_bit_set_55',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 4, 'ACTION_731_ret_59']
    },
    {
        "identifier": 'ACTION_731_visibility_off_56',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_731_object_memory_set_bit_57',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_731_clear_solidity_bits_58',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_731_ret_59',
        "command": 'ret'
    }
]
