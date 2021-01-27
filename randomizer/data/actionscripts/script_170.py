from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_170_face_southwest_0',
        "command": 'face_southwest'
    },
    {
        "identifier": 'ACTION_170_fixed_f_coord_on_1',
        "command": 'fixed_f_coord_on'
    },
    {
        "identifier": 'ACTION_170_set_vram_priority_2',
        "command": 'set_vram_priority',
        "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_170_set_priority_3',
        "command": 'set_priority',
        "args": [3]
    },
    {
        "identifier": 'ACTION_170_sequence_looping_on_4',
        "command": 'sequence_looping_on'
    },
    {
        "identifier": 'ACTION_170_add_short_5',
        "command": 'add_short',
        "args": [0x701a, 0x0002]
    },
    {
        "identifier": 'ACTION_170_db_6',
        "command": 'db',
        "args": [0x9a]
    },
    {
        "identifier": 'ACTION_170_set_animation_speed_7',
        "command": 'set_animation_speed',
        "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
    },
    {
        "identifier": 'ACTION_170_shift_east_pixels_8',
        "command": 'shift_east_pixels',
        "args": [4]
    },
    {
        "identifier": 'ACTION_170_set_object_memory_bits_9',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [3]]
    },
    {
        "identifier": 'ACTION_170_visibility_on_10',
        "command": 'visibility_on'
    },
    {
        "identifier": 'ACTION_170_ret_11',
        "command": 'ret'
    }
]
