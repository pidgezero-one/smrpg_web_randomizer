from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3494_run_background_event_0',
        "command": 'run_background_event',
        "args": [3497, [_0x40Flags.RETURN_ON_LEVEL_EXIT]]
    },
    {
        "identifier": 'EVENT_3494_fade_in_from_black_sync_1',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3494_freeze_camera_2',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3494_set_action_script_sync_3',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 601]
    },
    {
        "identifier": 'EVENT_3494_action_queue_sync_4',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_pause_0',
                "command": 'pause',
                "args": [220]
            },
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_shift_west_steps_2',
                "command": 'shift_west_steps',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_set_animation_speed_3',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_shift_northwest_steps_4',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_walk_1_step_northwest_5',
                "command": 'walk_1_step_northwest'
            },
            {
                "identifier": 'EVENT_3494_action_queue_sync_4_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3494_move_script_to_background_thread_2_5',
        "command": 'move_script_to_background_thread_2'
    },
    {
        "identifier": 'EVENT_3494_jmp_to_subroutine_6',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3491_action_queue_sync_16']
    },
    {
        "identifier": 'EVENT_3494_move_script_to_main_thread_7',
        "command": 'move_script_to_main_thread'
    },
    {
        "identifier": 'EVENT_3494_jmp_if_bit_set_8',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 6, 'EVENT_3494_enter_area_11']
    },
    {
        "identifier": 'EVENT_3494_add_frog_coins_9',
        "command": 'add_frog_coins',
        "args": [1]
    },
    {
        "identifier": 'EVENT_3494_set_bit_10',
        "command": 'set_bit',
        "args": [0x7078, 6]
    },
    {
        "identifier": 'EVENT_3494_enter_area_11',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 4, 83, 0, []]
    },
    {
        "identifier": 'EVENT_3494_fade_out_music_to_volume_12',
        "command": 'fade_out_music_to_volume',
        "args": [1, 56]
    },
    {
        "identifier": 'EVENT_3494_play_sound_13',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4]
    },
    {
        "identifier": 'EVENT_3494_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3494_action_queue_async_14_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3494_fade_in_from_black_async_15',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3494_action_queue_async_16',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3494_action_queue_async_16_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_16_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [4, 76]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_16_SUBSCRIPT_set_short_2',
                "command": 'set_short',
                "args": [0x7016, 0x0580]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_16_SUBSCRIPT_set_short_3',
                "command": 'set_short',
                "args": [0x7018, 0x2180]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_16_SUBSCRIPT_run_away_transfer_4',
                "command": 'run_away_transfer'
            }
        ]
    },
    {
        "identifier": 'EVENT_3494_jmp_to_subroutine_17',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3480_action_queue_async_73']
    },
    {
        "identifier": 'EVENT_3494_action_queue_async_18',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_shift_south_steps_2',
                "command": 'shift_south_steps',
                "args": [8]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x80, 0x02, 0xe4, 0xff]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_shift_southeast_steps_7',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3494_action_queue_async_18_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3494_set_action_script_sync_19',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 466]
    },
    {
        "identifier": 'EVENT_3494_jmp_20',
        "command": 'jmp',
        "args": ['EVENT_3489_enable_controls_3']
    },
    {
        "identifier": 'EVENT_3494_ret_21',
        "command": 'ret'
    }
]
