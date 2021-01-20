from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1733_set_short_0',
        "command": 'set_short',
        "args": [0x7030, 0x0000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_enable_controls_1',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_summon_to_level_2',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_2, Rooms._148_GAME_INTRO_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_summon_to_level_3',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_3, Rooms._148_GAME_INTRO_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_summon_to_level_4',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_4, Rooms._148_GAME_INTRO_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_summon_to_level_5',
        "command": 'summon_to_level',
        "args": [AreaObjects.NPC_5, Rooms._148_GAME_INTRO_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_enable_trigger_in_level_6',
        "command": 'enable_trigger_in_level',
        "args": [AreaObjects.NPC_0, Rooms._148_GAME_INTRO_BANDITS_WAY_AREA_04],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._148_GAME_INTRO_BANDITS_WAY_AREA_04, RadialDirections.EAST, 7, 24, 4, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_action_queue_async_8',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1733_action_queue_async_8_SUBSCRIPT_set_solidity_bits_0',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_8_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1733_action_queue_sync_9',
        "command": 'action_queue_sync',
        "args": [AreaObjects.NPC_7],
        "subscript": [
            {
                "identifier": 'EVENT_1733_action_queue_sync_9_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FASTEST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1733_action_queue_sync_9_SUBSCRIPT_fixed_f_coord_on_1',
                "command": 'fixed_f_coord_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1733_action_queue_sync_9_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [16]
            }
        ]
    },
    {
        "identifier": 'EVENT_1733_fade_in_from_black_sync_10',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1733_action_queue_async_11_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_11_SUBSCRIPT_shift_northeast_pixels_1',
                "command": 'shift_northeast_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_11_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1733_move_script_to_background_thread_2_12',
        "command": 'move_script_to_background_thread_2',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1733_action_queue_async_13_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_13_SUBSCRIPT_floating_off_1',
                "command": 'floating_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_13_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [5]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_13_SUBSCRIPT_jump_to_height_silent_3',
                "command": 'jump_to_height_silent',
                "args": [108]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_13_SUBSCRIPT_shift_east_steps_4',
                "command": 'shift_east_steps',
                "args": [2]
            }
        ]
    },
    {
        "identifier": 'EVENT_1733_set_action_script_sync_14',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_2, 769],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 769],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_4, 769],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_set_action_script_sync_17',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_5, 769],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_run_background_event_18',
        "command": 'run_background_event',
        "args": [1734, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_east_steps_0',
                "command": 'shift_east_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_northwest_steps_1',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_southwest_steps_2',
                "command": 'shift_southwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_northwest_steps_3',
                "command": 'shift_northwest_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_northeast_steps_4',
                "command": 'shift_northeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_southeast_steps_5',
                "command": 'shift_southeast_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_1733_action_queue_async_19_SUBSCRIPT_shift_northeast_steps_6',
                "command": 'shift_northeast_steps',
                "args": [3]
            }
        ]
    },
    {
        "identifier": 'EVENT_1733_fade_out_to_black_sync_duration_20',
        "command": 'fade_out_to_black_sync_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_action_queue_sync_21',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1733_action_queue_sync_21_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.BIT_4, _0x0AFlags.CANT_PASS_NPCS, _0x0AFlags.CANT_WALK_THROUGH, _0x0AFlags.BIT_7]]
            },
            {
                "identifier": 'EVENT_1733_action_queue_sync_21_SUBSCRIPT_shift_west_steps_1',
                "command": 'shift_west_steps',
                "args": [6]
            }
        ]
    },
    {
        "identifier": 'EVENT_1733_pause_script_until_effect_done_22',
        "command": 'pause_script_until_effect_done',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_move_script_to_main_thread_23',
        "command": 'move_script_to_main_thread',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_clear_bit_24',
        "command": 'clear_bit',
        "args": [0x7076, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_set_bit_3_25',
        "command": 'set_bit_3',
        "args": [0x1d8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1733_jmp_to_event_26',
        "command": 'jmp_to_event',
        "args": [1728],
        "subscript": []
    }
]
