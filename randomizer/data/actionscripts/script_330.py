from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_330_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_330_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_330_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_330_face_southwest_3',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_330_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_330_pause_5',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_330_reset_properties_6',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_330_shift_northwest_steps_7',
        "command": 'shift_northwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_330_pause_8',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_330_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_330_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_330_shift_southwest_steps_10',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_330_face_northwest_11',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_330_pause_12',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_330_shift_northeast_steps_13',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_330_face_northwest_14',
        "command": 'face_northwest'
    },
    {
        "identifier": 'ACTION_330_pause_15',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_330_jmp_if_random_above_128_16',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_330_shift_southwest_steps_10']
    },
    {
        "identifier": 'ACTION_330_jmp_17',
        "command": 'jmp',
        "args": ['ACTION_330_set_animation_speed_0']
    }
]
