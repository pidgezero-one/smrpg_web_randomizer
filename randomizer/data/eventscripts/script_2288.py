from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2288_enter_area_0',
        "command": 'enter_area',
        "args": [Rooms._246_GAME_INTRO_KERO_SEWERS_ENTRANCE, RadialDirections.SOUTHEAST, 4, 18, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_freeze_camera_1',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_async_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_2_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_fade_in_from_black_async_3',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_pause_4',
        "command": 'pause',
        "args": [15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_action_queue_async_5',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_async_5_SUBSCRIPT_jump_to_height_silent_0',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_5_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_5_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_5_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_5_SUBSCRIPT_face_south_4',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_pause_6',
        "command": 'pause',
        "args": [5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_set_short_7',
        "command": 'set_short',
        "args": [0x7016, 0x0005],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_set_short_8',
        "command": 'set_short',
        "args": [0x7018, 0x0014],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_shadow_off_0',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_face_south_1',
                "command": 'face_south',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_floating_off_3',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_run_away_shift_6',
                "command": 'run_away_shift',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_set_solidity_bits_8',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._028_PIPE_ENTRANCE, 6]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_10',
                "command": 'set_sprite_sequence',
                "args": [30, inc_sprite=2, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_clear_solidity_bits_11',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_shift_z_down_steps_12',
                "command": 'shift_z_down_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_set_vram_priority_13',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_shift_south_pixels_14',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_set_solidity_bits_15',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS, _0x0AFlags.CANT_PASS_NPCS]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_9_SUBSCRIPT_visibility_off_16',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_pause_10',
        "command": 'pause',
        "args": [10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [45]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_face_southeast_8',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_face_southwest_10',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_12',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_jump_to_height_14',
                "command": 'jump_to_height',
                "args": [80]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_11_SUBSCRIPT_shift_northeast_steps_15',
                "command": 'shift_northeast_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_visibility_on_4',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_jump_to_height_5',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_shift_southwest_steps_8',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_shift_southwest_steps_10',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2288_action_queue_sync_12_SUBSCRIPT_visibility_off_11',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_visibility_on_1',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_jump_to_height_4',
                "command": 'jump_to_height',
                "args": [112]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_shift_southwest_steps_9',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_13_SUBSCRIPT_visibility_off_10',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_circle_mask_nonstatic_14',
        "command": 'circle_mask_nonstatic',
        "args": [AreaObjects.NPC_0, 30, 5],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_pause_15',
        "command": 'pause',
        "args": [90],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2288_action_queue_async_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_16_SUBSCRIPT_db_1',
                "command": 'db',
                "args": [0x20, 0x03]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_16_SUBSCRIPT_db_2',
                "command": 'db',
                "args": [0x24, 0x33, 0x01, 0xec, 0xfe]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_16_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [33]
            },
            {
                "identifier": 'EVENT_2288_action_queue_async_16_SUBSCRIPT_bpl_26_27_28_4',
                "command": 'bpl_26_27_28',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2288_display_intro_title_17',
        "command": 'display_intro_title',
        "args": [7, IntroTitles.MALLOW],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_pause_18',
        "command": 'pause',
        "args": [150],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_fade_out_to_black_async_duration_19',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_join_party_20',
        "command": 'join_party',
        "args": [AreaObjects.MALLOW],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_jmp_to_event_21',
        "command": 'jmp_to_event',
        "args": [135],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2288_ret_22',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
