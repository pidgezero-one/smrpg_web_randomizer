from randomizer.data.eventtables import ControllerDirections, RadialDirections, Rooms, Sounds, AreaObjects, NPCPackets, Locations, Shops, EventSequences, MenuTutorials, OverworldSequences, PlayableCharacters, EquipSlots, DialogDurations, IntroTitles, Colours, PaletteSetTypes, Music, MusicDirections, MusicPitch, Coords, CoordUnits, Tutorials, _0x40Flags, _0x60Flags, _0x62Flags, _0x63Flags, _0x68Flags, _0x6AFlags, _0x6BFlags, _0x81Flags, _0x84Flags
from randomizer.data.objectsequencetables import SequenceSpeeds, VramPriority, _0x08Flags, _0x0AFlags, _0x10Flags
script = [
    {
        "identifier": 'EVENT_1819_jmp_if_bit_set_0',
        "command": 'jmp_if_bit_set',
        "args": [0x7043, 0, 'EVENT_1819_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_set_bit_1',
        "command": 'set_bit',
        "args": [0x7043, 0],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_pause_2',
        "command": 'pause',
        "args": [1],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_jmp_if_mario_in_air_3',
        "command": 'jmp_if_mario_in_air',
        "args": ['EVENT_1819_pause_2'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_jmp_if_bit_set_4',
        "command": 'jmp_if_bit_set',
        "args": [0x704e, 6, 'EVENT_1819_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_set_7000_to_object_coord_5',
        "command": 'set_7000_to_object_coord',
        "args": [AreaObjects.MARIO, Coords.Y, CoordUnits.PIXEL],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_mem_compare_6',
        "command": 'mem_compare',
        "args": [0x7000, 48],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_jmp_if_comparison_result_is_greater_or_equal_7',
        "command": 'jmp_if_comparison_result_is_greater_or_equal',
        "args": ['EVENT_1819_ret_13'],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_reset_coords_8',
        "command": 'reset_coords',
        "args": [AreaObjects.NPC_3],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_set_action_script_async_9',
        "command": 'set_action_script_async',
        "args": [AreaObjects.NPC_3, 160],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_action_queue_async_10',
        "command": 'action_queue_async',
        "args": [AreaObjects.NPC_3],
        "subscript": [
            {
                "identifier": 'EVENT_1819_action_queue_async_10_SUBSCRIPT_set_animation_speed_0',
                "command": 'set_animation_speed',
                "args": [SequenceSpeeds.FAST, [_0x10Flags.WALKING, _0x10Flags.SEQUENCE]]
            },
            {
                "identifier": 'EVENT_1819_action_queue_async_10_SUBSCRIPT_walk_to_xy_coords_1',
                "command": 'walk_to_xy_coords',
                "args": [28, 37]
            },
            {
                "identifier": 'EVENT_1819_action_queue_async_10_SUBSCRIPT_face_southeast_2',
                "command": 'face_southeast',
                "args": []
            }
        ]
    },
    {
        "identifier": 'EVENT_1819_run_dialog_11',
        "command": 'run_dialog',
        "args": [1277, AreaObjects.MARIO, [_0x60Flags.CLOSABLE, _0x60Flags.ASYNC, _0x60Flags.MULTILINE]],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_set_action_script_sync_12',
        "command": 'set_action_script_sync',
        "args": [AreaObjects.NPC_3, 714],
        "subscript": []
    },
    {
        "identifier": 'EVENT_1819_ret_13',
        "command": 'ret',
        "args": [],
        "subscript": []
    }
]
