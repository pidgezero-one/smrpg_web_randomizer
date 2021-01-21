from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_62_object_memory_set_bit_0',
        "command": 'object_memory_set_bit',
        "args": [0x0b, [3]]
    },
    {
        "identifier": 'ACTION_62_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_62_shift_southeast_steps_2',
        "command": 'shift_southeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_62_shift_southwest_steps_3',
        "command": 'shift_southwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_62_shift_northwest_steps_4',
        "command": 'shift_northwest_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_62_shift_northeast_steps_5',
        "command": 'shift_northeast_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_62_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_62_object_memory_set_bit_0']
    }
]
