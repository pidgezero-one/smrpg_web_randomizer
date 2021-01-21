from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_637_enable_controls_until_return_0',
        "command": 'enable_controls_until_return',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_637_start_loop_n_times_1',
        "command": 'start_loop_n_times',
        "args": [19]
    },
    {
        "identifier": 'EVENT_637_pause_2',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_637_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 3, 'EVENT_637_enable_controls_6']
    },
    {
        "identifier": 'EVENT_637_end_loop_4',
        "command": 'end_loop'
    },
    {
        "identifier": 'EVENT_637_jmp_to_event_5',
        "command": 'jmp_to_event',
        "args": [256]
    },
    {
        "identifier": 'EVENT_637_enable_controls_6',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_637_pause_action_script_7',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_637_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_sync_8_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_apply_solidity_mod_9',
        "command": 'apply_solidity_mod',
        "args": [Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL, 1, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_637_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_sync_10_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_sync_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_11_SUBSCRIPT_clear_solidity_bits_1',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_11_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_start_embedded_action_script_async_12',
        "command": 'start_embedded_action_script_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_637_start_embedded_action_script_async_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_637_start_embedded_action_script_async_12_SUBSCRIPT_shift_northeast_steps_1',
                "command": 'shift_northeast_steps',
                "args": [4]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_pause_13',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_637_play_sound_14',
        "command": 'play_sound',
        "args": [Sounds._151_CRASH_HIT, 6]
    },
    {
        "identifier": 'EVENT_637_apply_tile_mod_15',
        "command": 'apply_tile_mod',
        "args": [Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_637_pause_16',
        "command": 'pause',
        "args": [12]
    },
    {
        "identifier": 'EVENT_637_enter_area_17',
        "command": 'enter_area',
        "args": [Rooms._153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, RadialDirections.NORTHEAST, 18, 21, 0, []]
    },
    {
        "identifier": 'EVENT_637_remove_from_level_18',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL]
    },
    {
        "identifier": 'EVENT_637_remove_from_level_19',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL]
    },
    {
        "identifier": 'EVENT_637_remove_from_level_20',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_10, Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL]
    },
    {
        "identifier": 'EVENT_637_action_queue_async_21',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_async_21_SUBSCRIPT_set_priority_0',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_637_action_queue_async_21_SUBSCRIPT_set_vram_priority_1',
                "command": 'set_vram_priority',
                "args": [VramPriority.MARIO_OVERLAPS_ON_ALL_SIDES]
            },
            {
                "identifier": 'EVENT_637_action_queue_async_21_SUBSCRIPT_transfer_xyzf_pixels_2',
                "command": 'transfer_xyzf_pixels',
                "args": [0, 3, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_async_22_SUBSCRIPT_transfer_xyzf_pixels_0',
                "command": 'transfer_xyzf_pixels',
                "args": [8, 4, 0, RadialDirections.EAST]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_walk_1_step_northeast_1',
                "command": 'walk_1_step_northeast'
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_shift_northeast_pixels_2',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=6, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._018_SUDDEN_STOP, 4]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_reset_properties_12',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_23_SUBSCRIPT_set_animation_speed_13',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_637_action_queue_sync_24',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_sync_24_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_24_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_24_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_24_SUBSCRIPT_visibility_off_3',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_637_action_queue_sync_25',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_sync_25_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [12, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_25_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_25_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_25_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_637_action_queue_sync_25_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_637_fade_in_from_black_sync_26',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_637_pause_27',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_637_play_sound_28',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_637_apply_tile_mod_29',
        "command": 'apply_tile_mod',
        "args": [Rooms._153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, 0, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_637_remember_last_object_30',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_637_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY]
    },
    {
        "identifier": 'EVENT_637_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY]
    },
    {
        "identifier": 'EVENT_637_pause_33',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_637_play_sound_balance_34',
        "command": 'play_sound_balance',
        "args": [Sounds._021_RUMBLING, 192]
    },
    {
        "identifier": 'EVENT_637_set_action_script_async_35',
        "command": 'set_action_script_async',
        "args": [AreaObjects.SCREEN_FOCUS, 334]
    },
    {
        "identifier": 'EVENT_637_jmp_36',
        "command": 'jmp',
        "args": ['EVENT_637_play_sound_44']
    },
    {
        "identifier": 'EVENT_637_pause_37',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_637_run_dialog_38',
        "command": 'run_dialog',
        "args": [2070, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_637_pause_39',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_637_run_dialog_40',
        "command": 'run_dialog',
        "args": [2071, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_637_stop_sound_41',
        "command": 'stop_sound'
    },
    {
        "identifier": 'EVENT_637_pause_42',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_637_pause_43',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_637_play_sound_44',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6]
    },
    {
        "identifier": 'EVENT_637_apply_tile_mod_45',
        "command": 'apply_tile_mod',
        "args": [Rooms._153_MARRYMORE_CHAPEL_ENTRANCE_TO_SANCTUARY, 0, []]
    },
    {
        "identifier": 'EVENT_637_apply_solidity_mod_46',
        "command": 'apply_solidity_mod',
        "args": [Rooms._152_MARRYMORE_CHAPEL_MAIN_HALL, 0, [_0x6BFlags.PERMANENT]]
    },
    {
        "identifier": 'EVENT_637_enable_controls_47',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_637_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_637_action_queue_async_48_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_637_ret_49',
        "command": 'ret'
    }
]
