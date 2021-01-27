from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_701_sequence_looping_on_0',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_701_set_animation_speed_1',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_701_shift_southeast_pixels_2',
        "command": 'shift_southeast_pixels',
        "args": [2]
    },
    {
        "identifier": 'ACTION_701_shift_southwest_pixels_3',
        "command": 'shift_southwest_pixels',
        "args": [9]
    },
    {
        "identifier": 'ACTION_701_set_700C_to_pressed_button_4',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_701_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_701_face_southeast_11']
    },
    {
        "identifier": 'ACTION_701_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [23, 'ACTION_701_face_southeast_11']
    },
    {
        "identifier": 'ACTION_701_jmp_if_700C_equals_short_7',
        "command": 'jmp_if_700C_equals_short',
        "args": [25, 'ACTION_701_face_southeast_11']
    },
    {
        "identifier": 'ACTION_701_jmp_if_700C_equals_short_8',
        "command": 'jmp_if_700C_equals_short',
        "args": [27, 'ACTION_701_face_southeast_11']
    },
    {
        "identifier": 'ACTION_701_face_southwest_9',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_701_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_701_face_southeast_11',
        "command": 'face_southeast'
    },
    {
        "identifier": 'ACTION_701_ret_12',
        "command": 'ret'
    }
]
