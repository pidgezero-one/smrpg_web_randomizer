from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2596_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708f, 7, 'EVENT_2596_ret_42'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_jmp_1',
        "command": 'jmp',
        "args": ['EVENT_2596_start_battle_33'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_2',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_2_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_3_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_4_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._029_ALARM_CLOCK, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_pause_5',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_async_6_SUBSCRIPT_start_loop_n_times_0',
                "command": 'start_loop_n_times',
                "args": [1]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_6_SUBSCRIPT_pause_2',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_6_SUBSCRIPT_set_sprite_sequence_3',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=3, flags=[_0x08Flags.READ_AS_SEQUENCE, _0x08Flags.MIRROR_SPRITE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_6_SUBSCRIPT_pause_4',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_6_SUBSCRIPT_end_loop_5',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_8',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_8_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_9_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_async_10_SUBSCRIPT_reset_properties_0',
                "command": 'reset_properties',
                "args": []
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_10_SUBSCRIPT_face_northeast_1',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_async_11_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [4, 69]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_pause_12',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_13_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._029_ALARM_CLOCK, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_run_dialog_14',
        "command": 'run_dialog',
        "args": [3150, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_async_15_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 4]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_15_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_pause_16',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_17',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_17_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_17_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_17_SUBSCRIPT_play_sound_2',
                "command": 'play_sound',
                "args": [Sounds._029_ALARM_CLOCK, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_run_dialog_18',
        "command": 'run_dialog',
        "args": [3150, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_async_19_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._000_SILENCE, 4]
            },
            {
                "identifier": 'EVENT_2596_action_queue_async_19_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_pause_20',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_21_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_21_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_22',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_22_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_22_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_play_sound_23',
        "command": 'play_sound',
        "args": [Sounds._029_ALARM_CLOCK, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_run_dialog_24',
        "command": 'run_dialog',
        "args": [3160, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_pause_26',
        "command": 'pause',
        "args": [16],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_27',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_1],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_27_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_27_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_28',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_2],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_28_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2596_action_queue_sync_28_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [2, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_action_queue_sync_29',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_0],
        "subscript": [
            {
                "identifier": 'EVENT_2596_action_queue_sync_29_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._029_ALARM_CLOCK, 4]
            }
        ]
    },
    {
        "identifier": 'EVENT_2596_set_action_script_sync_30',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 861],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_set_action_script_sync_31',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 862],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_run_dialog_32',
        "command": 'run_dialog',
        "args": [3151, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_start_battle_33',
        "command": 'start_battle',
        "args": [0x00ae, 18],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_set_action_script_sync_34',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_set_action_script_sync_35',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 15],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_jmp_if_bit_clear_36',
        "command": 'jmp_if_bit_clear',
        "args": [0x7040, 0, 'EVENT_2596_restore_all_hp_38'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_reset_and_choose_game_37',
        "command": 'reset_and_choose_game',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_restore_all_hp_38',
        "command": 'restore_all_hp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_restore_all_fp_39',
        "command": 'restore_all_fp',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_set_bit_40',
        "command": 'set_bit',
        "args": [0x708f, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_enter_area_41',
        "command": 'enter_area',
        "args": [Rooms._433_SMITHY_FACTORY_AREA_01_____DUMMY, RadialDirections.NORTHEAST, 7, 106, 10, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2596_ret_42',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
