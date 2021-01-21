from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_769_set_700C_to_pressed_button_0',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_769_add_1',
        "command": 'add',
        "args": [0x700c, 65517]
    },
    {
        "identifier": 'ACTION_769_load_mem_2',
        "command": 'load_mem',
        "args": [0x700c]
    },
    {
        "identifier": 'ACTION_769_pause_3',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'ACTION_769_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'ACTION_769_set_animation_speed_5',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
    },
    {
        "identifier": 'ACTION_769_face_mario_6',
        "command": 'face_mario'
    },
    {
        "identifier": 'ACTION_769_shift_f_direction_steps_7',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_769_jmp_8',
        "command": 'jmp',
        "args": ['ACTION_769_face_mario_6']
    }
]
