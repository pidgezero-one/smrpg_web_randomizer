from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_2421_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x708b, 2, 'EVENT_2421_enter_area_34']
    },
    {
        "identifier": 'EVENT_2421_jmp_if_bit_clear_1',
        "command": 'jmp_if_bit_clear',
        "args": [0x708b, 1, 'EVENT_2421_enter_area_34']
    },
    {
        "identifier": 'EVENT_2421_enable_controls_2',
        "command": 'enable_controls',
        "args": [[]]
    },
    {
        "identifier": 'EVENT_2421_remove_from_current_level_3',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO]
    },
    {
        "identifier": 'EVENT_2421_remove_from_current_level_4',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.NPC_10]
    },
    {
        "identifier": 'EVENT_2421_pause_5',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2421_stop_all_background_events_6',
        "command": 'stop_all_background_events'
    },
    {
        "identifier": 'EVENT_2421_run_background_event_7',
        "command": 'run_background_event',
        "args": [2419, [_0x40Flags.RETURN_ON_LEVEL_EXIT, _0x40Flags.BIT_6]]
    },
    {
        "identifier": 'EVENT_2421_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_async_8_SUBSCRIPT_walk_to_xy_coords_0',
                "command": 'walk_to_xy_coords',
                "args": [10, 59]
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_run_dialog_9',
        "command": 'run_dialog',
        "args": [3083, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2421_action_queue_sync_10',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_sync_10_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_pause_script_resume_on_next_dialog_page_a_11',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2421_action_queue_sync_12',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_sync_12_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [4, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_pause_script_resume_on_next_dialog_page_a_13',
        "command": 'pause_script_resume_on_next_dialog_page_a'
    },
    {
        "identifier": 'EVENT_2421_action_queue_sync_14',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_sync_14_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [6, inc_sprite=0, flags=[_0x08Flags.READ_AS_MOLD, _0x08Flags.READ_AS_SEQUENCE]]
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_unsync_dialog_15',
        "command": 'unsync_dialog'
    },
    {
        "identifier": 'EVENT_2421_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_async_16_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [16]
            },
            {
                "identifier": 'EVENT_2421_action_queue_async_16_SUBSCRIPT_reset_properties_1',
                "command": 'reset_properties'
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_play_sound_17',
        "command": 'play_sound',
        "args": [Sounds._076_BOOSTERS_TRAIN_HORN, 6]
    },
    {
        "identifier": 'EVENT_2421_pause_18',
        "command": 'pause',
        "args": [72]
    },
    {
        "identifier": 'EVENT_2421_action_queue_sync_19',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_8],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._074_BOOSTERS_TRAIN, 6]
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_set_sprite_sequence_1',
                "command": 'set_sprite_sequence',
                "args": [13, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_fixed_f_coord_on_2',
                "command": 'fixed_f_coord_on'
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_set_priority_4',
                "command": 'set_priority',
                "args": [2]
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_shift_northwest_steps_5',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_19_SUBSCRIPT_visibility_off_6',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_action_queue_sync_20',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_9],
        "subscript": [
            {
                "identifier": 'EVENT_2421_action_queue_sync_20_SUBSCRIPT_set_sprite_sequence_0',
                "command": 'set_sprite_sequence',
                "args": [0, inc_sprite=0, flags=[_0x08Flags.READ_AS_SEQUENCE]]
            },
            {
                "identifier": 'EVENT_2421_action_queue_sync_20_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_2421_run_dialog_21',
        "command": 'run_dialog',
        "args": [3087, AreaObjects.NPC_14, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]]
    },
    {
        "identifier": 'EVENT_2421_stop_embedded_action_script_22',
        "command": 'stop_embedded_action_script',
        "args": [AreaObjects.NPC_9]
    },
    {
        "identifier": 'EVENT_2421_pause_23',
        "command": 'pause',
        "args": [24]
    },
    {
        "identifier": 'EVENT_2421_enable_controls_24',
        "command": 'enable_controls',
        "args": [[ControllerDirections.LEFT, ControllerDirections.RIGHT, ControllerDirections.DOWN, ControllerDirections.UP, ControllerDirections.X, ControllerDirections.A, ControllerDirections.Y, ControllerDirections.B]]
    },
    {
        "identifier": 'EVENT_2421_play_sound_25',
        "command": 'play_sound',
        "args": [Sounds._000_SILENCE, 6]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_26',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_0, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_27',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_1, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_28',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_2, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_29',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_3, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_30',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_4, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_31',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_5, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_32',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_6, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_remove_from_level_33',
        "command": 'remove_from_level',
        "args": [AreaObjects.NPC_7, Rooms._038_BOOSTER_TOWER_9F_BOOSTERS_BOMBTHROWING_ROOM_WRAIL_TRACKS]
    },
    {
        "identifier": 'EVENT_2421_enter_area_34',
        "command": 'enter_area',
        "args": [Rooms._198_BOOSTER_TOWER_8F_AREA_03_3LEVEL_WONE_CHOMP, RadialDirections.SOUTHWEST, 28, 55, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]]
    },
    {
        "identifier": 'EVENT_2421_ret_35',
        "command": 'ret'
    }
]
