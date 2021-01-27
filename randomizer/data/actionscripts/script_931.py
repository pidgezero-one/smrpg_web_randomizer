from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data.eventtables import RadialDirections, AreaObjects, NPCPackets, Sounds, Coords, CoordUnits, Rooms
script = [
    {
        "identifier": 'ACTION_931_set_vram_priority_0',
        "command": 'set_vram_priority',
        "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
    },
    {
        "identifier": 'ACTION_931_set_700C_to_pressed_button_1',
        "command": 'set_700C_to_pressed_button'
    },
    {
        "identifier": 'ACTION_931_jmp_if_700C_equals_short_2',
        "command": 'jmp_if_700C_equals_short',
        "args": [21, 'ACTION_931_transfer_xyzf_pixels_8']
    },
    {
        "identifier": 'ACTION_931_jmp_if_700C_equals_short_3',
        "command": 'jmp_if_700C_equals_short',
        "args": [22, 'ACTION_931_transfer_xyzf_pixels_12']
    },
    {
        "identifier": 'ACTION_931_jmp_if_700C_equals_short_4',
        "command": 'jmp_if_700C_equals_short',
        "args": [23, 'ACTION_931_set_vram_priority_16']
    },
    {
        "identifier": 'ACTION_931_jmp_if_700C_equals_short_5',
        "command": 'jmp_if_700C_equals_short',
        "args": [24, 'ACTION_931_set_vram_priority_21']
    },
    {
        "identifier": 'ACTION_931_jmp_if_700C_equals_short_6',
        "command": 'jmp_if_700C_equals_short',
        "args": [25, 'ACTION_931_set_vram_priority_26']
    },
    {
        "identifier": 'ACTION_931_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_931_transfer_xyzf_pixels_8',
        "command": 'transfer_xyzf_pixels',
        "args": [16, 16, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_931_set_sprite_sequence_9',
        "command": 'set_sprite_sequence',
        "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_931_set_object_memory_bits_10',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0]]
    },
    {
        "identifier": 'ACTION_931_ret_11',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_931_transfer_xyzf_pixels_12',
        "command": 'transfer_xyzf_pixels',
        "args": [16, 48, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_931_set_sprite_sequence_13',
        "command": 'set_sprite_sequence',
        "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_931_set_object_memory_bits_14',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [1]]
    },
    {
        "identifier": 'ACTION_931_ret_15',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_931_set_vram_priority_16',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_931_transfer_xyzf_pixels_17',
        "command": 'transfer_xyzf_pixels',
        "args": [224, 21, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_931_set_sprite_sequence_18',
        "command": 'set_sprite_sequence',
        "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_931_set_object_memory_bits_19',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0, 1]]
    },
    {
        "identifier": 'ACTION_931_ret_20',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_931_set_vram_priority_21',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_931_transfer_xyzf_pixels_22',
        "command": 'transfer_xyzf_pixels',
        "args": [224, 53, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_931_set_sprite_sequence_23',
        "command": 'set_sprite_sequence',
        "args": [3, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_931_set_object_memory_bits_24',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [2]]
    },
    {
        "identifier": 'ACTION_931_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'ACTION_931_set_vram_priority_26',
        "command": 'set_vram_priority',
        "args": [VramPriority.NORMAL]
    },
    {
        "identifier": 'ACTION_931_transfer_xyzf_pixels_27',
        "command": 'transfer_xyzf_pixels',
        "args": [0, 37, 0, RadialDirections.EAST]
    },
    {
        "identifier": 'ACTION_931_set_sprite_sequence_28',
        "command": 'set_sprite_sequence',
        "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
    },
    {
        "identifier": 'ACTION_931_set_object_memory_bits_29',
        "command": 'set_object_memory_bits',
        "args": [0x0e, [0, 2]]
    },
    {
        "identifier": 'ACTION_931_ret_30',
        "command": 'ret'
    }
]
