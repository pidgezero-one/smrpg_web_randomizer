from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_532_set_7000_to_current_level_0',
        "command": 'set_7000_to_current_level'
    },
    {
        "identifier": 'EVENT_532_jmp_if_var_equals_short_1',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 98, 'EVENT_532_set_bit_20']
    },
    {
        "identifier": 'EVENT_532_set_2',
        "command": 'set',
        "args": [0x70a9, 21]
    },
    {
        "identifier": 'EVENT_532_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_256_ret_0']
    },
    {
        "identifier": 'EVENT_532_set_bit_4',
        "command": 'set_bit',
        "args": [0x7043, 0]
    },
    {
        "identifier": 'EVENT_532_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._009_GREEN_SWITCH, 6]
    },
    {
        "identifier": 'EVENT_532_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MEM_70A9],
        "subscript": [
            {
                "identifier": 'EVENT_532_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_532_action_queue_sync_6_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_532_action_queue_sync_6_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_532_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_532_action_queue_sync_7_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_532_action_queue_sync_7_SUBSCRIPT_shift_z_down_pixels_1',
                "command": 'shift_z_down_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_532_action_queue_sync_7_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_532_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7060, 4, 'EVENT_532_apply_tile_mod_13']
    },
    {
        "identifier": 'EVENT_532_set_bit_9',
        "command": 'set_bit',
        "args": [0x7060, 4]
    },
    {
        "identifier": 'EVENT_532_pause_10',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_532_jmp_to_subroutine_11',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_532_play_sound_17']
    },
    {
        "identifier": 'EVENT_532_jmp_if_bit_set_12',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_532_apply_tile_mod_27']
    },
    {
        "identifier": 'EVENT_532_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_532_apply_solidity_mod_14',
        "command": 'apply_solidity_mod',
        "args": [Rooms._083_ROSE_TOWN_DURING_BOWYER_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_532_jmp_15',
        "command": 'jmp',
        "args": ['EVENT_529_clear_bit_48']
    },
    {
        "identifier": 'EVENT_532_ret_16',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_532_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._021_RUMBLING, 6]
    },
    {
        "identifier": 'EVENT_532_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_north_pixels_4',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_south_pixels_8',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_532_action_queue_async_18_SUBSCRIPT_shift_north_pixels_9',
                "command": 'shift_north_pixels',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_532_ret_19',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_532_set_bit_20',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_532_set_21',
        "command": 'set',
        "args": [0x70a9, 20]
    },
    {
        "identifier": 'EVENT_532_jmp_22',
        "command": 'jmp',
        "args": ['EVENT_532_jmp_if_bit_set_3']
    },
    {
        "identifier": 'EVENT_532_apply_tile_mod_23',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_532_apply_solidity_mod_24',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_532_jmp_25',
        "command": 'jmp',
        "args": ['EVENT_529_clear_bit_48']
    },
    {
        "identifier": 'EVENT_532_ret_26',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_532_apply_tile_mod_27',
        "command": 'apply_tile_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 0, []]
    },
    {
        "identifier": 'EVENT_532_apply_solidity_mod_28',
        "command": 'apply_solidity_mod',
        "args": [Rooms._084_ROSE_TOWN_OUTSIDE, 0, []]
    },
    {
        "identifier": 'EVENT_532_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_529_clear_bit_48']
    },
    {
        "identifier": 'EVENT_532_ret_30',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_532_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_stop_sound_42',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_532_ret_43',
        "command": 'ret'
    }
]
