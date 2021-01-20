from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1688_jmp_if_bit_clear_0',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 6, 'EVENT_1688_set_short_mem_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_mem_7000_and_const_3',
        "command": 'mem_7000_and_const',
        "args": [0x0003],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x7024, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_short_mem_5',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_mem_7000_and_const_6',
        "command": 'mem_7000_and_const',
        "args": [0x000c],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_short_mem_7',
        "command": 'set_short_mem',
        "args": [0x7026, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_short_mem_8',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70ac],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_jmp_if_7000_all_bits_clear_9',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[4], 'EVENT_1688_jmp_if_7000_all_bits_clear_12'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_apply_tile_mod_10',
        "command": 'apply_tile_mod',
        "args": [Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, 32, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_bit_11',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_jmp_if_7000_all_bits_clear_12',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[5], 'EVENT_1688_jmp_if_7000_all_bits_clear_15'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_apply_tile_mod_13',
        "command": 'apply_tile_mod',
        "args": [Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, 33, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_bit_14',
        "command": 'set_bit',
        "args": [0x7043, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_jmp_if_7000_all_bits_clear_15',
        "command": 'jmp_if_7000_all_bits_clear',
        "args": [[6], 'EVENT_1688_jmp_if_bit_clear_18'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_apply_tile_mod_16',
        "command": 'apply_tile_mod',
        "args": [Rooms._420_BELOME_TEMPLE_AREA_02_FORTUNE_ROOM, 34, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_set_bit_17',
        "command": 'set_bit',
        "args": [0x7043, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_jmp_if_bit_clear_18',
        "command": 'jmp_if_bit_clear',
        "args": [0x7094, 0, 'EVENT_1688_jmp_to_event_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0xb4]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_19_SUBSCRIPT_shift_north_pixels_10',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1688_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_visibility_on_3',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_fixed_f_coord_on_4',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_floating_on_6',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_jump_to_height_7',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_db_9',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x15, 0xcc]
            },
            {
                "identifier": 'EVENT_1688_action_queue_async_20_SUBSCRIPT_shift_north_pixels_10',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1688_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7050, 7, 'EVENT_1688_jmp_to_event_23'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1688_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_inc_palette_row_by_0',
                "command": 'inc_palette_row_by',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_floating_on_4',
                "command": 'floating_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [0]
            },
            {
                "identifier": 'EVENT_1688_action_queue_sync_22_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_1688_jmp_to_event_23',
        "command": 'jmp_to_event',
        "args": [15],
        "subscript": []
    }
]
