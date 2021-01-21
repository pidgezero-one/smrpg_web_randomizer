from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_53_set_animation_speed_0',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_53_shift_z_up_steps_1',
        "command": 'shift_z_up_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_53_face_mario_2',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_53_pause_3',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'ACTION_53_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_53_shift_z_down_steps_5',
        "command": 'shift_z_down_steps',
        "args": [8]
    },
    {
        "identifier": 'ACTION_53_jump_to_height_silent_6',
        "command": 'jump_to_height_silent',
        "args": [0]
    },
    {
        "identifier": 'ACTION_53_set_bit_7',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'ACTION_53_play_sound_8',
        "command": 'play_sound',
        "args": [0xff, 6]
    },
    {
        "identifier": 'ACTION_53_pause_9',
        "command": 'pause',
        "args": [120]
    },
    {
        "identifier": 'ACTION_53_jmp_10',
        "command": 'jmp',
        "args": ['ACTION_53_set_animation_speed_0']
    }
]
