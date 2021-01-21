from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_1011_fixed_f_coord_on_0',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_1011_jump_to_height_1',
        "command": 'jump_to_height',
        "args": [64]
    },
    {
        "identifier": 'ACTION_1011_set_animation_speed_2',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_1011_shift_southeast_steps_3',
        "command": 'shift_southeast_steps',
        "args": [1]
    },
    {
        "identifier": 'ACTION_1011_shift_southeast_pixels_4',
        "command": 'shift_southeast_pixels',
        "args": [8]
    },
    {
        "identifier": 'ACTION_1011_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'ACTION_1011_fixed_f_coord_off_6',
        "command": 'fixed_f_coord_off'
    },
    {
        "identifier": 'ACTION_1011_jmp_7',
        "command": 'jmp',
        "args": ['ACTION_1012_face_mario_0']
    }
]
