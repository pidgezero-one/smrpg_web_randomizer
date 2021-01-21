from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_441_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_441_face_southeast_1',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_441_fixed_f_coord_off_2',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_441_sequence_looping_on_3',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_441_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_441_shift_southeast_steps_5',
        "command": 'shift_southeast_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_441_fixed_f_coord_on_6',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_441_shift_northwest_steps_7',
        "command": 'shift_northwest_steps',
        "args": [7]
    },
    {
        "identifier": 'ACTION_441_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_441_set_animation_speed_0']
    }
]
