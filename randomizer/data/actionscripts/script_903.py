from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_903_face_northeast_0',
        "command": 'face_northeast'
    },
    {
        "identifier": 'ACTION_903_jump_to_height_silent_1',
        "command": 'jump_to_height_silent',
        "args": [112]
    },
    {
        "identifier": 'ACTION_903_shadow_off_2',
        "command": 'shadow_off'
    },
    {
        "identifier": 'ACTION_903_set_vram_priority_3',
        "command": 'set_vram_priority',
        "args": [VramPriority.PRIORITY_3]
    },
    {
        "identifier": 'ACTION_903_set_sprite_sequence_4',
        "command": 'set_sprite_sequence',
        "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_903_shift_f_direction_steps_5',
        "command": 'shift_f_direction_steps',
        "args": [2]
    },
    {
        "identifier": 'ACTION_903_visibility_off_6',
        "command": 'visibility_off'
    },
    {
        "identifier": 'ACTION_903_ret_7',
        "command": 'ret'
    }
]
