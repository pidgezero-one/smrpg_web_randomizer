from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2531_play_sound_0',
        "command": 'play_sound',
        "args": [Sounds._110_ABSTRACT_MUSIC, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x705f, 4, 'EVENT_2531_run_dialog_5'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_run_dialog_2',
        "command": 'run_dialog',
        "args": [3327, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_play_sound_3',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_ret_4',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_run_dialog_5',
        "command": 'run_dialog',
        "args": [3116, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_play_sound_6',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_jmp_if_bit_set_7',
        "command": 'jmp_if_bit_set',
        "args": [0x708c, 0, 'EVENT_2531_ret_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_set_bit_8',
        "command": 'set_bit',
        "args": [0x708c, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_fade_out_music_9',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_summon_to_current_level_at_marios_coords_10',
        "command": 'summon_to_current_level_at_marios_coords',
        "args": [AreaObjects.NPC_21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=2, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_11_SUBSCRIPT_jump_to_height_1',
                "command": 'jump_to_height',
                "args": [108]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_11_SUBSCRIPT_walk_1_step_northeast_2',
                "command": 'walk_1_step_northeast',
                "args": []
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_11_SUBSCRIPT_shift_northeast_pixels_3',
                "command": 'shift_northeast_pixels',
                "args": [8]
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_run_dialog_12',
        "command": 'run_dialog',
        "args": [3123, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_pause_script_resume_on_next_dialog_page_a_13',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_14_SUBSCRIPT_face_northeast_0',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_pause_script_resume_on_next_dialog_page_a_15',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_play_music_default_volume_16',
        "command": 'play_music_default_volume',
        "args": [Music._21_SAD_SONG],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_17_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_unsync_dialog_18',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_pause_19',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_20',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_pause_21',
        "command": 'pause',
        "args": [48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_run_dialog_22',
        "command": 'run_dialog',
        "args": [3126, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_23',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_shift_north_pixels_2',
                "command": 'shift_north_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_shift_south_pixels_4',
                "command": 'shift_south_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_23_SUBSCRIPT_end_loop_6',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_unsync_dialog_24',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_pause_25',
        "command": 'pause',
        "args": [96],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_26',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_26_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_run_dialog_27',
        "command": 'run_dialog',
        "args": [3124, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_pause_28',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_set_action_script_sync_29',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_pause_30',
        "command": 'pause',
        "args": [32],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_31',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_31_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [9, inc_sprite=1, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_run_dialog_32',
        "command": 'run_dialog',
        "args": [3125, AreaObjects.NPC_12, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_action_queue_async_33',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_21],
        "subscript": [
            {
                "identifier": 'EVENT_2531_action_queue_async_33_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_33_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_33_SUBSCRIPT_walk_1_step_southwest_2',
                "command": 'walk_1_step_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_33_SUBSCRIPT_shift_southwest_pixels_3',
                "command": 'shift_southwest_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_2531_action_queue_async_33_SUBSCRIPT_visibility_off_4',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2531_remove_from_current_level_34',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_21],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_fade_out_music_35',
        "command": 'fade_out_music',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_pause_36',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_play_music_default_volume_37',
        "command": 'play_music_default_volume',
        "args": [Music._34_STAR_HILL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2531_ret_38',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
