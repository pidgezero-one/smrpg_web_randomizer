from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1905_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7096, 0, 'EVENT_1905_enter_area_9'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_remove_from_current_level_1',
        "command": 'remove_from_current_level',
        "args": [AreaObjects.MARIO],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_play_sound_2',
        "command": 'play_sound',
        "args": [Sounds._019_LONG_FALL, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_pause_3',
        "command": 'pause',
        "args": [50],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_fade_out_to_black_sync_duration_4',
        "command": 'fade_out_to_black_sync_duration',
        "args": [180],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_play_sound_5',
        "command": 'play_sound',
        "args": [Sounds._091_TUMBLING_BOULDERS, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_action_queue_async_6',
        "command": 'action_queue_async',
        "args": [AreaObjects.SCREEN_FOCUS],
        "subscript": [
            {
                "identifier": 'EVENT_1905_action_queue_async_6_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.VERY_FAST, [_0x10Flags.WALKING]]
            },
            {
                "identifier": 'EVENT_1905_action_queue_async_6_SUBSCRIPT_start_loop_n_times_1',
                "command": 'start_loop_n_times',
                "args": [59]
            },
            {
                "identifier": 'EVENT_1905_action_queue_async_6_SUBSCRIPT_shift_east_pixels_2',
                "command": 'shift_east_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1905_action_queue_async_6_SUBSCRIPT_shift_west_pixels_3',
                "command": 'shift_west_pixels',
                "args": [8]
            },
            {
                "identifier": 'EVENT_1905_action_queue_async_6_SUBSCRIPT_end_loop_4',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1905_enter_area_7',
        "command": 'enter_area',
        "args": [Rooms._103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, RadialDirections.SOUTH, 23, 54, 0, [_0x68Flags.RUN_ENTRANCE_EVENT]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_ret_8',
        "command": 'ret',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_enter_area_9',
        "command": 'enter_area',
        "args": [Rooms._103_SMITHY_FACTORY_AREA_17_DOMINO_AND_CLOAKERS_ROOM, RadialDirections.SOUTH, 23, 54, 0, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_fade_in_from_black_sync_10',
        "command": 'fade_in_from_black_sync',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_set_bit_11',
        "command": 'set_bit',
        "args": [0x7049, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_enable_controls_12',
        "command": 'enable_controls',
        "args": [[]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1905_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1905_action_queue_async_13_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [24, 54, 18, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_1905_action_queue_async_13_SUBSCRIPT_jump_to_height_silent_1',
                "command": 'jump_to_height_silent',
                "args": [0]
            }
        ]
    },
    {
        "identifier": 'EVENT_1905_ret_14',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
