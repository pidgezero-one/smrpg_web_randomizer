from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_733_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7057, 3, 'ACTION_730_clear_solidity_bits_54']
    },
    {
        "identifier": 'ACTION_733_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_733_clear_solidity_bits_2',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_733_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7056, 5, 'ACTION_730_clear_solidity_bits_54']
    },
    {
        "identifier": 'ACTION_733_visibility_off_4',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_733_object_memory_set_bit_5',
        "command": 'object_memory_set_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_733_clear_solidity_bits_6',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
    },
    {
        "identifier": 'ACTION_733_jmp_if_var_equals_byte_7',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 25, 'ACTION_733_transfer_to_xyzf_29']
    },
    {
        "identifier": 'ACTION_733_set_bit_8',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_733_jmp_if_var_equals_byte_9',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 19, 'ACTION_733_pause_14']
    },
    {
        "identifier": 'ACTION_733_jmp_if_var_equals_byte_10',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 21, 'ACTION_733_pause_17']
    },
    {
        "identifier": 'ACTION_733_jmp_if_var_equals_byte_11',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 17, 'ACTION_733_pause_20']
    },
    {
        "identifier": 'ACTION_733_jmp_if_var_equals_byte_12',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 27, 'ACTION_733_pause_23']
    },
    {
        "identifier": 'ACTION_733_jmp_if_var_equals_byte_13',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70b5, 23, 'ACTION_733_pause_26']
    },
    {
        "identifier": 'ACTION_733_pause_14',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_733_set_15',
        "command": 'set',
        "args": [0x70b5, 21]
    },
    {
        "identifier": 'ACTION_733_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_733_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_733_pause_17',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_733_set_18',
        "command": 'set',
        "args": [0x70b5, 17]
    },
    {
        "identifier": 'ACTION_733_jmp_19',
        "command": 'jmp',
        "args": ['ACTION_733_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_733_pause_20',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_733_set_21',
        "command": 'set',
        "args": [0x70b5, 27]
    },
    {
        "identifier": 'ACTION_733_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_733_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_733_pause_23',
        "command": 'pause',
        "args": [200]
    },
    {
        "identifier": 'ACTION_733_set_24',
        "command": 'set',
        "args": [0x70b5, 23]
    },
    {
        "identifier": 'ACTION_733_jmp_25',
        "command": 'jmp',
        "args": ['ACTION_733_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_733_pause_26',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_733_set_27',
        "command": 'set',
        "args": [0x70b5, 25]
    },
    {
        "identifier": 'ACTION_733_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_733_jmp_if_bit_set_3']
    },
    {
        "identifier": 'ACTION_733_transfer_to_xyzf_29',
        "command": 'transfer_to_xyzf',
        "args": [27, 88, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_733_jmp_if_bit_set_30',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'ACTION_733_face_southwest_37']
    },
    {
        "identifier": 'ACTION_733_set_animation_speed_31',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_733_shift_southwest_steps_32',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_733_set_animation_speed_33',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_733_set_bit_34',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'ACTION_733_visibility_on_35',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_733_jmp_36',
        "command": 'jmp',
        "args": ['ACTION_733_object_memory_clear_bit_40']
    },
    {
        "identifier": 'ACTION_733_face_southwest_37',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_733_visibility_on_38',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_733_shift_southwest_steps_39',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_733_object_memory_clear_bit_40',
        "command": 'object_memory_clear_bit',
        "args": [0x30, [4]]
    },
    {
        "identifier": 'ACTION_733_set_solidity_bits_41',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_WALK_THROUGH]]
    },
    {
        "identifier": 'ACTION_733_play_sound_42',
        "command": 'play_sound',
        "args": [Sounds._011_WHOOSH_AWAY, 4]
    },
    {
        "identifier": 'ACTION_733_shift_southwest_steps_43',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_733_sequence_looping_on_44',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_733_pause_45',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_733_face_northwest_46',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_733_pause_47',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_733_face_southeast_48',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_733_pause_49',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_733_sequence_looping_off_50',
        "command": 'sequence_looping_off'
    },
    {
        "identifier": 'ACTION_733_shift_southwest_steps_51',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_733_shift_southeast_steps_52',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_733_shift_southwest_steps_53',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_733_set_54',
        "command": 'set',
        "args": [0x70b5, 19]
    },
    {
        "identifier": 'ACTION_733_jmp_55',
        "command": 'jmp',
        "args": ['ACTION_733_jmp_if_bit_set_3']
    }
]
