from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2066_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 5, 'EVENT_2066_run_dialog_37']
    },
    {
        "identifier": 'EVENT_2066_jmp_if_bit_set_1',
        "command": 'jmp_if_bit_set',
        "args": [0x708a, 2, 'EVENT_2066_run_dialog_35']
    },
    {
        "identifier": 'EVENT_2066_jmp_2',
        "command": 'jmp',
        "args": ['EVENT_2066_action_queue_async_7']
    },
    {
        "identifier": 'EVENT_2066_run_dialog_3',
        "command": 'run_dialog',
        "args": [3033, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_run_dialog_4',
        "command": 'run_dialog',
        "args": [3035, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_pause_5',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2066_freeze_camera_6',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_2066_action_queue_async_7',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_async_7_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_7_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_7_SUBSCRIPT_walk_to_xy_coords_2',
                "command": 'walk_to_xy_coords',
                "args": [5, 16]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_7_SUBSCRIPT_face_northeast_3',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_sync_8_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_8_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [53]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_shift_northeast_steps_3',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._101_TERRAPIN_ATTACK, 6]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [4, 0, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_9_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_fixed_f_coord_on_0',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_jump_to_height_silent_2',
                "command": 'jump_to_height_silent',
                "args": [53]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_shift_southwest_steps_3',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [2, 4, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_10_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [45]
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_start_battle_11',
        "command": 'start_battle',
        "args": [0x00bd, 46]
    },
    {
        "identifier": 'EVENT_2066_restore_all_hp_12',
        "command": 'restore_all_hp'
    },
    {
        "identifier": 'EVENT_2066_restore_all_fp_13',
        "command": 'restore_all_fp'
    },
    {
        "identifier": 'EVENT_2066_jmp_if_bit_set_14',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 0, 'EVENT_2066_fade_in_from_black_async_17']
    },
    {
        "identifier": 'EVENT_2066_jmp_if_bit_set_15',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_2066_fade_in_from_black_async_17']
    },
    {
        "identifier": 'EVENT_2066_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_async_16_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [6, 8, 3, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_16_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_16_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_fade_in_from_black_async_17',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_2066_action_queue_sync_18',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_sync_18_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [1]
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [70]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_face_northeast_2',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_fixed_f_coord_off_3',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_2066_action_queue_async_19_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2066_unfreeze_camera_20',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_2066_pause_21',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_2066_jmp_if_bit_set_22',
        "command": 'jmp_if_bit_set',
        "args": [0x7040, 1, 'EVENT_2066_run_dialog_31']
    },
    {
        "identifier": 'EVENT_2066_jmp_if_bit_clear_23',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2066_jmp_30']
    },
    {
        "identifier": 'EVENT_2066_stop_music_FDA2_24',
        "command": 'stop_music_FDA2'
    },
    {
        "identifier": 'EVENT_2066_fade_out_music_to_volume_25',
        "command": 'fade_out_music_to_volume',
        "args": [0, 100]
    },
    {
        "identifier": 'EVENT_2066_play_music_default_volume_26',
        "command": 'play_music_default_volume',
        "args": [Music._51_MONSTRO_TOWN]
    },
    {
        "identifier": 'EVENT_2066_run_dialog_27',
        "command": 'run_dialog',
        "args": [3036, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_ret_28',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2066_run_dialog_29',
        "command": 'run_dialog',
        "args": [3037, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2066_jmp_30',
        "command": 'jmp',
        "args": ['EVENT_2067_action_queue_async_0']
    },
    {
        "identifier": 'EVENT_2066_run_dialog_31',
        "command": 'run_dialog',
        "args": [2592, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_ret_32',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2066_run_dialog_33',
        "command": 'run_dialog',
        "args": [3034, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_ret_34',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2066_run_dialog_35',
        "command": 'run_dialog',
        "args": [3044, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_ret_36',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_2066_run_dialog_37',
        "command": 'run_dialog',
        "args": [3352, AreaObjects.MEM_70A8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_2066_ret_38',
        "command": 'ret'
    }
]
