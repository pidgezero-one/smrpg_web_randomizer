from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_1390_apply_tile_mod_0',
        "command": 'apply_tile_mod',
        "args": [Rooms._439_BOWSERS_KEEP_OUTSIDE_TALK_TO_EXOR, 32, [_0x6AFlags.USE_ALTERNATE]]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_1',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_1_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_1_SUBSCRIPT_shift_south_steps_1',
                "command": 'shift_south_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_1_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_1_SUBSCRIPT_shift_east_pixels_3',
                "command": 'shift_east_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_1_SUBSCRIPT_shift_southeast_pixels_4',
                "command": 'shift_southeast_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_1_SUBSCRIPT_set_sprite_sequence_5',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_2_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_2_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_3_SUBSCRIPT_shift_south_pixels_0',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_3_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_3_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_4_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [18]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_4_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_4_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_4_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_5',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_5_SUBSCRIPT_shift_northeast_pixels_0',
                "command": 'shift_northeast_pixels',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_5_SUBSCRIPT_shift_east_pixels_1',
                "command": 'shift_east_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_5_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_5_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_async_6_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [1, 46, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_6_SUBSCRIPT_shift_southwest_pixels_1',
                "command": 'shift_southwest_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_6_SUBSCRIPT_shift_northwest_pixels_2',
                "command": 'shift_northwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_6_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_remove_from_current_level_7',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_1390_fade_in_from_black_sync_8',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_1390_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_vram_priority_0',
                "command": 'set_vram_priority',
                "args": [VramPriority.PRIORITY_3]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_sequence_looping_on_3',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_6',
                "command": 'shift_northeast_pixels',
                "args": [83]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_animation_speed_7',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_8',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_10',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_11',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_12',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_13',
                "command": 'pause',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_14',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_15',
                "command": 'pause',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_17',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_18',
                "command": 'pause',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_19',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_20',
                "command": 'pause',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_shift_northeast_pixels_21',
                "command": 'shift_northeast_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_22',
                "command": 'set_sprite_sequence',
                "args": [5, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_23',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_sequence_looping_on_24',
                "command": 'sequence_looping_on'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_sequence_playback_on_25',
                "command": 'sequence_playback_on'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_animation_speed_26',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_set_sprite_sequence_27',
                "command": 'set_sprite_sequence',
                "args": [1, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_9_SUBSCRIPT_pause_28',
                "command": 'pause',
                "args": [55]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_1',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_5',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_set_animation_speed_8',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_steps_9',
                "command": 'shift_north_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_pause_10',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_south_pixels_12',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_13',
                "command": 'shift_north_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_south_pixels_14',
                "command": 'shift_south_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_15',
                "command": 'shift_north_pixels',
                "args": [10]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_south_pixels_16',
                "command": 'shift_south_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_17',
                "command": 'shift_north_pixels',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_south_pixels_18',
                "command": 'shift_south_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_10_SUBSCRIPT_shift_north_pixels_19',
                "command": 'shift_north_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_pause_11',
        "command": 'pause',
        "args": [90]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 581]
    },
    {
        "identifier": 'EVENT_1390_run_dialog_13',
        "command": 'run_dialog',
        "args": [2570, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_1390_pause_script_resume_on_next_dialog_page_a_14',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_15',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_16',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_17',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_18',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 581]
    },
    {
        "identifier": 'EVENT_1390_pause_script_resume_on_next_dialog_page_a_19',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_20',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_21',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_22',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_23',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 582]
    },
    {
        "identifier": 'EVENT_1390_pause_script_resume_on_next_dialog_page_a_24',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_25',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_26',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_27',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 582]
    },
    {
        "identifier": 'EVENT_1390_pause_script_resume_on_next_dialog_page_a_29',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_30',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_31',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_32',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_33',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 582]
    },
    {
        "identifier": 'EVENT_1390_pause_script_resume_on_next_dialog_page_a_34',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_35',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_36',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_37',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_38',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 582]
    },
    {
        "identifier": 'EVENT_1390_pause_script_resume_on_next_dialog_page_a_39',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_40',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_41',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_42',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_action_queue_async_43',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_async_43_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_43_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [35]
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_44',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 581]
    },
    {
        "identifier": 'EVENT_1390_unsync_dialog_45',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_1390_close_dialog_46',
        "command": 'close_dialog'
    },
    {
        "identifier": 'EVENT_1390_pause_action_script_47',
        "command": 'pause_action_script',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_48',
        "command": 'pause',
        "args": [1]
    },
    {
        "identifier": 'EVENT_1390_reset_coords_49',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_0]
    },
    {
        "identifier": 'EVENT_1390_pause_50',
        "command": 'pause',
        "args": [30]
    },
    {
        "identifier": 'EVENT_1390_set_action_script_sync_51',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_0, 583]
    },
    {
        "identifier": 'EVENT_1390_pause_52',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1390_fade_out_sound_to_volume_53',
        "command": 'fade_out_sound_to_volume',
        "args": [0, 0]
    },
    {
        "identifier": 'EVENT_1390_play_sound_54',
        "command": 'play_sound',
        "args": [Sounds._091_TUMBLING_BOULDERS, 6]
    },
    {
        "identifier": 'EVENT_1390_fade_out_sound_to_volume_55',
        "command": 'fade_out_sound_to_volume',
        "args": [7, 100]
    },
    {
        "identifier": 'EVENT_1390_action_queue_async_56',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [34]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_north_pixels_3',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_end_loop_4',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_start_loop_n_times_5',
                "command": 'start_loop_n_times',
                "args": [14]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_north_pixels_7',
                "command": 'shift_north_pixels',
                "args": [2]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_end_loop_8',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_start_loop_n_times_9',
                "command": 'start_loop_n_times',
                "args": [9]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_pixels_10',
                "command": 'shift_south_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_north_pixels_11',
                "command": 'shift_north_pixels',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_end_loop_12',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_start_loop_n_times_13',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_pixels_14',
                "command": 'shift_south_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_north_pixels_15',
                "command": 'shift_north_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_end_loop_16',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_set_animation_speed_17',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_steps_18',
                "command": 'shift_south_steps',
                "args": [11]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_set_animation_speed_19',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_start_loop_n_times_20',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_pixels_21',
                "command": 'shift_south_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_north_pixels_22',
                "command": 'shift_north_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_end_loop_23',
                "command": 'end_loop'
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_start_loop_n_times_24',
                "command": 'start_loop_n_times',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_south_pixels_25',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_shift_north_pixels_26',
                "command": 'shift_north_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_async_56_SUBSCRIPT_end_loop_27',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_57',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_57_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [89]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_57_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_57_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [7]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_57_SUBSCRIPT_end_loop_3',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_58',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_shift_south_pixels_1',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_shift_south_pixels_3',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_shift_south_pixels_5',
                "command": 'shift_south_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_58_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_59',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_5],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_59_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_60',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_4],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [12]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_shift_south_pixels_6',
                "command": 'shift_south_pixels',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_60_SUBSCRIPT_visibility_off_7',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_action_queue_sync_61',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [7, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_shadow_off_2',
                "command": 'shadow_off'
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_jump_to_height_silent_4',
                "command": 'jump_to_height_silent',
                "args": [80]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTER, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_shift_southwest_steps_6',
                "command": 'shift_southwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_db_8',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0xec]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_jump_to_height_silent_9',
                "command": 'jump_to_height_silent',
                "args": [48]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_set_animation_speed_10',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_shift_southeast_steps_11',
                "command": 'shift_southeast_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_pause_12',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_db_13',
                "command": 'db',
                "args": [0xfd, 0x3d, 0x14, 0xfa]
            },
            {
                "identifier": 'EVENT_1390_action_queue_sync_61_SUBSCRIPT_end_loop_14',
                "command": 'end_loop'
            }
        ]
    },
    {
        "identifier": 'EVENT_1390_fade_out_to_black_async_duration_62',
        "command": 'fade_out_to_black_async_duration',
        "args": [200]
    },
    {
        "identifier": 'EVENT_1390_fade_out_sound_to_volume_63',
        "command": 'fade_out_sound_to_volume',
        "args": [5, 0]
    },
    {
        "identifier": 'EVENT_1390_pause_64',
        "command": 'pause',
        "args": [60]
    },
    {
        "identifier": 'EVENT_1390_clear_bit_65',
        "command": 'clear_bit',
        "args": [0x7065, 0]
    },
    {
        "identifier": 'EVENT_1390_set_bit_66',
        "command": 'set_bit',
        "args": [0x7068, 3]
    },
    {
        "identifier": 'EVENT_1390_set_bit_67',
        "command": 'set_bit',
        "args": [0x7070, 3]
    },
    {
        "identifier": 'EVENT_1390_set_bit_68',
        "command": 'set_bit',
        "args": [0x7053, 1]
    },
    {
        "identifier": 'EVENT_1390_enter_area_69',
        "command": 'enter_area',
        "args": [Rooms._015_VISTA_HILL, RadialDirections.NORTHWEST, 4, 16, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_1390_ret_70',
        "command": 'ret'
    }
]
