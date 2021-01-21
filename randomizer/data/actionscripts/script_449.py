from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_449_shadow_off_0',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_449_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_449_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_449_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_449_pause_4',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_449_shift_northwest_steps_5',
        "command": 'shift_northwest_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_449_pause_6',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'ACTION_449_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_449_shift_southeast_steps_3']
    }
]
