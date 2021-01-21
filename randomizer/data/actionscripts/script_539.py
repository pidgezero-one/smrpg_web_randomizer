from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_539_floating_off_0',
        "command": 'floating_off'
    },
    {
        "identifier": 'ACTION_539_sequence_looping_on_1',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_539_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_539_set_animation_speed_3',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_539_face_mario_4',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_539_pause_5',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_539_shift_f_direction_steps_6',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_539_pause_7',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'ACTION_539_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_539_floating_off_0']
    }
]
