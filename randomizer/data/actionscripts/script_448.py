from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_448_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_448_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_448_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_448_shift_northeast_steps_3',
        "command": 'shift_northeast_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_448_pause_4',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_448_shift_southwest_steps_5',
        "command": 'shift_southwest_steps',
        "args": [6]
    },
    {
        "identifier": 'ACTION_448_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_448_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_448_shift_northeast_steps_3']
    }
]
