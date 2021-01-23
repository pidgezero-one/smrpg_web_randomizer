from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3839_set_bit_0',
        "command": 'set_bit',
        "args": [0x7080, 7]
    },
    {
        "identifier": 'EVENT_3839_enter_area_1',
        "command": 'enter_area',
        "args": [Rooms._219_GAME_INTRO_SEA_SHORE_WITH_SUNKEN_SHIP, RadialDirections.SOUTHWEST, 12, 29, 6, []]
    },
    {
        "identifier": 'EVENT_3839_fade_in_from_black_async_2',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3839_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3839_action_queue_sync_3_SUBSCRIPT_walk_1_step_southwest_0',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_3_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_3_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_3_SUBSCRIPT_walk_1_step_southwest_3',
                "command": 'walk_1_step_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3839_pause_4',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3839_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Z, [], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_3839_mem_compare_val_6',
        "command": 'mem_compare_val',
        "args": [1296]
    },
    {
        "identifier": 'EVENT_3839_jmp_if_comparison_result_is_greater_or_equal_7',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_3839_pause_4']
    },
    {
        "identifier": 'EVENT_3839_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [5, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_transfer_to_object_xy_3',
                "command": 'transfer_to_object_xy',
                "args": [AreaObjects.MARIO]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_shift_xy_pixels_4',
                "command": 'shift_xy_pixels',
                "args": [0, 8]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_set_object_memory_bits_5',
                "command": 'set_object_memory_bits',
                "args": [0x0e, [2, 3]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_8_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3839_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [13, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_walk_1_step_south_5',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_vram_priority_6',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_walk_1_step_south_8',
                "command": 'walk_1_step_south'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [13, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_10',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [12, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_12',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [14, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_14',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [11, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_16',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_reset_properties_17',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_inc_palette_row_by_18',
                "command": 'inc_palette_row_by',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_object_memory_modify_bits_19',
                "command": 'object_memory_modify_bits',
                "args": [0x0c, [4], [3, 5]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_face_north_20',
                "command": 'face_north'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_vram_priority_21',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_start_loop_n_times_22',
                "command": 'start_loop_n_times',
                "args": [35]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_turn_clockwise_45_degrees_n_times_23',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_z_down_pixels_24',
                "command": 'shift_z_down_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_end_loop_25',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_floating_on_26',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_animation_speed_27',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_walk_1_step_southwest_28',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_29',
                "command": 'jump_to_height_silent',
                "args": [34]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_southwest_steps_30',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_bit_31',
                "command": 'set_bit',
                "args": [0x7044, 7]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_shift_southwest_steps_32',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3839_action_queue_sync_9_SUBSCRIPT_set_animation_speed_33',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3839_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3839_jmp_if_bit_clear_11',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 7, 'EVENT_3839_pause_10']
    },
    {
        "identifier": 'EVENT_3839_fade_out_to_black_async_duration_12',
        "command": 'fade_out_to_black_async_duration',
        "args": [30]
    },
    {
        "identifier": 'EVENT_3839_clear_bit_13',
        "command": 'clear_bit',
        "args": [0x7080, 7]
    },
    {
        "identifier": 'EVENT_3839_jmp_to_event_14',
        "command": 'jmp_to_event',
        "args": [145]
    }
]
