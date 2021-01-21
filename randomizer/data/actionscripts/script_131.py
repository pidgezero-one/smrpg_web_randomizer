from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_131_set_priority_0',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_131_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_131_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_131_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_131_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 4, 'ACTION_131_shift_northwest_steps_6']
    },
    {
        "identifier": 'ACTION_131_jmp_5',
        "command": 'jmp',
        "args": ['ACTION_131_pause_3']
    },
    {
        "identifier": 'ACTION_131_shift_northwest_steps_6',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_131_pause_7',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_131_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 3, 'ACTION_131_set_priority_0']
    },
    {
        "identifier": 'ACTION_131_jmp_9',
        "command": 'jmp',
        "args": ['ACTION_131_pause_7']
    }
]
