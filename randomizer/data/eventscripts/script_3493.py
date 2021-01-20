from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3493_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7078, 5, 'EVENT_3493_fade_in_from_black_sync_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_run_background_event_1',
        "command": 'run_background_event',
        "args": [3496, [_0x40Flags.RETURN_ON_LEVEL_EXIT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_fade_in_from_black_sync_2',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_freeze_camera_3',
        "command": 'freeze_camera',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_set_action_script_sync_4',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 600],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.SCREEN_FOCUS, 647],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_jmp_to_subroutine_6',
        "command": 'jmp_to_subroutine',
        "args": [0x6752],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._069_MIDAS_RIVER_WATERFALL, RadialDirections.SOUTH, 9, 56, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_fade_out_music_to_volume_8',
        "command": 'fade_out_music_to_volume',
        "args": [1, 56],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._035_RUNNING_WATER, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3493_action_queue_async_10_SUBSCRIPT_visibility_off_0',
                "command": 'visibility_off',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3493_fade_in_from_black_async_11',
        "command": 'fade_in_from_black_async',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_action_queue_async_12',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3493_action_queue_async_12_SUBSCRIPT_clear_solidity_bits_0',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_12_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [12, 67]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_12_SUBSCRIPT_set_short_2',
                "command": 'set_short',
                "args": [0x7016, 0x1980]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_12_SUBSCRIPT_set_short_3',
                "command": 'set_short',
                "args": [0x7018, 0x2080]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_12_SUBSCRIPT_run_away_transfer_4',
                "command": 'run_away_transfer',
                "args": []
            },
        ]
    },
    {
        "identifier": 'EVENT_3493_jmp_to_subroutine_13',
        "command": 'jmp_to_subroutine',
        "args": [0x6247],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_action_queue_async_14',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._033_JUMPING_BOUNCING_FISH, 4]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_set_animation_speed_1',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.SLOW, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_shift_south_pixels_2',
                "command": 'shift_south_pixels',
                "args": [32]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_db_3',
                "command": 'db',
                "args": [0x20, 0x04]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_db_4',
                "command": 'db',
                "args": [0x25, 0x80, 0x02, 0xf2, 0xff]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_set_animation_speed_5',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.NORMAL, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_play_sound_6',
                "command": 'play_sound',
                "args": [Sounds._010_TRAMPOLINE, 4]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_shift_northwest_steps_7',
                "command": 'shift_northwest_steps',
                "args": [6]
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_bpl_26_27_28_8',
                "command": 'bpl_26_27_28',
                "args": []
            },
            {
                "identifier": 'EVENT_3493_action_queue_async_14_SUBSCRIPT_set_solidity_bits_9',
                "command": 'set_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            },
        ]
    },
    {
        "identifier": 'EVENT_3493_set_action_script_sync_15',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 466],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_jmp_16',
        "command": 'jmp',
        "args": ['EVENT_3489_enable_controls_3'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3493_ret_17',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
]
