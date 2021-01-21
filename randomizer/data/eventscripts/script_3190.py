from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3190_stop_all_background_events_0',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_3190_set_bit_1',
        "command": 'set_bit',
        "args": [0x7057, 4]
    },
    {
        "identifier": 'EVENT_3190_clear_bit_2',
        "command": 'clear_bit',
        "args": [0x7052, 1]
    },
    {
        "identifier": 'EVENT_3190_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_sync_3_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.NORMAL]
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_async_4_SUBSCRIPT_floating_off_0',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_4_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_4_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [11, 61]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_4_SUBSCRIPT_set_solidity_bits_3',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_4_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_4_SUBSCRIPT_floating_on_5',
                "command": 'floating_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_set_action_script_async_5',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_1, 15]
    },
    {
        "identifier": 'EVENT_3190_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_async_6_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [12, 61]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_6_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_set_7',
        "command": 'set',
        "args": [0x70ae, 21]
    },
    {
        "identifier": 'EVENT_3190_set_temp_action_script_async_8',
        "command": 'set_temp_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_3190_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_async_9_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [54]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_9_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_9_SUBSCRIPT_jump_to_height_2',
                "command": 'jump_to_height',
                "args": [54]
            },
            {
                "identifier": 'EVENT_3190_action_queue_async_9_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_walk_1_step_northeast_3',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_4',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_jmp_if_bit_clear_6',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 6, 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_5']
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_sequence_looping_off_8',
                "command": 'sequence_looping_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_sequence_playback_off_9',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_southeast_pixels_10',
                "command": 'shift_southeast_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_south_pixels_11',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_12',
                "command": 'shift_southwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_west_pixels_13',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_z_up_pixels_14',
                "command": 'shift_z_up_pixels',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_face_southwest_16',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_on_17',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shadow_off_18',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_bounce_to_xy_with_height_19',
                "command": 'bounce_to_xy_with_height',
                "args": [12, 62, 2]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_southwest_pixels_20',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_shift_z_down_pixels_21',
                "command": 'shift_z_down_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_fixed_f_coord_off_22',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_clear_solidity_bits_23',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_WALK_THROUGH]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_floating_off_24',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_25',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_jmp_if_bit_clear_26',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 5, 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_pause_25']
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_10_SUBSCRIPT_set_object_memory_bits_27',
                "command": 'set_object_memory_bits',
                "args": [0x0e, bits=[0]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_jump_to_height_0',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 61]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_bit_5',
                "command": 'set_bit',
                "args": [0x7044, 6]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_east_6',
                "command": 'face_east'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_south_10',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_reset_properties_16',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_southwest_17',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_northeast_19',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_walk_1_step_northeast_20',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_bit_21',
                "command": 'set_bit',
                "args": [0x7044, 2]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_22',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_jmp_if_bit_clear_23',
                "command": 'jmp_if_bit_clear',
                "args": [0x7044, 1, 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_22']
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_face_southwest_24',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_walk_1_step_southwest_25',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_26',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_27',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_jump_to_height_28',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_29',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_animation_speed_30',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_shift_southwest_pixels_31',
                "command": 'shift_southwest_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_shadow_off_32',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_pause_33',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_vram_priority_34',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_floating_off_35',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_animation_speed_36',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_37',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=6, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_11_SUBSCRIPT_set_bit_38',
                "command": 'set_bit',
                "args": [0x7044, 5]
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_pause_12',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3190_jmp_if_bit_clear_13',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 2, 'EVENT_3190_pause_12']
    },
    {
        "identifier": 'EVENT_3190_set_bit_14',
        "command": 'set_bit',
        "args": [0x7044, 1]
    },
    {
        "identifier": 'EVENT_3190_pause_15',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3190_jmp_if_bit_clear_16',
        "command": 'jmp_if_bit_clear',
        "args": [0x7044, 5, 'EVENT_3190_pause_15']
    },
    {
        "identifier": 'EVENT_3190_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_embedded_animation_routine_3',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_embedded_animation_routine_4',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._048_MINECART_START, 4]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_17_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [200]
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_embedded_animation_routine_2',
                "command": 'embedded_animation_routine',
                "args": [0x26]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_embedded_animation_routine_3',
                "command": 'embedded_animation_routine',
                "args": [0x27]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_embedded_animation_routine_4',
                "command": 'embedded_animation_routine',
                "args": [0x28]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [200]
            },
            {
                "identifier": 'EVENT_3190_action_queue_sync_18_SUBSCRIPT_set_bit_6',
                "command": 'set_bit',
                "args": [0x7043, 0]
            }
        ]
    },
    {
        "identifier": 'EVENT_3190_pause_19',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3190_jmp_if_bit_clear_20',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 0, 'EVENT_3190_pause_19']
    },
    {
        "identifier": 'EVENT_3190_close_dialog_21',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_3190_fade_out_to_black_async_22',
        "command": 'fade_out_to_black_async'
    },
    {
        "identifier": 'EVENT_3190_remove_from_level_23',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._284_MOLEVILLE_MINES_AREA_18_MINECART_ROOM]
    },
    {
        "identifier": 'EVENT_3190_store_7000_minecart_timer_24',
        "command": 'store_7000_minecart_timer'
    },
    {
        "identifier": 'EVENT_3190_set_short_mem_25',
        "command": 'set_short_mem',
        "args": [0x702e, 0x7000]
    },
    {
        "identifier": 'EVENT_3190_stop_sound_26',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_27',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_28',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_29',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_30',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_31',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_32',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_33',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_34',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_35',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_36',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_37',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_38',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_39',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_40',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_3190_run_moleville_mountain_sequence_42',
        "command": 'run_moleville_mountain_sequence'
    },
    {
        "identifier": 'EVENT_3190_enter_area_43',
        "command": 'enter_area',
        "args": [Rooms._108_MOLEVILLE_OUTSIDE, RadialDirections.SOUTH, 0, 0, 0, []]
    },
    {
        "identifier": 'EVENT_3190_run_event_as_subroutine_44',
        "command": 'run_event_as_subroutine',
        "args": [1394]
    },
    {
        "identifier": 'EVENT_3190_set_bit_45',
        "command": 'set_bit',
        "args": [0x7044, 6]
    },
    {
        "identifier": 'EVENT_3190_jmp_to_event_46',
        "command": 'jmp_to_event',
        "args": [1648]
    }
]
