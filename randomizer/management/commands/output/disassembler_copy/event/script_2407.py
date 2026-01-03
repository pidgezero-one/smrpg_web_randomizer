
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2407_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 5, 'EVENT_2407_jmp_if_var_equals_byte_26']
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_byte_1',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 6, 'EVENT_2407_set_7000_to_object_coord_3']
    },
    {
        "identifier": 'EVENT_2407_ret_2',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2407_set_7000_to_object_coord_3',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F, []]
    },
    {
        "identifier": 'EVENT_2407_jmp_if_7000_equals_short_4',
        "command": 'jmp_if_7000_equals_short',
        "args": [7, 'EVENT_2407_freeze_camera_8']
    },
    {
        "identifier": 'EVENT_2407_jmp_if_7000_equals_short_5',
        "command": 'jmp_if_7000_equals_short',
        "args": [0, 'EVENT_2407_freeze_camera_8']
    },
    {
        "identifier": 'EVENT_2407_jmp_if_7000_equals_short_6',
        "command": 'jmp_if_7000_equals_short',
        "args": [6, 'EVENT_2407_freeze_camera_8']
    },
    {
        "identifier": 'EVENT_2407_ret_7',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2407_freeze_camera_8',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2407_enable_controls_9',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2407_pause_10',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_2407_jmp_if_mario_in_air_11',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_2407_pause_10']
    },
    {
        "identifier": 'EVENT_2407_summon_to_current_level_at_marios_coords_12',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_7]
    },
    {
        "identifier": 'EVENT_2407_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_sync_13_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_13_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_13_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_13_SUBSCRIPT_walk_to_xy_coords_3',
                "command": 'walk_to_xy_coords',
                "args": [26, 110]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_13_SUBSCRIPT_face_southwest_4',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_overwrite_solidity_0',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_floating_off_1',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_shadow_on_2',
                "command": 'shadow_on'
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_shift_southwest_steps_4',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_14_SUBSCRIPT_set_vram_priority_7',
                "command": 'set_vram_priority',
                "args": [VramPriority.OBJECT_OVERLAPS_MARIO_ON_ALL_SIDES]
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_sync_15_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_run_dialog_16',
        "command": 'run_dialog',
        "args": [3104, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2407_set_7000_to_object_coord_17',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.X, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2407_set_7000_short_mem_to_7000_18',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7016]
    },
    {
        "identifier": 'EVENT_2407_set_7000_to_object_coord_19',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, [7], CoordUnits.PIXEL]
    },
    {
        "identifier": 'EVENT_2407_set_7000_short_mem_to_7000_20',
        "command": 'set_7000_short_mem_to_7000',
        "args": [0x7018]
    },
    {
        "identifier": 'EVENT_2407_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_async_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_21_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_21_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_21_SUBSCRIPT_run_away_shift_3',
                "command": 'run_away_shift'
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_21_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_set_action_script_async_22',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_2407_unfreeze_camera_23',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2407_enable_controls_24',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2407_ret_25',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2407_jmp_if_var_equals_byte_26',
        "command": 'jmp_if_var_equals_byte',
        "args": [0x70ae, 6, 'EVENT_2407_freeze_camera_28']
    },
    {
        "identifier": 'EVENT_2407_ret_27',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2407_freeze_camera_28',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2407_action_queue_async_29',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2407_action_queue_async_29_SUBSCRIPT_walk_1_step_northeast_0',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_2407_action_queue_async_29_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2407_pause_30',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2407_db_31',
        "command": 'db',
        "args": [0xfd, 0x8d]
    },
    {
        "identifier": 'EVENT_2407_apply_tile_mod_32',
        "command": 'apply_tile_mod',
        "args": [Rooms._159_STAR_HILL_AREA_04, 13, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_2407_play_sound_33',
        "command": 'play_sound',
        "args": [Sounds._126_EMERGE_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2407_unfreeze_camera_34',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2407_pause_35',
        "command": 'pause',
        "args": [32]
    },
    {
        "identifier": 'EVENT_2407_fade_out_to_black_async_duration_36',
        "command": 'fade_out_to_black_async_duration',
        "args": [16]
    },
    {
        "identifier": 'EVENT_2407_play_sound_37',
        "command": 'play_sound',
        "args": [Sounds._125_ENTER_DEEP_WATER, 6]
    },
    {
        "identifier": 'EVENT_2407_set_bit_38',
        "command": 'set_bit',
        "args": [0x706f, 2]
    },
    {
        "identifier": 'EVENT_2407_set_bit_39',
        "command": 'set_bit',
        "args": [0x7067, 3]
    },
    {
        "identifier": 'EVENT_2407_open_location_40',
        "command": 'open_location',
        "args": [Locations._031_STAR_HILL, [6, 7]]
    }
]
