from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_450_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_450_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_450_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_450_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_450_pause_4',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_450_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [5]
    },
    {
        "identifier": 'ACTION_450_pause_6',
        "command": 'pause',
        "args": [16]
    },
    {
        "identifier": 'ACTION_450_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_450_shift_southeast_steps_3']
    }
]
