from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_402_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_402_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_402_jmp_if_random_above_128_2',
        "command": 'jmp_if_random_above_128',
        "args": ['ACTION_402_set_random_5']
    },
    {
        "identifier": 'ACTION_402_turn_random_direction_3',
        "command": 'turn_random_direction'
    },
    {
        "identifier": 'ACTION_402_pause_4',
        "command": 'pause',
        "args": [8]
    },
    {
        "identifier": 'ACTION_402_set_random_5',
        "command": 'set_random',
        "args": [0x700c, 2]
    },
    {
        "identifier": 'ACTION_402_inc_short_6',
        "command": 'inc_short',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_402_shift_z_20_steps_7',
        "command": 'shift_z_20_steps'
    },
    {
        "identifier": 'ACTION_402_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_402_jmp_if_random_above_128_2']
    }
]
