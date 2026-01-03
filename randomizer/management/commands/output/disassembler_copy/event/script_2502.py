
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2502_fade_out_music_to_volume_0',
        "command": 'fade_out_music_to_volume',
        "args": [5, 0]
    },
    {
        "identifier": 'EVENT_2502_pause_1',
        "command": 'pause',
        "args": [80]
    },
    {
        "identifier": 'EVENT_2502_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [8, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [48]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [0, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_start_loop_n_times_8',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [27, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [27, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_end_loop_13',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_14',
                "command": 'set_sprite_sequence',
                "args": [12, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_16',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_17',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_18',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_19',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_20',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_pause_21',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_2_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [0, 3, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_play_music_default_volume_3',
        "command": 'play_music_default_volume',
        "args": [Music._12_FIGHT_AGAINST_BOWSER]
    },
    {
        "identifier": 'EVENT_2502_action_queue_async_4',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_async_4_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_freeze_camera_5',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2502_action_queue_sync_6',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_sync_6_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 3, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_6_SUBSCRIPT_sequence_playback_off_1',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_6_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_6_SUBSCRIPT_jump_to_height_3',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_6_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [31]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_6_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_pause_7',
        "command": 'pause',
        "args": [128]
    },
    {
        "identifier": 'EVENT_2502_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_8_SUBSCRIPT_shift_north_steps_1',
                "command": 'shift_north_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_async_9_SUBSCRIPT_shift_north_steps_0',
                "command": 'shift_north_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_9_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._026_LAUGHING_BOWSER, 6]
    },
    {
        "identifier": 'EVENT_2502_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [2, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_11_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [144]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [0, 2, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_pause_12',
        "command": 'pause',
        "args": [64]
    },
    {
        "identifier": 'EVENT_2502_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._004_JUMP, 6]
    },
    {
        "identifier": 'EVENT_2502_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 46, 2, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [4, 1, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_priority_2',
                "command": 'set_priority',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_overwrite_solidity_3',
                "command": 'overwrite_solidity',
                "args": [[]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x20, 0x07]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_db_5',
                "command": 'db',
                "args": [0x24, 0xe0, 0xfd, 0x00, 0xff]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_db_6',
                "command": 'db',
                "args": [0x25, 0x00, 0x0d, 0x80, 0xff]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [44]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_9',
                "command": 'set_sprite_sequence',
                "args": [16, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [9]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_11',
                "command": 'set_sprite_sequence',
                "args": [23, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_13',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_pause_14',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_15',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_pause_16',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_set_sprite_sequence_17',
                "command": 'set_sprite_sequence',
                "args": [3, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_async_14_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [48]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_action_queue_sync_16',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, 4, [_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_play_sound_3',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_play_sound_5',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_pause_6',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_play_sound_7',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2502_action_queue_sync_16_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._096_SWINGING_FIST, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2502_pause_17',
        "command": 'pause',
        "args": [72]
    },
    {
        "identifier": 'EVENT_2502_restore_all_hp_18',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2502_restore_all_fp_19',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2502_start_battle_20',
        "command": 'start_battle',
        "args": [0x00a0, 29]
    },
    {
        "identifier": 'EVENT_2502_jmp_if_bit_clear_21',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2502_enable_controls_23']
    },
    {
        "identifier": 'EVENT_2502_reset_game_22',
        "command": 'reset_game'
    },
    {
        "identifier": 'EVENT_2502_enable_controls_23',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2502_put_inventory_24',
        "command": 'put_inventory',
        "args": [0xa0]
    },
    {
        "identifier": 'EVENT_2502_restore_all_hp_25',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2502_restore_all_fp_26',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2502_clear_bit_27',
        "command": 'clear_bit',
        "args": [0x7064, 0]
    },
    {
        "identifier": 'EVENT_2502_clear_bit_28',
        "command": 'clear_bit',
        "args": [0x7064, 1]
    },
    {
        "identifier": 'EVENT_2502_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7064, 2]
    },
    {
        "identifier": 'EVENT_2502_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7064, 3]
    },
    {
        "identifier": 'EVENT_2502_set_31',
        "command": 'set',
        "args": [0x70da, 0]
    },
    {
        "identifier": 'EVENT_2502_set_32',
        "command": 'set',
        "args": [0x70db, 0]
    },
    {
        "identifier": 'EVENT_2502_set_33',
        "command": 'set',
        "args": [0x70dc, 0]
    },
    {
        "identifier": 'EVENT_2502_set_34',
        "command": 'set',
        "args": [0x70dd, 0]
    },
    {
        "identifier": 'EVENT_2502_stop_music_FDA2_35',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_2502_exor_crashes_into_keep_36',
        "command": 'exor_crashes_into_keep'
    },
    {
        "identifier": 'EVENT_2502_run_event_sequence_37',
        "command": 'run_event_sequence',
        "args": [EventSequences._16_RUN_WORLD_MAP_EVENT_SEQUENCE, OverworldSequences._00_MARIO_FALLS_TO_PIPEHOUSE]
    },
    {
        "identifier": 'EVENT_2502_stop_music_FDA2_38',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_2502_jmp_to_event_39',
        "command": 'jmp_to_event',
        "args": [1393]
    },
    {
        "identifier": 'EVENT_2502_ret_40',
        "command": 'ret'
    }
]
