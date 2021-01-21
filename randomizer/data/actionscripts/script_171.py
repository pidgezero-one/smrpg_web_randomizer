from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_171_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_171_set_priority_1',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_171_sequence_looping_on_2',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_171_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x707b, 0, 'ACTION_171_set_animation_speed_11']
    },
    {
        "identifier": 'ACTION_171_set_animation_speed_4',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_171_set_sprite_sequence_5',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_171_jump_to_height_6',
        "command": 'jump_to_height',
        "args": [80]
    },
    {
        "identifier": 'ACTION_171_face_east_7',
        "command": 'face_east'
    },
    {
        "identifier": 'ACTION_171_shift_f_direction_pixels_8',
        "command": 'shift_f_direction_pixels',
        "args": [48]
    },
    {
        "identifier": 'ACTION_171_visibility_off_9',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_171_ret_10',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_171_set_animation_speed_11',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_171_set_sprite_sequence_12',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_171_jump_to_height_13',
        "command": 'jump_to_height',
        "args": [96]
    },
    {
        "identifier": 'ACTION_171_shift_southeast_pixels_14',
        "command": 'shift_southeast_pixels',
        "args": [17]
    },
    {
        "identifier": 'ACTION_171_visibility_off_15',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_171_ret_16',
        "command": 'ret'
    }
]
