from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2407_jmp_0',
        "command": 'jmp',
        "args": ['EVENT_2407_jmp_if_var_equals_byte_27'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_stop_sound_1',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_byte_2',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 6, 'EVENT_2407_set_7000_to_object_coord_4'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_ret_3',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_7000_to_object_coord_4',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_short_5',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 7, 'EVENT_2407_freeze_camera_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_short_6',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 0, 'EVENT_2407_freeze_camera_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_short_7',
        "command": 'jmp_if_var_equals_short',
        "args": [0x7000, 6, 'EVENT_2407_freeze_camera_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_freeze_camera_9',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_enable_controls_10',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_pause_11',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_jmp_if_mario_in_air_12',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2407_pause_11'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_summon_to_current_level_at_marios_coords_13',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_sync_14_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_14_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_14_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_14_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [26, 110]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_14_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off',
                "args": []
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_15_SUBSCRIPT_set_vram_priority_7',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_sync_16_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_run_dialog_17',
        "command": 'run_dialog',
        "args": [3104, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_7000_to_object_coord_18',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_short_mem_19',
        "command": 'set_short_mem',
        "args": [0x7016, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_7000_to_object_coord_20',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_short_mem_21',
        "command": 'set_short_mem',
        "args": [0x7018, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_async_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_22_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_22_SUBSCRIPT_run_away_shift_3',
                "command": 'run_away_shift',
                "args": []
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_22_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_set_action_script_async_23',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_unfreeze_camera_24',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_enable_controls_25',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_ret_26',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_byte_27',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 6, 'EVENT_2407_freeze_camera_29'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_ret_28',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_freeze_camera_29',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_async_30_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_30_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_pause_31',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_db_32',
        "command": 'db',
        "args": [0xfd, 0x8d],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_apply_tile_mod_33',
        "command": 'apply_tile_mod',
        "args": [Rooms._159_STAR_HILL_AREA_04, 13, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_play_sound_34',
        "command": 'play_sound',
        "args": [Sounds._126_EMERGE_DEEP_WATER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_unfreeze_camera_35',
        "command": 'unfreeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_pause_36',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_fade_out_to_black_async_duration_37',
        "command": 'fade_out_to_black_async_duration',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_play_sound_38',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_bit_39',
        "command": 'set_bit',
        "args": [0x706f, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_set_bit_40',
        "command": 'set_bit',
        "args": [0x7067, 3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2407_open_location_41',
        "command": 'open_location',
        "args": [Locations._031_STAR_HILL, [6, 7]],
        "subscript": []
    }
]
