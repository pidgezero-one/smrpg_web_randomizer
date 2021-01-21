from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_409_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_409_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_409_db_2',
        "command": 'db',
        "args": [0x3b, 0x00, 0x80, 0x03, 0x9a, 0x4b]
    },
    {
        "identifier": 'ACTION_409_jmp_if_random_above_128_3',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_409_jmp_if_random_above_128_10']
    },
    {
        "identifier": 'ACTION_409_face_mario_4',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_409_pause_5',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_409_set_random_6',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_409_add_short_7',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_409_shift_z_20_steps_8',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_409_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_409_db_2']
    },
    {
        "identifier": 'ACTION_409_jmp_if_random_above_128_10',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_409_set_random_13']
    },
    {
        "identifier": 'ACTION_409_turn_random_direction_11',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_409_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_409_set_random_13',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_409_add_short_14',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_409_shift_z_20_steps_15',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_409_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_409_db_2']
    },
    {
        "identifier": 'ACTION_409_clear_solidity_bits_17',
        "command": 'clear_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_409_set_priority_18',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_409_db_19',
        "command": 'db',
        "args": [0x20, 0x07]
    },
    {
        "identifier": 'ACTION_409_bpl_26_27_20',
        "command": 'bpl_26_27'
    },
    {
        "identifier": 'ACTION_409_visibility_on_21',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_409_db_22',
        "command": 'db',
        "args": [0x30, 0x00, 0x02]
    },
    {
        "identifier": 'ACTION_409_db_23',
        "command": 'db',
        "args": [0x29, 0x00]
    },
    {
        "identifier": 'ACTION_409_pause_24',
        "command": 'pause',
        "args": [192]
    },
    {
        "identifier": 'ACTION_409_bpl_26_27_28_25',
        "command": 'bpl_26_27_28'
    },
    {
        "identifier": 'ACTION_409_set_solidity_bits_26',
        "command": 'set_solidity_bits',
        "args": [[_0x0AFlags.CANT_PASS_WALLS]]
    },
    {
        "identifier": 'ACTION_409_object_memory_modify_bits_27',
        "command": 'object_memory_modify_bits',
        "args": [0x09, [5], [4, 6]]
    },
    {
        "identifier": 'ACTION_409_jmp_28',
        "command": 'jmp',
        "args": ['ACTION_409_db_2']
    }
]
