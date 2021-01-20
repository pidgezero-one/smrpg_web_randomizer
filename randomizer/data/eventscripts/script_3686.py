from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_3686_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7044, 6, 'EVENT_3584_ret_0'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_set_bit_1',
        "command": 'set_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_action_queue_async_2',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3686_action_queue_async_2_SUBSCRIPT_face_southwest_0',
                "command": 'face_southwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_2_SUBSCRIPT_visibility_off_1',
                "command": 'visibility_off',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3686_pause_3',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_play_sound_4',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_apply_tile_mod_5',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_6',
        "command": 'pause',
        "args": [60],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_play_sound_7',
        "command": 'play_sound',
        "args": [Sounds._155_POSTCREDITS_MARIO_THEME_WHISTLE, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_8',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_play_sound_9',
        "command": 'play_sound',
        "args": [Sounds._006_RUNNING_WATER, 4],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_short_10',
        "command": 'pause_short',
        "args": [480],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_start_loop_n_times_11',
        "command": 'start_loop_n_times',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_play_sound_12',
        "command": 'play_sound',
        "args": [Sounds._018_SUDDEN_STOP, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_13',
        "command": 'pause',
        "args": [8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_stop_sound_14',
        "command": 'stop_sound',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_15',
        "command": 'pause',
        "args": [20],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_end_loop_16',
        "command": 'end_loop',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_17',
        "command": 'pause',
        "args": [120],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_palette_set_18',
        "command": 'palette_set',
        "args": [142, 1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_action_queue_async_19',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3686_action_queue_async_19_SUBSCRIPT_transfer_to_xyzf_0',
                "command": 'transfer_to_xyzf',
                "args": [10, 13, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_19_SUBSCRIPT_transfer_xyzf_pixels_1',
                "command": 'transfer_xyzf_pixels',
                "args": [252, 4, 0, RadialDirections.EAST]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_19_SUBSCRIPT_visibility_on_2',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_19_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [30]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_19_SUBSCRIPT_clear_solidity_bits_4',
                "command": 'clear_solidity_bits',
                "args": [[_0x0AFlags.CANT_PASS_WALLS]]
            }
        ]
    },
    {
        "identifier": 'EVENT_3686_play_sound_20',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_apply_tile_mod_21',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 1, [_0x6AFlags.USE_ALTERNATE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_action_queue_async_22',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_shift_southwest_steps_0',
                "command": 'shift_southwest_steps',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [60]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_face_west_2',
                "command": 'face_west',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_face_northwest_4',
                "command": 'face_northwest',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_pause_5',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_face_north_6',
                "command": 'face_north',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_pause_7',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_22_SUBSCRIPT_face_northeast_8',
                "command": 'face_northeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3686_pause_23',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_play_sound_24',
        "command": 'play_sound',
        "args": [Sounds._016_OPEN_DOOR, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_apply_tile_mod_25',
        "command": 'apply_tile_mod',
        "args": [Rooms._012_MARRYMORE_INN_SUITE_ROOM, 1, []],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_pause_26',
        "command": 'pause',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_action_queue_async_27',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_3686_action_queue_async_27_SUBSCRIPT_face_east_0',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_27_SUBSCRIPT_pause_1',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_27_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_27_SUBSCRIPT_pause_3',
                "command": 'pause',
                "args": [2]
            },
            {
                "identifier": 'EVENT_3686_action_queue_async_27_SUBSCRIPT_face_south_4',
                "command": 'face_south',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_3686_set_action_script_sync_28',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 395],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_clear_bit_29',
        "command": 'clear_bit',
        "args": [0x7044, 7],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_clear_bit_30',
        "command": 'clear_bit',
        "args": [0x7044, 6],
        "subscript": []
    },
    {
        "identifier": 'EVENT_3686_ret_31',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
