from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_530_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_530_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTER, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_530_shift_northwest_steps_2',
        "command": 'shift_northwest_steps',
        "args": [10]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_530_shift_northwest_steps_4',
        "command": 'shift_northwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_530_visibility_off_7',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_530_shirt_to_xy_coords_8',
        "command": 'shirt_to_xy_coords',
        "args": [12, 11]
    },
    {
        "identifier": 'ACTION_530_visibility_on_9',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_10',
        "command": 'shift_southwest_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_530_shift_southeast_steps_11',
        "command": 'shift_southeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_12',
        "command": 'shift_southwest_steps',
        "args": [3]
    },
    {
        "identifier": 'ACTION_530_shift_southeast_steps_13',
        "command": 'shift_southeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_530_shift_northeast_steps_14',
        "command": 'shift_northeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_southeast_steps_15',
        "command": 'shift_southeast_steps',
        "args": [4]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_16',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_southeast_steps_17',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_18',
        "command": 'shift_southwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_southeast_steps_19',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_20',
        "command": 'shift_southwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_530_shift_northwest_steps_21',
        "command": 'shift_northwest_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_530_shift_southwest_steps_22',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_530_jmp_23',
        "command": 'jmp',
        "args": ['ACTION_530_shift_northwest_steps_2']
    }
]
