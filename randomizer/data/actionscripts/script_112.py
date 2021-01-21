from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_112_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_112_visibility_off_1',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_112_pause_2',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_112_clear_bit_3',
        "command": 'clear_bit',
        "args": [0x7043, 1]
    },
    {
        "identifier": 'ACTION_112_visibility_on_4',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_112_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_112_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_112_pause_7',
        "command": 'pause',
        "args": [150]
    },
    {
        "identifier": 'ACTION_112_set_bit_8',
        "command": 'set_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_112_pause_9',
        "command": 'pause',
        "args": [100]
    },
    {
        "identifier": 'ACTION_112_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_112_shift_northwest_steps_11',
        "command": 'shift_northwest_steps',
        "args": [9]
    },
    {
        "identifier": 'ACTION_112_visibility_off_12',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_112_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7043, 2]
    },
    {
        "identifier": 'ACTION_112_pause_14',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_112_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 1, 'ACTION_112_pause_2']
    },
    {
        "identifier": 'ACTION_112_jmp_16',
        "command": 'jmp',
        "args": ['ACTION_112_pause_14']
    }
]
