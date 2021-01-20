from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1544_freeze_all_npcs_until_return_0',
        "command": 'freeze_all_npcs_until_return',
        "args": [],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_set_short_mem_1',
        "command": 'set_short_mem',
        "args": [0x7000, 0x70a8],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_set_short_mem_2',
        "command": 'set_short_mem',
        "args": [0x70a9, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_set_7000_to_object_coord_3',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_set_short_mem_4',
        "command": 'set_short_mem',
        "args": [0x700c, 0x7000],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_set_action_script_sync_5',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.MARIO, 781],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_pause_6',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_action_queue_sync_7',
        "command": 'action_queue_sync',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1544_action_queue_sync_7_SUBSCRIPT_add_0',
                "command": 'add',
                "args": [0x700c, 0x01]
            },
            {
                "identifier": 'EVENT_1544_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1544_action_queue_sync_7_SUBSCRIPT_face_east_2',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_1544_action_queue_sync_7_SUBSCRIPT_fixed_f_coord_on_3',
                "command": 'fixed_f_coord_on',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1544_pause_8',
        "command": 'pause',
        "args": [2],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_jmp_if_bit_set_9',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1544_action_queue_sync_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_set_7000_to_object_coord_10',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.F],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_jmp_if_var_not_equals_short_11',
        "command": 'jmp_if_var_not_equals_short',
        "args": [0x7000, 2, 'EVENT_1544_action_queue_sync_7'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_pixelate_layers_12',
        "command": 'pixelate_layers',
        "args": [[_0x84Flags.LAYER_1, _0x84Flags.LAYER_2, _0x84Flags.LAYER_3], 9, 70],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_action_queue_async_13',
        "command": 'action_queue_async',
        "args": [AreaObjects.MARIO],
        "subscript": [
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_play_sound_0',
                "command": 'play_sound',
                "args": [Sounds._112_DRAINING_WATER, 4]
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_fixed_f_coord_off_1',
                "command": 'fixed_f_coord_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_set_2',
                "command": 'set',
                "args": [0x700c, 2]
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_start_loop_n_times_3',
                "command": 'start_loop_n_times',
                "args": [15]
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_add_4',
                "command": 'add',
                "args": [0x700c, 0x01]
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_face_east_5',
                "command": 'face_east',
                "args": []
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_visibility_on_6',
                "command": 'visibility_on',
                "args": []
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_shift_f_direction_pixels_7',
                "command": 'shift_f_direction_pixels',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_visibility_off_8',
                "command": 'visibility_off',
                "args": []
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_pause_9',
                "command": 'pause',
                "args": [1]
            },
            {
                "identifier": 'EVENT_1544_action_queue_async_13_SUBSCRIPT_end_loop_10',
                "command": 'end_loop',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1544_fade_out_to_black_async_duration_14',
        "command": 'fade_out_to_black_async_duration',
        "args": [30],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1544_ret_15',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
