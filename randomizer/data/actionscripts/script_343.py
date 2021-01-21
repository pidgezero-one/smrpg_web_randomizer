from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_343_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_343_shift_f_direction_steps_1',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_343_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_343_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_343_pause_3',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_343_jmp_if_random_above_128_4',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_343_set_animation_speed_0']
    },
    {
        "identifier": 'ACTION_343_turn_random_direction_5',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_343_jmp_6',
        "command": 'jmp',
        "args": ['ACTION_343_set_animation_speed_0']
    }
]
