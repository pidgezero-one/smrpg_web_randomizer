from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_331_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_331_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_331_shift_southwest_steps_2',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_331_shift_northwest_steps_3',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_331_pause_4',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_331_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_331_shift_northeast_steps_6',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_331_face_southeast_7',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_331_pause_8',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_331_jmp_if_random_above_128_9',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_331_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_331_set_sprite_sequence_10',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_331_pause_11',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_331_reset_properties_12',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_331_jmp_if_random_above_128_13',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_331_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_331_shift_northwest_steps_14',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_331_pause_15',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_331_shift_southeast_steps_16',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_331_pause_17',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_331_jmp_if_random_above_128_18',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_331_shift_northwest_steps_14']
    },
    {
        "identifier": 'ACTION_331_set_sprite_sequence_19',
        "command": 'set_sprite_sequence',
        "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
    },
    {
        "identifier": 'ACTION_331_pause_20',
        "command": 'pause',
        "args": [20]
    },
    {
        "identifier": 'ACTION_331_reset_properties_21',
        "command": 'reset_properties'
    },
    {
        "identifier": 'ACTION_331_jmp_22',
        "command": 'jmp',
        "args": ['ACTION_331_set_animation_speed_0']
    }
]
