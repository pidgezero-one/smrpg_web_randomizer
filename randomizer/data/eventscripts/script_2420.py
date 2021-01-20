from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_2420_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 2, 'EVENT_2420_enter_area_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 1, 'EVENT_2420_enter_area_35'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_set_bit_2',
        "command": 'set_bit',
        "args": [0x708b, 2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_enable_controls_3',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_current_level_5',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_pause_6',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_stop_all_background_events_7',
        "command": 'stop_all_background_events',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_run_background_event_8',
        "command": 'run_background_event',
        "args": [2419, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_action_queue_async_9',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_async_9_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [10, 59]
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_run_dialog_10',
        "command": 'run_dialog',
        "args": [3083, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_action_queue_sync_11',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_sync_11_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_pause_script_resume_on_next_dialog_page_a_12',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_action_queue_sync_13',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_sync_13_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_pause_script_resume_on_next_dialog_page_a_14',
        "command": 'pause_script_resume_on_next_dialog_page_a',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_action_queue_sync_15',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_sync_15_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_unsync_dialog_16',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_action_queue_async_17',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_async_17_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2420_action_queue_async_17_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_play_sound_18',
        "command": 'play_sound',
        "args": [Sounds._076_BOOSTERS_TRAIN_HORN, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_pause_19',
        "command": 'pause',
        "args": [72],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_run_dialog_20',
        "command": 'run_dialog',
        "args": [3087, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._074_BOOSTERS_TRAIN, 6]
            },
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2420_action_queue_sync_21_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2420_action_queue_async_22_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2420_action_queue_async_22_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2420_unsync_dialog_23',
        "command": 'unsync_dialog',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_pause_24',
        "command": 'pause',
        "args": [24],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_enable_controls_25',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_play_sound_26',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_27',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_29',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_33',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_remove_from_level_34',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_enter_area_35',
        "command": 'enter_area',
        "args": [Rooms._040_BOOSTER_TOWER_5F_KNIFE_GUYS_JUGGLINE_ROOM_AFTER_DEFEAT, RadialDirections.NORTHWEST, 11, 125, 5, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_2420_ret_36',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
