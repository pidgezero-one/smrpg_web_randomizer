from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
from randomizer.data import items
script = [
    {
        "identifier": 'EVENT_3492_fade_in_from_black_sync_0',
        "command": 'fade_in_from_black_sync'
    },
    {
        "identifier": 'EVENT_3492_freeze_camera_1',
        "command": 'freeze_camera'
    },
    {
        "identifier": 'EVENT_3492_set_action_script_sync_2',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 599]
    },
    {
        "identifier": 'EVENT_3492_action_queue_sync_3',
        "command": 'action_queue_sync',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_east_steps_1',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_2',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_east_steps_3',
                "command": 'shift_east_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_4',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_east_steps_5',
                "command": 'shift_east_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_6',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_east_steps_7',
                "command": 'shift_east_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_8',
                "command": 'shift_southeast_steps',
                "args": [3]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_9',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_southeast_steps_10',
                "command": 'shift_southeast_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_11',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_walk_1_step_southeast_12',
                "command": 'walk_1_step_southeast'
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_east_steps_13',
                "command": 'shift_east_steps',
                "args": [5]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_14',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_shift_east_steps_15',
                "command": 'shift_east_steps',
                "args": [1]
            },
            {
                "identifier": 'EVENT_3492_action_queue_sync_3_SUBSCRIPT_set_animation_speed_16',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3492_jmp_to_subroutine_4',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3491_action_queue_sync_16']
    },
    {
        "identifier": 'EVENT_3492_jmp_if_bit_clear_5',
        "command": 'jmp_if_bit_clear',
        "args": [0x7043, 4, 'EVENT_3492_enter_area_8']
    },
    {
        "identifier": 'EVENT_3492_set_6',
        "command": 'set',
        "args": [0x7000, 1]
    },
    {
        "identifier": 'EVENT_3492_add_max_FP_7000_7',
        "command": 'add_max_FP_7000'
    },
    {
        "identifier": 'EVENT_3492_enter_area_8',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 6, 56, 0, []]
    },
    {
        "identifier": 'EVENT_3492_fade_out_music_to_volume_9',
        "command": 'fade_out_music_to_volume',
        "args": [1, 56]
    },
    {
        "identifier": 'EVENT_3492_play_sound_10',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4]
    },
    {
        "identifier": 'EVENT_3492_action_queue_async_11',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3492_action_queue_async_11_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off'
            }
        ]
    },
    {
        "identifier": 'EVENT_3492_fade_in_from_black_async_12',
        "command": 'fade_in_from_black_async'
    },
    {
        "identifier": 'EVENT_3492_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3492_action_queue_async_13_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_13_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [13, 67]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_13_SUBSCRIPT_set_short_2',
                "command": 'set_short',
                "args": [0x7016, 0x1b80]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_13_SUBSCRIPT_set_short_3',
                "command": 'set_short',
                "args": [0x7018, 0x2180]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_13_SUBSCRIPT_run_away_transfer_4',
                "command": 'run_away_transfer'
            }
        ]
    },
    {
        "identifier": 'EVENT_3492_jmp_to_subroutine_14',
        "command": 'jmp_to_subroutine',
        "args": ['EVENT_3480_action_queue_async_73']
    },
    {
        "identifier": 'EVENT_3492_action_queue_async_15',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x80, 0x02, 0xf4, 0xff]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [7]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_shift_southwest_pixels_8',
                "command": 'shift_southwest_pixels',
                "args": [4]
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_bpl_26_27_28_9',
                "command": 'bpl_26_27_28'
            },
            {
                "identifier": 'EVENT_3492_action_queue_async_15_SUBSCRIPT_set_solidity_bits_10',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3492_set_action_script_sync_16',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 466]
    },
    {
        "identifier": 'EVENT_3492_jmp_17',
        "command": 'jmp',
        "args": ['EVENT_3489_enable_controls_3']
    },
    {
        "identifier": 'EVENT_3492_ret_18',
        "command": 'ret'
    }
]
