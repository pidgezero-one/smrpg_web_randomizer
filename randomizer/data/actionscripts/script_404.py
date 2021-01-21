from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_404_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_404_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_404_jmp_if_random_above_66_2',
        "command": 'jmp_if_random_above_66',
        "args": ['ACTION_404_jmp_if_random_above_128_10']
    },
    {
        "identifier": 'ACTION_404_face_mario_3',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_404_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_404_pause_5',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_404_set_random_6',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_404_add_short_7',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_404_shift_z_20_steps_8',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_404_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_404_jmp_if_random_above_66_2']
    },
    {
        "identifier": 'ACTION_404_jmp_if_random_above_128_10',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_404_set_animation_speed_13']
    },
    {
        "identifier": 'ACTION_404_turn_random_direction_11',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_404_pause_12',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_404_set_animation_speed_13',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_404_set_random_14',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_404_add_short_15',
        "command": 'add_short',
        "args": [0x700c, 0x01]
    },
    {
        "identifier": 'ACTION_404_shift_z_20_steps_16',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_404_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_404_jmp_if_random_above_66_2']
    }
]
