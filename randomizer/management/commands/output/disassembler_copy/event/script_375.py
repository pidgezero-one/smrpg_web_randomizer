
from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_375_play_music_default_volume_0',
        "command": 'play_music_default_volume',
        "args": [Music._02_MUSHROOM_KINGDOM]
    },
    {
        "identifier": 'EVENT_375_pause_action_script_1',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_13]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_walk_to_xy_coords_4',
                "command": 'walk_to_xy_coords',
                "args": [17, 20]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_face_southwest_5',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_2_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_jmp_if_bit_set_3',
        "command": 'jmp_if_bit_set',
        "args": [0x7061, 5, 'EVENT_375_action_queue_async_117']
    },
    {
        "identifier": 'EVENT_375_run_dialog_4',
        "command": 'run_dialog',
        "args": [630, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_jmp_if_mario_in_air_1',
                "command": 'jmp_if_mario_in_air',
                "args": ['EVENT_375_action_queue_sync_5_SUBSCRIPT_pause_0']
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_2',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_floating_off_3',
                "command": 'floating_off'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_bounce_to_xy_with_height_5',
                "command": 'bounce_to_xy_with_height',
                "args": [16, 30, 4]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_7',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_floating_on_8',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_5_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_floating_on_1',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_sequence_playback_on_2',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_shift_southwest_steps_5',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_shift_southwest_steps_7',
                "command": 'shift_southwest_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_6_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_7',
        "command": 'run_dialog',
        "args": [631, AreaObjects.NPC_13, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_script_resume_on_next_dialog_page_a_8',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_375_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_9_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_9_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_set_action_script_async_10',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_375_pause_11',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_12_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_12_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_12_SUBSCRIPT_shift_northeast_steps_2',
                "command": 'shift_northeast_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_12_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_12_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_13',
        "command": 'run_dialog',
        "args": [632, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_14',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_summon_to_current_level_15',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_375_summon_to_current_level_16',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_375_summon_to_current_level_17',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_375_run_dialog_18',
        "command": 'run_dialog',
        "args": [633, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_19_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_20_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [12, 35, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_face_northeast_6',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_7',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_21_SUBSCRIPT_floating_off_8',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [12, 35, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_shift_southeast_steps_6',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_22_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_23',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_23_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_23_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_24',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [12, 35, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_clear_solidity_bits_6',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_24_SUBSCRIPT_floating_off_7',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_25',
        "command": 'run_dialog',
        "args": [643, AreaObjects.NPC_10, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_26',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_375_jmp_if_bit_set_27',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_375_action_queue_async_30']
    },
    {
        "identifier": 'EVENT_375_action_queue_async_28',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_28_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_28_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_28_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_jmp_29',
        "command": 'jmp',
        "args": ['EVENT_375_pause_31']
    },
    {
        "identifier": 'EVENT_375_action_queue_async_30',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_30_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_30_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_30_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_pause_31',
        "command": 'pause',
        "args": [40]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_32',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_32_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_jmp_if_bit_clear_33',
        "command": 'jmp_if_bit_clear',
        "args": [0x7061, 5, 'EVENT_375_run_dialog_35']
    },
    {
        "identifier": 'EVENT_375_action_queue_async_34',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_34_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_35',
        "command": 'run_dialog',
        "args": [644, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_36',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [24, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_4',
                "command": 'set_sprite_sequence',
                "args": [23, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_set_sprite_sequence_6',
                "command": 'set_sprite_sequence',
                "args": [3, 2, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_36_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_fade_out_to_black_sync_duration_37',
        "command": 'fade_out_to_black_sync_duration',
        "args": [100]
    },
    {
        "identifier": 'EVENT_375_set_action_script_async_38',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_375_jmp_if_bit_clear_39',
        "command": 'jmp_if_bit_clear',
        "args": [0x7061, 5, 'EVENT_375_pause_script_until_effect_done_41']
    },
    {
        "identifier": 'EVENT_375_action_queue_async_40',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_40_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_40_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_pause_script_until_effect_done_41',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_375_enter_area_42',
        "command": 'enter_area',
        "args": [Rooms._018_MUSHROOM_KINGDOM_CASTLE_THRONE_ROOM, RadialDirections.NORTHEAST, 16, 30, 2, []]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_43_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_43_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_fade_in_from_black_sync_duration_44',
        "command": 'fade_in_from_black_sync_duration',
        "args": [200]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_45',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_walk_1_step_southeast_5',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_6',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_walk_1_step_northwest_8',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_9',
                "command": 'face_southwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_shift_southeast_pixels_11',
                "command": 'shift_southeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_45_SUBSCRIPT_face_southwest_12',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_pause_script_until_effect_done_46',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_375_run_dialog_47',
        "command": 'run_dialog',
        "args": [635, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_48',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_48_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, 3, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_48_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_49',
        "command": 'run_dialog',
        "args": [637, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_50',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_50_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_51',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_51_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [16, 30, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_51_SUBSCRIPT_shift_northwest_pixels_1',
                "command": 'shift_northwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_51_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_51_SUBSCRIPT_shift_northwest_pixels_3',
                "command": 'shift_northwest_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_51_SUBSCRIPT_face_southeast_4',
                "command": 'face_southeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_52',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_52_SUBSCRIPT_face_northwest_0',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_unsync_dialog_53',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_375_run_dialog_54',
        "command": 'run_dialog',
        "args": [638, AreaObjects.NPC_8, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_unsync_dialog_55',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_375_set_action_script_sync_56',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_8, 114]
    },
    {
        "identifier": 'EVENT_375_run_dialog_57',
        "command": 'run_dialog',
        "args": [639, AreaObjects.NPC_8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_58',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_59_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [7, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_59_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_59_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_60_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_60_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_61',
        "command": 'run_dialog',
        "args": [645, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_62',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_pause_action_script_63',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_8]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_64',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_64_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_64_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_64_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [15, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_64_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_64_SUBSCRIPT_reset_properties_4',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_65',
        "command": 'run_dialog',
        "args": [646, AreaObjects.NPC_8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_66',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_66_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_66_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_66_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_66_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_67',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_68',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_68_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_68_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_68_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_68_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_68_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_69',
        "command": 'run_dialog',
        "args": [647, AreaObjects.NPC_0, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_70',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_71',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_71_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_71_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_71_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_71_SUBSCRIPT_reset_properties_3',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_71_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_71_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_72',
        "command": 'run_dialog',
        "args": [648, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_73',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_action_queue_async_74',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_walk_1_step_southwest_1',
                "command": 'walk_1_step_southwest'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_add_z_coord_1_step_3',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_dec_z_coord_1_step_4',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_add_z_coord_1_step_5',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_74_SUBSCRIPT_dec_z_coord_1_step_6',
                "command": 'dec_z_coord_1_step'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_75',
        "command": 'run_dialog',
        "args": [636, AreaObjects.NPC_0, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_76',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_76_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_pause_77',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_78',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_face_southeast_0',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [10, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_shift_z_up_pixels_4',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_shift_z_up_pixels_6',
                "command": 'shift_z_up_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [11, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_dec_z_coord_1_step_9',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_78_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_79',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_79_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_79_SUBSCRIPT_face_northwest_1',
                "command": 'face_northwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_80',
        "command": 'run_dialog',
        "args": [642, AreaObjects.NPC_8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_81',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_82',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_82_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_pause_83',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_run_dialog_84',
        "command": 'run_dialog',
        "args": [877, AreaObjects.NPC_8, [_0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_85',
        "command": 'pause',
        "args": [10]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_86',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_86_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_86_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_86_SUBSCRIPT_set_sprite_sequence_2',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_87',
        "command": 'run_dialog',
        "args": [878, AreaObjects.NPC_8, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_88',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_89',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_sequence_playback_on_3',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_shift_southeast_pixels_5',
                "command": 'shift_southeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_89_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_pause_90',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_375_freeze_camera_91',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_92',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_92_SUBSCRIPT_face_south_0',
                "command": 'face_south'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_92_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_92_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_92_SUBSCRIPT_walk_1_step_north_3',
                "command": 'walk_1_step_north'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_set_bit_7_offset_93',
        "command": 'set_bit_7_offset',
        "args": [0x0158, []]
    },
    {
        "identifier": 'EVENT_375_set_bit_7_offset_94',
        "command": 'set_bit_7_offset',
        "args": [0x015a, []]
    },
    {
        "identifier": 'EVENT_375_db_95',
        "command": 'db',
        "args": [0xfd, 0x8e, 0x80, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_375_pause_script_until_effect_done_96',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_375_remember_last_object_97',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_run_dialog_98',
        "command": 'run_dialog',
        "args": [640, AreaObjects.BOWSER, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_375_pause_99',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_100',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_fixed_f_coord_off_0',
                "command": 'fixed_f_coord_off'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_sequence_playback_on_1',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_start_loop_n_times_2',
                "command": 'start_loop_n_times',
                "args": [6]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_turn_clockwise_45_degrees_n_times_3',
                "command": 'turn_clockwise_45_degrees_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_end_loop_5',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_set_sprite_sequence_7',
                "command": 'set_sprite_sequence',
                "args": [10, 2, [_0x08Flags.LOOPING_OFF, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_pause_8',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_play_sound_9',
                "command": 'play_sound',
                "args": [Sounds._013_COIN, 6]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_reset_properties_11',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_100_SUBSCRIPT_face_south_12',
                "command": 'face_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_set_bit_101',
        "command": 'set_bit',
        "args": [0x7082, 0]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_102',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_102_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [17, 27, 6, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_102_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_102_SUBSCRIPT_face_southwest_2',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_103',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_103_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_103_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_103_SUBSCRIPT_sequence_playback_off_2',
                "command": 'sequence_playback_off'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_103_SUBSCRIPT_walk_1_step_south_3',
                "command": 'walk_1_step_south'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_set_action_script_async_104',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 395]
    },
    {
        "identifier": 'EVENT_375_unfreeze_camera_105',
        "command": 'unfreeze_camera'
    },
    {
        "identifier": 'EVENT_375_pause_106',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_db_107',
        "command": 'db',
        "args": [0xfd, 0x8e, 0xb2, 0x07, 0x01]
    },
    {
        "identifier": 'EVENT_375_pause_script_until_effect_done_108',
        "command": 'pause_script_until_effect_done'
    },
    {
        "identifier": 'EVENT_375_clear_bit_7_offset_109',
        "command": 'clear_bit_7_offset',
        "args": [0x0158, []]
    },
    {
        "identifier": 'EVENT_375_clear_bit_7_offset_110',
        "command": 'clear_bit_7_offset',
        "args": [0x015a, []]
    },
    {
        "identifier": 'EVENT_375_set_bit_111',
        "command": 'set_bit',
        "args": [0x7065, 5]
    },
    {
        "identifier": 'EVENT_375_set_bit_112',
        "command": 'set_bit',
        "args": [0x7065, 6]
    },
    {
        "identifier": 'EVENT_375_set_bit_113',
        "command": 'set_bit',
        "args": [0x7065, 7]
    },
    {
        "identifier": 'EVENT_375_set_bit_114',
        "command": 'set_bit',
        "args": [0x706d, 5]
    },
    {
        "identifier": 'EVENT_375_set_bit_115',
        "command": 'set_bit',
        "args": [0x7042, 0]
    },
    {
        "identifier": 'EVENT_375_ret_116',
        "command": 'ret'
    },
    {
        "identifier": 'EVENT_375_action_queue_async_117',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_117_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_117_SUBSCRIPT_add_z_coord_1_step_1',
                "command": 'add_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_117_SUBSCRIPT_dec_z_coord_1_step_2',
                "command": 'dec_z_coord_1_step'
            },
            {
                "identifier": 'EVENT_375_action_queue_async_117_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_118',
        "command": 'run_dialog',
        "args": [641, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_unsync_dialog_119',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_375_close_dialog_120',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_121',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_121_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [16, 22]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_121_SUBSCRIPT_face_southeast_1',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_121_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [32]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_121_SUBSCRIPT_shift_southeast_steps_3',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_121_SUBSCRIPT_shift_south_steps_4',
                "command": 'shift_south_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_121_SUBSCRIPT_face_northeast_5',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_122',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_122_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_122_SUBSCRIPT_shift_southwest_steps_1',
                "command": 'shift_southwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_122_SUBSCRIPT_shift_southeast_steps_2',
                "command": 'shift_southeast_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_122_SUBSCRIPT_face_southwest_3',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_123',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_run_dialog_124',
        "command": 'run_dialog',
        "args": [631, AreaObjects.NPC_13, [_0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_pause_script_resume_on_next_dialog_page_a_125',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_375_action_queue_async_126',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_126_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_126_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_async_126_SUBSCRIPT_reset_properties_2',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_set_action_script_async_127',
        "command": 'set_action_script_async',
        "args": [AreaObjects.MARIO, 670]
    },
    {
        "identifier": 'EVENT_375_pause_128',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_129',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_129_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_129_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [6, 0, [_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_375_run_dialog_130',
        "command": 'run_dialog',
        "args": [632, AreaObjects.NPC_13, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_131',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_summon_to_current_level_132',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_375_summon_to_current_level_133',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_11]
    },
    {
        "identifier": 'EVENT_375_summon_to_current_level_134',
        "command": 'summon_to_current_level',
        "args": [AreaObjects.NPC_12]
    },
    {
        "identifier": 'EVENT_375_run_dialog_135',
        "command": 'run_dialog',
        "args": [633, AreaObjects.NPC_10, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE, _0x60Flags.USE_BACKGROUND]]
    },
    {
        "identifier": 'EVENT_375_action_queue_async_136',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_13],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_async_136_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_137',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_137_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [8]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_137_SUBSCRIPT_face_southwest_1',
                "command": 'face_southwest'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_138',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_10],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [13, 34, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_set_solidity_bits_1',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_floating_on_2',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [9]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_shift_northeast_pixels_5',
                "command": 'shift_northeast_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_walk_1_step_southeast_6',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_face_northeast_7',
                "command": 'face_northeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_138_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_139',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_11],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 34, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_139_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_140',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_12],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [40]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_transfer_to_xyzf_1',
                "command": 'transfer_to_xyzf',
                "args": [13, 34, 4, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_set_solidity_bits_2',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_floating_on_3',
                "command": 'floating_on'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_shift_northeast_steps_5',
                "command": 'shift_northeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_shift_northwest_steps_6',
                "command": 'shift_northwest_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_face_southeast_7',
                "command": 'face_southeast'
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_clear_solidity_bits_8',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_140_SUBSCRIPT_floating_off_9',
                "command": 'floating_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_action_queue_sync_141',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_375_action_queue_sync_141_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [20]
            },
            {
                "identifier": 'EVENT_375_action_queue_sync_141_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast'
            }
        ]
    },
    {
        "identifier": 'EVENT_375_remember_last_object_142',
        "command": 'remember_last_object'
    },
    {
        "identifier": 'EVENT_375_close_dialog_143',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_375_jmp_144',
        "command": 'jmp',
        "args": ['EVENT_375_run_dialog_25']
    }
]
